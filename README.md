# pitblu-core

Native Raspberry Pi hardware gateway for Weber iGrill V202 thermometers. Provides
REST administration, SSE events and optional MQTT telemetry. This component is
separate from the web application and contains no cook-history database or UI.

Source lives in the public `pitblu-project/pitblu-core` repository.
Run installation, development and build commands from the repository root.
The current release is v1.0.0. Start with the
[Raspberry Pi installation guide](docs/installation.md), then use
`pitblu-core-config check` to verify physical readings. The
[release status](docs/release-status.md) explains checks that were waived at
publication.

The [documentation index](docs/README.md) points to everyday use, setup,
troubleshooting and developer references. Documentation is maintained in this
repository and is not bundled into the Python package.
