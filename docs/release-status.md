# v1.0.0 release status

v1.0.0 is published at the release owner's direction. Publication is **not** a
claim that every item in the [physical acceptance checklist](physical-acceptance.md)
passed. The owner explicitly waived the remaining gates for this release.

The final candidate was `v1.0.0rc5` at commit
`2ad2aa5d133117c137a1005572d6221f6616102b`. The runtime implementation on
the release branch is unchanged from that tag; stable-release preparation updates
version metadata, the soak script's version assertion, and documentation. The
stable package itself had not been installed on the Pi when publication was
requested. Do not carry candidate hardware results forward as a stable-tag smoke
test.

The [rc5 operator record](physical-candidate-rc5.md) reports physical Disconnect
then Connect, force reconnect, automatic recovery, four inserted probes matching
the iGrill display, fresh REST/SSE/MQTT telemetry, retained MQTT state and Last
Will, and recovery across service/broker/Bluetooth/Pi restarts. Its twelve-hour
soak completed 43,200 seconds, 7,094 good REST samples, 23,904 probe-temperature
MQTT messages, no reported anomalies or session changes, and an 11.8-second
maximum MQTT gap.

The timed power-off exercise showed disconnection before heartbeat staleness; it
did **not** exercise a connected-but-unresponsive link. That ageing case remains
unproved. Other checklist items without recorded final-candidate evidence,
including fresh registration, invalid-value handling, token rotation and a clean
install/rollback of the stable tag, remain unverified rather than passed. Automated
CI can validate code and packaging but cannot close physical evidence gaps.

Earlier candidate failures and rollbacks remain in the rc1–rc4 records. The
[v0.9.0 clean-Pi record](clean-pi-acceptance.md) is a historical baseline, not
validation of v1.0.0. The web/Cook application is a separate project.
