# v1.0.0rc1 partial Raspberry Pi evidence

Operator-reported physical checks against canonical tag `v1.0.0rc1`, commit
`f0cb79e505335e1a2ff4d5a141d7551ffbc93ad4`. This record is partial and
does not approve a final release.

## Environment and upgrade

On 22 September 2026 the Pi reported Debian 13.6 Trixie, aarch64, Python 3.13.5,
active `pitblu-core` v0.9.0 and a powered Bluetooth controller. The canonical
source checkout matched the candidate commit and all guided installer prerequisite
checks passed. The operator ran the guided upgrade and reported success. The
installed support check reported active service, healthy local API, ready state,
runtime v1.0.0rc1, synchronised clock, one registered device in polling state,
healthy physical communication and a fresh physical battery reading at 50%.
MQTT was disabled.

## Physical thermometer observations

- At 2026-09-22 18:52:02 UTC, probes 1 and 2 were present, fresh and physically
  reported 20.0°C. Probes 3 and 4 were absent with fresh null temperatures.
  Display temperatures were not supplied, so the display comparison is pending.
- Probe 2 removal was reported within 5.4 seconds, with `present=false`,
  `fresh=true` and null temperature. The timing includes the operator's action.
- At 2026-09-22 18:55:53 UTC, all four probes were absent with fresh null
  temperatures. The physical heartbeat remained healthy and its most recent
  successful exchange was less than a second before the REST check. This confirms
  valid absent-probe replies advanced communication evidence.
- Four inserted probes were unavailable and were not tested.

## Reconnect failure

Two operator-initiated `pitblu-core-config igrill reconnect` attempts returned a
failed asynchronous operation with `device_operation_failed`. Sanitised service
events placed the failures at `connect_initialise`. After the first attempt,
automatic recovery restored connected polling and healthy heartbeat. After the
second attempt, the support check showed backoff, stale heartbeat at 33 seconds,
zero fresh probe readings and no fresh battery reading. No later recovery result
was supplied for the second attempt. The force-reconnect gate therefore failed.

Restart/session, BLE-loss ageing, broker/Last Will, rollback, four-probe comparison
and four-hour soak checks remain pending. No result here may be carried forward
as a pass for a changed candidate without relevant retesting.
