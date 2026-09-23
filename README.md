# pitblu-core

Native Raspberry Pi hardware gateway for Weber iGrill V202 thermometers. Provides
REST administration, SSE events and optional MQTT telemetry. This component is
independent of the future web frontend and contains no cook-history database or UI.

Source lives in the public `pitblu-project/pitblu-core` repository.
Run installation, development and build commands from the repository root.
The published release is 0.9.0. The 1.0.0rc3 candidate contains the guided tools
and thermometer heartbeat. Its four-probe physical suite and minimum four-hour
soak remain pending.

Start with the repository's [guided terminal tools](docs/terminal-tools.md).
See the documentation index for installation, security, API/MQTT
integration, migration and physical acceptance instructions. Those documents are
maintained in this repository and are outside the Python distribution.
