# v1.0.0rc2 partial Raspberry Pi evidence

Operator-reported checks against canonical tag `v1.0.0rc2`, commit
`07a2034012c69f4412ecd2cb185363ef222b90fd`. This candidate did not pass
physical reconnect acceptance.

On 23 September 2026 the canonical checkout resolved to the exact commit and
the guided prerequisite check passed on Debian 13/aarch64 with Python 3.13.5.
The guided upgrade reported installed runtime v1.0.0rc2 and healthy local API.
The authenticated support check reported the registered physical thermometer
polling, recent successful communication, four fresh channel responses and a
fresh 50% battery reading. MQTT was disabled. Four fresh channel responses are
not proof of four inserted probes; only two were available.

At 2026-09-23 11:41:30 +01:00, a manual force reconnect failed its asynchronous
operation with `device_operation_failed`. The next support check showed backoff,
stale communication at 44 seconds, zero fresh probe readings and no fresh battery.
Sanitised service events reported six `connect_initialise` failures of class
`AdapterError`. A later check still showed backoff and stale communication at
181 seconds. These events do not identify which bounded adapter operation failed.

The operator used the protected backup from before candidate deployment to roll
back to v0.9.0. The rollback selected the original release, and a follow-up check
confirmed active service and public health. Authenticated REST then reported
runtime v0.9.0, connected polling, fresh physical probes 1 and 2 at 19.0°C and
20.0°C, absent probes 3 and 4, and fresh battery at 40%. The first immediate
health check after rollback failed to connect; the follow-up succeeded without a
recorded service restart.

The fresh-discovery change in rc2 did not resolve force reconnect on this Pi.
No final v1.0.0 physical gate is marked passed from this candidate. Four inserted
probes remain required; display comparison, MQTT/Last Will, restart/session and
twelve-hour soak remain pending.
