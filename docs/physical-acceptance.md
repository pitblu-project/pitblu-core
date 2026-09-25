# Physical acceptance checklist

v1.0.0 was published with some checks still unverified. The release owner
waived them for publication; no unrun check is recorded as a pass. The
[Pi test record](physical-evidence.md) gives the observed results and exact
test build. The published package still needs its own Pi smoke test.

| Check | Evidence at publication |
| --- | --- |
| Four inserted probes match the iGrill display | Passed on the tested build; all four matched exactly. |
| Probe removal and no-probe communication | Passed on the tested build; removal observed after 12.5 seconds. |
| Disconnect/Connect, force reconnect and power-cycle recovery | Passed in targeted physical checks. |
| REST, SSE, MQTT temperatures, retained state and Last Will | Passed in targeted checks with an authenticated subscriber. |
| Service, broker, Bluetooth-service and Pi restart recovery | Passed in targeted checks. |
| Twelve-hour physical monitoring | Passed on the tested build; 7,094 good REST samples and 23,904 temperature messages, with no recorded errors. |
| Heartbeat ageing while Bluetooth stays connected but stops responding | Not demonstrated. The link disconnected before the heartbeat became stale. |
| Fresh registration, invalid-value rejection and token rotation on the final build | No complete physical result recorded. |
| Clean installation, upgrade and rollback of the published v1.0.0 package | Not yet recorded on the Pi. |

## If you run further checks

Schedule disruptive checks outside an active cook. Close other apps connected to
the iGrill and run only one gateway. Record the exact Git revision, Pi OS and
Python version, what you did, what the iGrill displayed and what the gateway
reported. Keep passwords, Bluetooth addresses, private network details and
raw databases out of shared logs. A healthy service alone does not prove that
physical readings are current. Continue independent temperature checks.
