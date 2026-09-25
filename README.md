# pitblu-core

Native Raspberry Pi hardware gateway for Weber iGrill V202 thermometers. Provides
REST administration, SSE events and optional MQTT telemetry. This component is
independent of the future web frontend and contains no cook-history database or UI.

Source lives in the public `pitblu-project/pitblu-core` repository.
Run installation, development and build commands from the repository root.
The current release is v1.0.0, adding guided tools and a thermometer
communication heartbeat. The four-probe display comparison and twelve-hour
soak passed on rc5. The release owner waived the remaining physical acceptance
gates for publication; they are not recorded as passed. See the
[release status](docs/release-status.md) before deploying.

Start with the repository's [guided terminal tools](docs/terminal-tools.md).
See the documentation index for installation, security, API/MQTT
integration, migration and physical acceptance instructions. Those documents are
maintained in this repository and are outside the Python distribution.
