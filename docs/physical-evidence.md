# Raspberry Pi and iGrill test evidence

This is a summary of the operator's physical checks before v1.0.0 was
published. The tests used a Debian 13 Raspberry Pi, Python 3.13, a Weber iGrill
V202 and build `2ad2aa5d133117c137a1005572d6221f6616102b`. The v1.0.0
gateway implementation is unchanged from that build, but the published v1.0.0
package had not itself been installed and checked on the Pi at publication.

## What was observed

- All four probes were inserted and reported fresh physical temperatures of
  20°C, 20°C, 20°C and 19°C. The iGrill display showed the same four values.
- Removing probe 2 changed its state to absent, with no temperature, after
  12.5 seconds. With no probes inserted, the iGrill still answered and the
  communication heartbeat remained healthy.
- Disconnect followed by ordinary Connect worked. Force Reconnect succeeded
  during automatic-recovery backoff. Turning the iGrill off produced stale
  telemetry; turning it on again restored polling without a manual service
  restart.
- REST and the live SSE heartbeat reported physical communication. MQTT
  delivered live probe temperatures and retained service/heartbeat state at
  QoS 1. A separate subscriber observed the broker's offline Last Will after
  a forced service failure, followed by online state from a new session.
- Service restart, broker restart, Pi reboot and a Bluetooth-service
  interruption were followed by working physical readings. These were
  targeted checks, not a guarantee against every future failure.
- A continuous twelve-hour run ended on 24 September 2026 with 7,094 good
  authenticated REST samples, 23,904 live MQTT temperature messages (5,976
  per probe), zero reported errors or session changes, and a maximum observed
  MQTT temperature gap of 11.8 seconds. The operator retains the detailed
  private evidence log; it is not included in the repository.

## What this does not prove

The timed power-off test did not leave the Bluetooth link connected long
enough to observe a connected-but-unresponsive heartbeat. The link had already
disconnected at 9.7 seconds; the heartbeat became stale at 15.7 seconds.
That specific behaviour remains unverified.

Fresh registration, invalid-temperature handling, token rotation and a clean
install/rollback of the published v1.0.0 package also lack recorded physical
results. They were waived by the release owner for publication, not passed.
See the [release status](release-status.md) and
[acceptance checklist](physical-acceptance.md). Keep independent temperature
checks during a cook.
