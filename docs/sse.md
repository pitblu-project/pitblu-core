# Live events (SSE)

Use SSE when an application needs changes as they happen. REST remains the
source for current state: start with a REST snapshot and refresh it after a
stream interruption. SSE is not a durable history feed.

## Connect

Open `GET /api/v1/events/stream` with the administrator bearer token. The
response is `text/event-stream` with no-cache and no-buffering headers.
Native browser `EventSource` cannot set an `Authorization` header, so a web
application should use its own authenticated backend relay or a fetch-based
stream client. Never put the token in the URL or browser storage.

The stream sends **new events only**. There is no initial snapshot, durable
cursor or `Last-Event-ID` replay. `GET /api/v1/events` exposes only the most
recent 100 in-memory events and is not a substitute for REST reconciliation.

## Read a frame

Each event frame has an ID, a named event type and JSON data, followed by a
blank line:

```text
id: <unique event ID>
event: probe.temperature
data: {"schemaVersion":1,"eventId":"<unique event ID>","sessionId":"<process session>","type":"probe.temperature","observedAt":"2026-09-07T12:00:00+00:00","sequence":9,"source":"physical","deviceId":"igrill-v202-example","probe":1,"data":{"temperatureC":21.0}}

```

Parse complete frames rather than assuming one network read contains one
event. Every JSON event has `schemaVersion`, `eventId`, `sessionId`, `type`,
`observedAt`, `sequence`, `source`, `deviceId`, `probe` and `data`.
`deviceId` and `probe` may be null when they do not apply. `source` is
`physical` or `simulated`; do not present simulated data as live hardware.

| Event name | Fields inside `data` |
| --- | --- |
| `service.availability` | `available` |
| `device.availability` | `available`, sometimes `reason` |
| `device.connection` | `state` |
| `thermometer.heartbeat` | `status`, `lastSuccessfulCommunicationAt`, `fresh`, `staleAfterSeconds` |
| `device.battery` | `available`, `percentage`, sometimes `reason` |
| `probe.availability` | `available`, `present`, sometimes `reason` |
| `probe.temperature` | `temperatureC` |
| `operation.state` | `operationId`, `kind`, `status`, `errorCode` |
| `configuration.changed` | `version`, changed `settings` names; no values or secrets |

An idle `: heartbeat` line is an SSE transport comment, **not** a
`thermometer.heartbeat` event and not proof of a fresh temperature. It is
sent at the configured `polling.availability_heartbeat` interval when no
event arrives.

## Recover safely

On first connection or reconnection, attach the stream, buffer events while
fetching current REST device/probe/battery state, then reconcile. If the
stream closes, mark the feed interrupted, reconnect with bounded backoff and
fetch REST state again. A new `sessionId` means the service restarted; do not
continue comparing its sequence counters with the old session. There is no
cross-resource or cross-transport global sequence. A slow stream can lose
older queued events, so refresh REST whenever continuity is uncertain.

Authentication is checked on connection. Rotating the token does not revoke
an already-open stream; close it when you rotate credentials. The number of
simultaneous SSE clients is limited (eight by default); excess connections
return HTTP 429. Normal service shutdown closes streams without promising a
final offline event. For complete API shapes, see the
[frontend integration contract](frontend-integration.md).
