# Changelog

This file is the canonical human-readable version history. Git tags and GitHub
releases identify published revisions.

## [1.0.0rc4] - candidate

- Before manual or automatic reconnect of a registered thermometer, ask BlueZ to
  release a leftover connection for that exact identity after the Bleak client
  disconnects and before fresh discovery. No unpairing or adapter reset is used.

This targets the rc3 physical finding that reconnection repeatedly timed out
before GATT service resolution. It requires a new physical retest; no v1.0.0
acceptance gate is marked passed.

## [1.0.0rc3] - 2026-09-23 prerelease

- Report only whitelisted first-party adapter failure details to distinguish BLE
  connection timeout from individual authentication steps. Native library messages,
  Bluetooth addresses and credentials remain excluded.

The Pi retest identified repeated BLE connection and GATT service resolution
timeouts on force reconnect. The operator rolled back to the working v0.9.0
runtime; see the rc3 physical record. Do not treat a healthy process or automated
tests as acceptance.

## [1.0.0rc2] - 2026-09-23 prerelease

- Refresh the registered thermometer's BLE discovery before manual and automatic
  reconnect attempts, avoiding a stale BlueZ candidate after disconnection.
- Add a safe failure class to operation diagnostics and journal events; exception
  messages and native Bluetooth identity remain private.

Pi force reconnect still failed, followed by repeated `AdapterError` failures and
stale communication. The service was rolled back to the physically accepted v0.9.0
baseline. The failure detail was not available from this candidate.

## [1.0.0rc1] - 2026-09-22 prerelease

- Added guided `pitblu-core-install` and `pitblu-core-config` terminal workflows.
- Added validated thermometer communication heartbeat to REST, SSE and MQTT, with
  manual force reconnect through the existing REST operation.
- Updated dependencies and restored standalone CI and documentation ownership.
- Changed the pending v1.0.0 physical soak requirement from 16 hours to four hours.

Automated validation passed. Pi testing found healthy physical communication,
correct absent-probe handling and probe removal within 5.4 seconds, but repeated
manual reconnects failed during initialisation before automatic recovery restored
communication. The four-probe and four-hour soak gates were not completed.

## [0.9.0] - 2026-09-10

- Added the native Raspberry Pi gateway with REST administration, SSE events and
  optional MQTT telemetry for Weber iGrill V202 thermometers.
- Added explicit device registration, stable public identifiers, physical and
  simulated adapters, four logical probe channels and supervised recovery.
- Added bearer authentication and rotation, request and stream limits, typed
  versioned configuration, write-only secrets and safe diagnostics.
- Added hardened systemd deployment, protected backup, upgrade, rollback and
  non-destructive uninstall workflows.
- Passed clean-Pi acceptance on Raspberry Pi OS Lite 64-bit Trixie at commit
  `f3bc11488e72b966676c0f3a1844ea218259ab90`: 114 tests, 93.79% coverage,
  native installation/security checks, two-probe display comparison, battery,
  SSE, MQTT, restart/reboot recovery and maintenance workflows.

The accepted runtime was labelled `0.9.0rc1`. Final `0.9.0` preparation changed
release metadata and documentation only. The original historical release plan
called for a 16-hour v1.0.0 soak; the candidate entry above records its later
change to four hours.
