# v1.0.0rc5 partial Raspberry Pi evidence

Operator-reported checks against canonical tag `v1.0.0rc5`, commit
`2ad2aa5d133117c137a1005572d6221f6616102b`. This is partial physical
evidence, not final v1.0.0 acceptance.

On 23 September 2026, the tag was cloned into a separate Pi checkout and the
guided prerequisite check passed on Debian 13/aarch64 with Python 3.13 and a
powered Bluetooth controller. The operator reported completing the guided
upgrade. An authenticated support check confirmed active service, healthy
local API and readiness, runtime v1.0.0rc5, the registered physical thermometer
polling, communication two seconds earlier, four fresh channel responses and
fresh 50% battery. MQTT was disabled. Four fresh channel responses are not
proof of four inserted probes; only two are available.

The operator selected Disconnect in the guided iGrill menu and received PASS.
Authenticated REST confirmed desired and observed states `disconnected`,
heartbeat `disconnected`, no connected adapter, zero polling tasks and zero
recovery tasks. The operator then selected ordinary Connect and received PASS.
After at least one minute, another authenticated support check reported desired
connected, observed polling, communication three seconds earlier, four fresh
channel responses and fresh 50% battery. This is a successful targeted
Disconnect → ordinary Connect retest of the sequence that failed on rc4.

The longer connection deadline and cached-candidate invalidation are both
present in rc5; the physical result does not isolate which change mattered.
Connected-but-unresponsive ageing, four-inserted-probe display comparison and
four-hour monitored soak remain pending on this candidate.

The operator then powered the thermometer off while leaving the Pi and service
running. After at least 20 seconds, the authenticated support check showed
desired connected, observed backoff, stale communication last successful 38
seconds earlier, automatic recovery active, zero fresh probe readings and no
fresh battery. The operator powered the thermometer on without forcing a
reconnect. After about one minute, the support check returned to polling with
communication at zero seconds, four fresh channel responses and fresh 40%
battery. This passes a targeted loss-and-automatic-recovery observation. It
does not yet test force reconnect during backoff or a connected-but-unresponsive
link. The protected upgrade backup `backup-75tJsb6g` was verified to point to
the previously accepted v0.9.0 release before this interruption.

Before a controlled service restart, authenticated REST showed healthy
heartbeat session `2df63310…` at sequence 710. The operator restarted only
`pitblu-core`; the command produced no output. The following support check
reported active service, ready local API, registered thermometer polling,
communication one second earlier, four fresh channel responses and fresh 40%
battery. A second authenticated REST check showed healthy heartbeat in a
different session, `d5751451…`, at sequence 20. This passes the targeted
restart/session-change and post-restart recovery observation.

A later authenticated REST baseline reported healthy, fresh, physical
heartbeat; probes 1 and 2 present and fresh at 20.0°C and 21.0°C; probes 3
and 4 absent with null temperatures; and fresh 40% battery. In a timed
operator-assisted test, probe 2 was unplugged and REST reported it absent
after 12.5 seconds, still fresh, with null temperature. This passes the
under-15-second probe-removal check on rc5. Probe 2 was left unplugged for
the following no-probe test.

With both available probes unplugged and the thermometer still powered on,
authenticated REST reported observed polling and a healthy, fresh, physical
heartbeat. All four probe channels were fresh, absent and null. This passes
the no-probe communication observation on rc5: valid absent-probe responses
continue to advance the thermometer heartbeat.

After reinserting probes 1 and 2, authenticated REST again reported polling
with a healthy heartbeat. Probes 1 and 2 were present and fresh at 20.0°C
and 21.0°C; probes 3 and 4 remained fresh, absent and null. This confirms
normal physical telemetry returned without a reconnect.

A read-only live SSE subscription returned HTTP 200 with `text/event-stream`
and a `thermometer.heartbeat` event sourced from `physical`. The confirmed
event had sequence 120 in the post-restart session `d5751451…`, with heartbeat
status `healthy` and `fresh: true`. The first operator script received an SSE
event but raised `KeyError` because it incorrectly expected `sessionId` inside
event data rather than at the event's top level; the corrected script produced
the values above. This passes the live SSE heartbeat representation check.

For the force-reconnect-in-backoff gate, the operator powered the thermometer
off again while leaving the service running. A later authenticated support
check showed desired connected, observed backoff, stale communication last
successful 197 seconds earlier, automatic recovery active, zero fresh probe
readings and no fresh battery. The operator powered the thermometer on and
immediately requested Force Reconnect. The CLI explicitly stated that
automatic recovery was active and this request forced an immediate attempt.
The asynchronous operation succeeded, returning to observed polling with
communication at zero seconds, four fresh channel responses and fresh 40%
battery. This passes a targeted successful force reconnect while in backoff.
A support check after at least one further minute still reported observed
polling, communication one second earlier, four fresh channel responses and
fresh 40% battery.

The local Mosquitto broker was active and rejected an unauthenticated
subscriber, as expected for an authenticated broker. Its configuration had
both a password file and ACL file; the ACL had three user entries and two
read rules. The operator used saved credentials through the guided MQTT tool.
An initial configuration with the wrong account entered MQTT backoff; after
correcting it to the existing `pitblu-publisher` account and entering its
password at the hidden prompt, the guided restart reported MQTT connected.
The authenticated support check then confirmed MQTT connected, readiness and
physical thermometer polling with recent communication and fresh 40% battery.

A separate subscriber connected using credentials entered only at hidden
prompts and received granted QoS 1 subscriptions for service availability
and device heartbeat. Both messages were retained, delivered at QoS 1 and
sourced from `physical`. Service availability was true, device heartbeat was
healthy, and both shared the same publisher session identifier. No subscriber
credential or secret was included in the test output or this record. This
passes the retained MQTT availability/heartbeat representation check, but
does not yet prove live temperature delivery or Last Will behaviour.

The separate subscriber then received a granted QoS 1 subscription to live
probe-temperature topics. A probe 1 message reported 20.0°C, source
`physical`, QoS 1 and `retained: false`, in the same publisher session as
the retained availability and heartbeat observations. This passes the live
MQTT temperature-delivery check. Last Will was tested next.

With no active cook, the operator ran a separate authenticated subscriber for
retained service availability, then sent SIGKILL only to the `pitblu-core`
service main process with `systemctl kill --kill-who=main`. The service was
configured `Restart=on-failure` with a five-second restart delay. The
subscriber observed `available=true` retained at QoS 1 in session
`b69a41d01aaa4d7396ab04401cdd4798`, then a live QoS 1
`available=false` publication from that same session (the broker Last Will),
then live QoS 1 `available=true` in new session
`9201688ee13e427dbb387c22b8b6ca9b`. This passes the MQTT Last Will and
publisher-session transition check. The observer subsequently raised a
`UnicodeEncodeError` solely while printing a non-ASCII completion message;
all three broker messages had already been received and printed. The
post-restart authenticated support check passed: service active, local API
healthy, readiness ready, runtime `1.0.0rc5` status okay, MQTT connected,
physical iGrill polling with communication two seconds earlier, four fresh
channel responses and fresh 40% battery. This completes the targeted
service-failure/Last Will/recovery check; it does not substitute for the
four-hour soak or four-inserted-probe comparison.
