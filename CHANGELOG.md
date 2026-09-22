# Changelog

This file is the canonical human-readable version history. Git tags and GitHub
releases identify published revisions.

## [1.0.0rc1] - candidate

- Added guided `pitblu-core-install` and `pitblu-core-config` terminal workflows.
- Added validated thermometer communication heartbeat to REST, SSE and MQTT, with
  manual force reconnect through the existing REST operation.
- Updated dependencies and restored standalone CI and documentation ownership.
- Changed the pending v1.0.0 physical soak requirement from 16 hours to four hours.

This candidate has automated validation. Real Pi/iGrill heartbeat, four-probe,
recovery and four-hour soak acceptance remain pending. It is not a final release.

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
