# Changelog

Git tags and GitHub releases identify the published versions. This file
summarises changes that matter to users.

## [1.0.0] - 2026-09-25

- Added guided `pitblu-core-install` and `pitblu-core-config` commands for
  installation, setup and support checks.
- Added a thermometer communication heartbeat to REST, SSE and MQTT, plus an
  operator-requested force reconnect.
- Improved reconnection by refreshing device discovery, releasing leftover
  BlueZ connections and allowing more time for BLE connection and GATT
  service resolution. Diagnostics report safe failure details without
  exposing device identity or credentials.
- Physical testing showed four probes matching the iGrill display, successful
  targeted recovery and a twelve-hour monitored run without recorded errors.

The owner published v1.0.0 with some physical checks waived, not passed. The
published package had not itself been smoke-tested on the Pi at publication.
See [release status](docs/release-status.md) and the
[Pi test record](docs/physical-evidence.md).

## [0.9.0] - 2026-09-10

- Added the native Raspberry Pi gateway with REST administration, SSE events
  and optional MQTT telemetry for Weber iGrill V202 thermometers.
- Added explicit device registration, physical and simulated adapters, four
  logical probe channels and automatic recovery.
- Added bearer authentication and rotation, typed configuration, write-only
  secrets, a hardened systemd service, protected backups, upgrade, rollback
  and non-destructive uninstall.
- Passed the historical clean-Pi checks at commit
  `f3bc11488e72b966676c0f3a1844ea218259ab90fd`, including two physical
  probes, SSE, MQTT and reboot recovery. This is historical evidence, not
  v1.0.0 acceptance.
