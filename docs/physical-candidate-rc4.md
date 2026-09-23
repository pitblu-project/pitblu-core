# v1.0.0rc4 partial Raspberry Pi evidence

Operator-reported checks against canonical tag `v1.0.0rc4`, commit
`81f01c2e8c952734aa186e750145481331e3ab68`. This is partial physical
evidence, not final v1.0.0 acceptance.

On 23 September 2026, the tag was cloned into a separate Pi checkout. The guided
prerequisite check passed on Debian 13/aarch64 with Python 3.13 and a powered
Bluetooth controller. The guided upgrade reported runtime v1.0.0rc4, active
service and healthy local API. The authenticated support check reported the
registered physical thermometer polling, communication one second earlier,
four fresh channel responses and fresh 50% battery. Four fresh channel
responses do not mean four inserted probes; only two were available.

One operator-requested force reconnect finished with `operation succeeded`.
The configuration tool then reported desired connected, observed polling,
successful communication at zero seconds, four fresh channel responses and
fresh 50% battery. This is the first successful physical force reconnect on a
v1 candidate following failures on rc1 through rc3. It supports the rc4
registered-link release change but does not prove that it was the unique cause
or that recovery is reliable under all conditions.

A later authenticated support check still reported polling, successful
communication one second earlier, four fresh channel responses and fresh 50%
battery. A detailed REST check then reported a healthy physical heartbeat,
15-second stale threshold and sequence 269, with probes 1 and 2 present and
fresh at 20.0°C, probes 3 and 4 absent with null temperatures, and fresh 50%
battery. This confirms two inserted physical probes, not the four-inserted-probe
gate. The heartbeat session identifier was observed but is omitted from this
record because its exact value is not needed for acceptance.

Long-duration communication after reconnect, recovery during backoff,
restart/session changes, MQTT/Last Will, four-inserted-probe display comparison
and four-hour monitored soak remain pending on this candidate.

The operator then selected Disconnect in the guided iGrill management menu;
the command returned PASS. Authenticated REST confirmed desired and observed
states both `disconnected`, heartbeat `disconnected`, no connected adapter,
zero polling tasks and zero recovery tasks. This passes the explicit-disconnect
and recovery-cancellation observation.

An intentional ordinary Connect from the guided menu then returned FAIL.
Authenticated runtime status showed desired connected, observed backoff,
no connected adapter or polling task, one automatic recovery task, and
`device_operation_failed` at `connect_initialise` with `AdapterError` detail
`BLE connection and GATT service resolution timed out`. Thus rc4 passes a
single force-reconnect attempt but does not pass the explicit disconnect then
ordinary Connect sequence. The candidate remains physically unaccepted.

A later authenticated support check still showed backoff with automatic
recovery active, stale communication last successful 624 seconds earlier,
zero fresh probe readings and no fresh battery. The protected upgrade backup
`backup-1lranZJ3` pointed to the previously verified v0.9.0 release. The
operator rolled back using that exact backup; rollback created safety backup
`backup-6RSdUT76`. Follow-up checks confirmed active service, runtime v0.9.0,
healthy local `/health`, connected polling, fresh probes 1 and 2 at 20.0°C,
absent probes 3 and 4, and fresh 50% battery. No further rc4 attempt should
be inferred from this partial test.
