# Documentation index

## Version and scope

The current release is v1.0.0. Start with [installation](installation.md) or
the [quick start](bbq-quick-start.md). Some physical checks were waived at
publication; the [release status](release-status.md) explains the limits.
Git tags and releases identify published versions.

## For cooks

- [Plain-English overview](bbq-overview.md)
- [Quick start](bbq-quick-start.md)

## Setup and operation

- [Installation](installation.md): the step-by-step path for a new Pi or upgrade
- [Guided terminal tools](terminal-tools.md): setup and support command reference
- [Fresh-OS rebuild checklist](rebuild-checklist.md)
- [Backup, upgrade, rollback and uninstall](upgrade-and-rollback.md)
- [Troubleshooting](troubleshooting.md)
- [Controlled migration](rename-migration.md) from an older service identity

## Frontend builders and contributors

- [Complete frontend/AI handoff](frontend-integration.md): all endpoints, settings,
  SSE/MQTT schemas, examples, workflows and implementation limitations.
- [pitblu-app repository](https://github.com/pitblu-project/pitblu-app) for Cook-aware APIs
- [REST](api.md), [SSE](sse.md), [MQTT](mqtt.md), [configuration](configuration.md)
- [Thermometer communication heartbeat](thermometer-heartbeat.md)
- [Architecture](architecture.md), [Bluetooth protocol](bluetooth.md)
- [Development](development.md), [contributing](../CONTRIBUTING.md)

## Release assurance

- [v1.0.0 release notes](v1.0.0-release-notes.md) and [release status](release-status.md)
- [Physical acceptance checklist](physical-acceptance.md)
- [Pi and iGrill test evidence](physical-evidence.md)
- [Security policy and operating limits](../SECURITY.md)
- [Dated dependency audit](dependency-audit.md)
- [Changelog](../CHANGELOG.md), v0.9.0 onward
- [Provenance](provenance.md), [third-party notices](../THIRD_PARTY_NOTICES.md), [licence](../LICENSE)
- Decisions: [hardware-first](adr/0001-incremental-hardware-first.md),
  [adapter boundary](adr/0002-device-adapter-boundary.md),
  [REST/configuration/authentication](adr/0003-rest-configuration-and-auth.md) and
  [guided terminal boundaries](adr/0004-guided-terminal-tools.md), and
  [thermometer heartbeat](adr/0008-thermometer-heartbeat.md)

## Maintenance policy

Maintain one current installation path and integration contract. Keep historical
test details only where they explain a current limitation or provide provenance;
Git history retains superseded plans. Active guides target v1.0.0.

Update affected guides alongside code changes. Verify relative links and examples,
state the release baseline, and distinguish implemented functionality, limitations
and pending acceptance. Never rewrite old evidence to imply newer code was tested.
Keep credentials and private deployment details out of examples. Beginner guides
must stay accurate without requiring readers to understand the technical reference.
