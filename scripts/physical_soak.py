"""Operator-run twelve-hour physical soak recorder for the exact installed release.

Run with the installed pitblu-core virtualenv Python. Credentials are prompted
interactively and never written to the evidence log.
"""

from __future__ import annotations

import asyncio
import json
import os
import time
from datetime import UTC, datetime
from getpass import getpass
from pathlib import Path
from typing import Any

import aiomqtt

from pitblu_core.api_client import ApiClient

DURATION_SECONDS = 12 * 60 * 60
POLL_SECONDS = 5
MQTT_GAP_SECONDS = 30


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


class Evidence:
    def __init__(self) -> None:
        stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
        self.path = Path.home() / f"pitblu-core-v1-soak-{stamp}.jsonl"
        fd = os.open(self.path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        self.file = os.fdopen(fd, "w", encoding="utf-8", buffering=1)

    def write(self, kind: str, **fields: Any) -> None:
        self.file.write(json.dumps({"at": utc_now(), "kind": kind, **fields}) + "\n")

    def close(self) -> None:
        self.file.close()


def read_rest(client: ApiClient, path: str) -> dict[str, Any]:
    status = client.get("/api/v1/status").data
    device = client.get(path).data
    probes = client.get(path + "/probes").data
    battery = client.get(path + "/battery").data
    heartbeat = device["heartbeat"]
    good_probes = sorted(p["probe"] for p in probes) == [1, 2, 3, 4] and all(
        p["probe"] in (1, 2, 3, 4)
        and p["present"]
        and p["fresh"]
        and p["source"] == "physical"
        and isinstance(p["temperatureC"], (int, float))
        for p in probes
    )
    good = (
        status["version"] == "1.0.0"
        and status["mqtt"]["state"] == "connected"
        and device["observedState"] == "polling"
        and heartbeat["status"] == "healthy"
        and heartbeat["fresh"]
        and heartbeat["source"] == "physical"
        and good_probes
        and battery is not None
        and battery["available"]
        and battery["fresh"]
        and battery["source"] == "physical"
    )
    return {
        "good": good,
        "version": status["version"],
        "sessionId": status["sessionId"],
        "mqttState": status["mqtt"]["state"],
        "deviceState": device["observedState"],
        "heartbeat": {
            "status": heartbeat["status"],
            "fresh": heartbeat["fresh"],
            "source": heartbeat["source"],
            "lastSuccessfulCommunicationAt": heartbeat["lastSuccessfulCommunicationAt"],
        },
        "probes": [
            {
                "probe": p["probe"],
                "present": p["present"],
                "fresh": p["fresh"],
                "temperatureC": p["temperatureC"],
                "source": p["source"],
            }
            for p in probes
        ],
        "battery": None
        if battery is None
        else {"fresh": battery["fresh"], "percentage": battery["percentage"]},
    }


async def monitor_rest(
    client: ApiClient, path: str, evidence: Evidence, deadline: float, counts: dict[str, Any]
) -> None:
    next_report = time.monotonic() + 60
    last_session: str | None = None
    while time.monotonic() < deadline:
        try:
            snapshot = await asyncio.to_thread(read_rest, client, path)
            evidence.write("rest", **snapshot)
            counts["restSamples"] += 1
            if last_session is not None and snapshot["sessionId"] != last_session:
                counts["sessionChanges"] += 1
                evidence.write("sessionChange", old=last_session, new=snapshot["sessionId"])
                print(f"Service session changed at {utc_now()}", flush=True)
            last_session = snapshot["sessionId"]
            if not snapshot["good"]:
                counts["restBad"] += 1
                print(f"REST gap at {utc_now()}: inspect evidence log", flush=True)
        except Exception as exc:
            evidence.write("restError", errorType=type(exc).__name__)
            counts["restBad"] += 1
            print(f"REST error at {utc_now()}: {type(exc).__name__}", flush=True)
        now = time.monotonic()
        for probe in range(1, 5):
            gap = now - counts["_lastMqttAt"][probe]
            counts["maxMqttGapSeconds"] = max(counts["maxMqttGapSeconds"], round(gap, 1))
            if gap > MQTT_GAP_SECONDS and not counts["_mqttSilent"][probe]:
                counts["mqttGaps"] += 1
                counts["_mqttSilent"][probe] = True
                evidence.write("mqttGap", probe=probe, seconds=round(gap, 1))
                print(f"MQTT probe {probe} silent for {gap:.1f}s", flush=True)
        if time.monotonic() >= next_report:
            print(
                f"{utc_now()} elapsed="
                f"{int(DURATION_SECONDS - max(0, deadline - time.monotonic()))}s "
                f"REST={counts['restSamples']} bad={counts['restBad']} "
                f"MQTT-temperature={counts['mqttTemperature']}",
                flush=True,
            )
            next_report += 60
        await asyncio.sleep(min(POLL_SECONDS, max(0, deadline - time.monotonic())))


async def monitor_mqtt(
    username: str,
    password: str,
    topic: str,
    evidence: Evidence,
    deadline: float,
    counts: dict[str, Any],
) -> None:
    while time.monotonic() < deadline:
        try:
            async with aiomqtt.Client(
                "127.0.0.1", port=1883, username=username, password=password
            ) as client:
                await client.subscribe(
                    [
                        ("pitblu/v1/service/availability", 1),
                        (topic + "/heartbeat", 1),
                        (topic + "/probes/+/temperature", 1),
                    ]
                )
                evidence.write("mqttConnected")
                remaining = max(0, deadline - time.monotonic())
                async with asyncio.timeout(remaining):
                    async for message in client.messages:
                        payload = json.loads(message.payload)
                        name = str(message.topic)
                        record = {
                            "topic": name,
                            "qos": int(message.qos),
                            "retained": bool(message.retain),
                            "sessionId": payload.get("sessionId"),
                            "source": payload.get("source"),
                        }
                        if name.endswith("/temperature"):
                            probe = int(payload["probe"])
                            now = time.monotonic()
                            gap = now - counts["_lastMqttAt"][probe]
                            counts["maxMqttGapSeconds"] = max(
                                counts["maxMqttGapSeconds"], round(gap, 1)
                            )
                            if gap > MQTT_GAP_SECONDS and not counts["_mqttSilent"][probe]:
                                counts["mqttGaps"] += 1
                                evidence.write("mqttGap", probe=probe, seconds=round(gap, 1))
                                print(f"MQTT probe {probe} gap {gap:.1f}s", flush=True)
                            counts["_lastMqttAt"][probe] = now
                            counts["_mqttSilent"][probe] = False
                            counts["mqttTemperature"] += 1
                            counts["mqttByProbe"][probe] += 1
                            record["probe"] = probe
                            record["temperatureC"] = payload.get("temperatureC")
                            if payload.get("source") != "physical" or int(message.qos) != 1:
                                counts["mqttBad"] += 1
                        else:
                            record["available"] = payload.get("available")
                            record["status"] = payload.get("status")
                            if name.endswith("/service/availability") and not payload.get(
                                "available", False
                            ):
                                counts["mqttBad"] += 1
                        evidence.write("mqtt", **record)
        except TimeoutError:
            break
        except Exception as exc:
            counts["mqttBad"] += 1
            evidence.write("mqttError", errorType=type(exc).__name__)
            print(f"MQTT error at {utc_now()}: {type(exc).__name__}", flush=True)
            await asyncio.sleep(min(2, max(0, deadline - time.monotonic())))


async def main() -> None:
    token = getpass("Administrator token: ")
    username = getpass("MQTT subscriber username: ")
    password = getpass("MQTT subscriber password: ")
    client = ApiClient(token=token)
    devices = await asyncio.to_thread(lambda: client.get("/api/v1/devices").data)
    if len(devices) != 1:
        raise SystemExit("Expected exactly one registered thermometer; soak not started")
    path = client.device_path(devices[0]["deviceId"])
    first = await asyncio.to_thread(read_rest, client, path)
    if not first["good"]:
        raise SystemExit("Four fresh physical probes, healthy heartbeat and MQTT required")
    try:
        async with aiomqtt.Client(
            "127.0.0.1", port=1883, username=username, password=password
        ) as mqtt_check:
            grants = await mqtt_check.subscribe(
                f"pitblu/v1/devices/{devices[0]['deviceId']}/probes/+/temperature", qos=1
            )
            if any(getattr(grant, "is_failure", grant == 128) for grant in grants):
                raise SystemExit("MQTT subscriber was not granted access; soak not started")
    except aiomqtt.MqttError as exc:
        raise SystemExit(f"MQTT subscriber preflight failed: {type(exc).__name__}") from None
    evidence = Evidence()
    start = time.monotonic()
    counts: dict[str, Any] = {
        "restSamples": 0,
        "restBad": 0,
        "sessionChanges": 0,
        "mqttTemperature": 0,
        "mqttByProbe": {1: 0, 2: 0, 3: 0, 4: 0},
        "mqttGaps": 0,
        "maxMqttGapSeconds": 0.0,
        "mqttBad": 0,
        "_lastMqttAt": {probe: start for probe in range(1, 5)},
        "_mqttSilent": {probe: False for probe in range(1, 5)},
    }
    deadline = start + DURATION_SECONDS
    evidence.write(
        "start",
        durationSeconds=DURATION_SECONDS,
        version=first["version"],
        sessionId=first["sessionId"],
        deviceId=devices[0]["deviceId"],
    )
    print(f"Twelve-hour soak started {utc_now()}; log: {evidence.path}", flush=True)
    try:
        await asyncio.gather(
            monitor_rest(client, path, evidence, deadline, counts),
            monitor_mqtt(
                username,
                password,
                f"pitblu/v1/devices/{devices[0]['deviceId']}",
                evidence,
                deadline,
                counts,
            ),
        )
    finally:
        elapsed = round(time.monotonic() - start, 1)
        review = (
            elapsed < DURATION_SECONDS
            or counts["restBad"] > 0
            or counts["sessionChanges"] > 0
            or counts["mqttBad"] > 0
            or counts["mqttGaps"] > 0
            or any(n == 0 for n in counts["mqttByProbe"].values())
        )
        summary = {key: value for key, value in counts.items() if not key.startswith("_")}
        evidence.write("summary", elapsedSeconds=elapsed, reviewRequired=review, **summary)
        evidence.close()
        print(f"Soak {'REVIEW REQUIRED' if review else 'NO AUTOMATIC GAPS'}: {summary}", flush=True)
        print(f"Evidence: {evidence.path}", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
