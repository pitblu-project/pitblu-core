# v0.9.0 release status

The v1.0.0 thermometer-heartbeat workstream does not change the v0.9.0 tag or historical
acceptance. Real Pi/iGrill heartbeat, four-probe and soak gates remain pending until explicitly
executed against the final candidate.

The v0.9.0 beta source is prepared from the runtime accepted as v0.9.0rc1 at exact
commit `f3bc11488e72b966676c0f3a1844ea218259ab90`. Release preparation changes only
metadata and documentation; gateway runtime code is unchanged from that physically
tested revision.

Clean-Pi installation, native security controls, REST onboarding, physical
two-probe comparison, battery cadence, SSE, MQTT, restart/reboot recovery, backup,
same-version upgrade/rollback and uninstall/restoration passed. The dated sanitised
results are in [clean-Pi acceptance](clean-pi-acceptance.md).

The original `v0.9.0` tag and release were published in the historical monorepo.
The standalone repository preserves the identical core source tree at `d5e407d`.
`CHANGELOG.md` is the canonical human-readable version history; Git tags and
releases are authoritative for published revisions.

The full four-probe physical suite and minimum four-hour soak are separate v1.0.0
gates and remain pending. The [frontend contract](frontend-integration.md) includes
the candidate heartbeat contract; pitblu-app is a separate application component.
