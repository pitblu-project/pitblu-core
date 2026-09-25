# Documentation index

## Version and scope

The current release is v1.0.0. The rc5 four-probe display comparison and
twelve-hour soak passed, but the owner waived the remaining physical gates for
publication; they are not claimed as passed. See [release status](release-status.md).
`CHANGELOG.md` is the canonical human-readable version history; Git tags and
releases are authoritative once published.

## For cooks

- [Plain-English overview](bbq-overview.md)
- [Quick start](bbq-quick-start.md)

## Setup and operation

- [Guided terminal tools](terminal-tools.md): normal install, configuration and support workflow
- [Installation](installation.md)
- [Fresh-OS rebuild checklist](rebuild-checklist.md)
- [Backup, upgrade, rollback and uninstall](upgrade-and-rollback.md)
- [Troubleshooting](troubleshooting.md)

## Frontend builders and contributors

- [Complete frontend/AI handoff](frontend-integration.md): all endpoints, settings,
  SSE/MQTT schemas, examples, workflows and implementation limitations.
- [pitblu-app repository](https://github.com/pitblu-project/pitblu-app) for Cook-aware APIs
- [REST](api.md), [configuration](configuration.md), [MQTT](mqtt.md)
- [Thermometer communication heartbeat](thermometer-heartbeat.md)
- [Architecture](architecture.md), [Bluetooth protocol](bluetooth.md)
- [Development](development.md), [contributing](../CONTRIBUTING.md)

## Release assurance

- [v1.0.0 release notes](v1.0.0-release-notes.md) and [release status](release-status.md)
- [Physical acceptance checklist](physical-acceptance.md)
- [v1.0.0rc1 partial Pi evidence](physical-candidate-rc1.md)
- [v1.0.0rc2 partial Pi evidence](physical-candidate-rc2.md)
- [v1.0.0rc3 partial Pi evidence](physical-candidate-rc3.md)
- [v1.0.0rc4 partial Pi evidence](physical-candidate-rc4.md)
- [v1.0.0rc5 partial Pi evidence](physical-candidate-rc5.md)
- [Security policy](../SECURITY.md) and [historical v0.9.0 security review](security-review.md)
- [Dependency audit](dependency-audit.md) and [clean-Pi procedure](clean-pi-acceptance.md)
- [Changelog](../CHANGELOG.md), v0.9.0 onward
- [Provenance](provenance.md), [third-party notices](../THIRD_PARTY_NOTICES.md), [licence](../LICENSE)
- Decisions: [hardware-first](adr/0001-incremental-hardware-first.md),
  [adapter boundary](adr/0002-device-adapter-boundary.md),
  [REST/configuration/authentication](adr/0003-rest-configuration-and-auth.md) and
  [guided terminal boundaries](adr/0004-guided-terminal-tools.md), and
  [thermometer heartbeat](adr/0008-thermometer-heartbeat.md)

## Maintenance policy

Maintain one current installation path and integration contract. Remove superseded
plans and obsolete command sequences from active documentation; Git history retains
them. Active documentation targets v1.0.0. Preserve relevant licence/provenance
and architectural rationale without obsolete milestone instructions.

Update affected guides alongside code changes. Verify relative links and examples,
state the release baseline, and distinguish implemented functionality, limitations
and pending acceptance. Never rewrite old evidence to imply newer code was tested.
Keep credentials and private deployment details out of examples. Beginner guides
must stay accurate without requiring readers to understand the technical reference.
