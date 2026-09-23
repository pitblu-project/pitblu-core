# v1.0.0rc3 partial Raspberry Pi evidence

Operator-reported checks against canonical tag `v1.0.0rc3`, commit
`4bb5e437272bb39e3e893fff12f381e16e04461d`. This diagnostic candidate
did not pass physical reconnect acceptance.

On 23 September 2026, the canonical tag was cloned into a separate Pi checkout.
The guided prerequisite check passed on Debian 13/aarch64 with Python 3.13 and
a powered Bluetooth controller. The guided upgrade reported runtime v1.0.0rc3,
active service and healthy local API. The authenticated support check reported
the registered thermometer polling, communication four seconds earlier, four
fresh channel responses and fresh 40% battery. Four fresh channel responses do
not mean four probes were inserted; only two probes were available.

A single force-reconnect request reached a terminal failed operation with
`device_operation_failed`. Five sanitised service events in the next ten-minute
window reported `connect_initialise`, `AdapterError` and the fixed first-party
detail `BLE connection and GATT service resolution timed out`. This locates the
failure before model-specific authentication and probe reads; it does not by
itself establish the underlying BlueZ or radio cause. No second manual reconnect
was attempted.

The upgrade's printed protected backup pointed to an rc3 release, so it was not
used as a v0.9.0 rollback target. The operator selected the newer backup
`backup-LdOfiFS4`, which pointed to the previously verified v0.9.0 release.
Rollback created another safety backup and restored runtime v0.9.0. The service
was active, local `/health` returned `ok`, and authenticated REST reported
connected polling, fresh physical probes 1 and 2 at 19.0°C and 20.0°C,
absent probes 3 and 4, and fresh 50% battery.

The rc3 diagnosis motivates a narrowly scoped BlueZ release before reconnect
in rc4, but rc4 has no physical evidence yet. Four inserted probes, display
comparison, MQTT/Last Will, restart/session and four-hour soak remain pending.
