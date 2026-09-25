# v1.0.0 release status

v1.0.0 is the published release. The release owner chose to publish it before
every physical acceptance check was complete. **Waived does not mean passed.**

Physical testing before publication showed four probes matching the iGrill
display, successful reconnection and recovery, live REST/SSE/MQTT readings,
and a twelve-hour monitored run with no recorded errors. The tested gateway
implementation is unchanged in v1.0.0, but the published package had not
itself been installed and checked on the Pi at publication. See the
[Pi test record](physical-evidence.md) for what was actually observed.

Still unverified: heartbeat ageing while the Bluetooth link remains connected
but stops responding, and several items without recorded physical results,
including fresh registration, invalid-value handling, token rotation and a
clean install/rollback of the published package. Supported-Python CI passed,
but software tests cannot establish those physical results. The
[acceptance checklist](physical-acceptance.md) tracks these limits.

During a cook, keep checking the iGrill independently. This gateway does not
provide cooking alarms or food-safety decisions.
