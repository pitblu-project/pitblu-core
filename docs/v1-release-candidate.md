# v1.0.0 release candidate and physical acceptance plan

## Candidate identity

The package and API version are `1.0.0rc1`. Record the full reviewed Git commit
and tag used for installation before running any Pi checks. The candidate source
comes from the standalone `pitblu-project/pitblu-core` repository. The historical
monorepo checkout is not a deployment source.

The Python 3.11, 3.12 and 3.13 CI matrix, wheel installation and Bash syntax
check must pass on that exact revision. Automated tests establish software
behaviour; they do not establish physical acceptance.

## Pi sequence

Schedule work outside an active cook. Preserve the existing installation and
backups. On the Pi, fetch the reviewed standalone revision into a separate checkout
and verify the full commit, clean tree, Python, OS and active service state. Use
`./pitblu-core-install check` before upgrade. The guided installer must detect
the existing managed installation and use its upgrade path. Keep the previous
release available for rollback.

After upgrade, run `pitblu-core-config check` and verify local health, authenticated
readiness, version, registered device, heartbeat, probes and battery. The token is
entered only through the tool's hidden TTY prompt. Record results without secrets
or Bluetooth addresses.

Run the physical checks in [the acceptance checklist](physical-acceptance.md):
all four inserted probes against the display, probe removal within 15 seconds,
no-probe communication, connected but unresponsive ageing, recovery and backoff,
force reconnect, explicit disconnect, restart session change, REST/SSE/MQTT
heartbeat representation, broker Last Will and rollback. An accepted asynchronous
reconnect operation is not proof of success; wait for its terminal result.

Complete at least four hours of monitored physical operation without manual
intervention. Record timestamps, fresh sample cadence, MQTT receipt, gaps,
interruptions and recovery. Review each gap. Keep the resulting evidence tied to
the exact candidate commit and physical environment.

## Final release decision

Keep any failed or unrun gate pending. If code changes are needed after physical
testing, build a new candidate and repeat affected checks on its exact revision.
Only after the final candidate passes CI, review and all physical gates should
`1.0.0` be merged, tagged, published and smoke-tested on the Pi.
