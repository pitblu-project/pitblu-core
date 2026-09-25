# Security policy

## Supported deployment

The published v1.0.0 release is intended for loopback or an explicitly trusted
LAN. Do not expose HTTP or the MQTT broker directly to the internet. There is
no built-in HTTPS, end-user account system or safety alarm. Use host and network
controls; API rate and body limits do not cover every resource or failure mode.

The administrator token grants full control. Keep it in a password manager or
trusted backend. The database and backups contain protected device identity and
may contain MQTT credentials; handle them as secrets.

## Operating limits

- The bearer-token holder is an administrator. Keep the token server-side in
  browser integrations. Token rotation invalidates future requests but does
  not close an already-admitted [SSE stream](docs/sse.md); close existing
  streams when rotating it. Only `/health` is unconditionally public when
  authentication is enabled.
- Treat Bluetooth advertisements and client input as untrusted. A powered
  controller, healthy process or successful readiness check does not prove
  fresh physical readings. Check device heartbeat, freshness and probe source
  before relying on telemetry. The gateway is not a safety alarm.
- Retained [MQTT](docs/mqtt.md) values can outlive a device registration, and
  [SSE](docs/sse.md) has no replay. Reconcile with authenticated REST after a
  gap; check timestamps, availability and session identity when consuming
  telemetry. Last Will timestamps reflect when the message was prepared.
- Configuration changes require a service restart. Avoid restarts and upgrades
  during an active cook. The installer executes trusted source and package
  builds as root; use reviewed release source, not arbitrary archives or
  user-supplied backup paths. Backups support controlled rollback on the same
  host, not automatic disaster recovery.
- Keep the Pi and its dependencies patched. Process supervision, rate limits
  and physical testing do not guarantee continuous readings; use an
  independent thermometer where safety matters.

## Reporting

Report suspected security problems privately to the repository maintainer through
an existing private project channel. Provide the affected version, a sanitised
reproduction and expected versus actual behaviour. Do not post credentials,
private addresses or database backups in public issues.

Review the dated [dependency audit](docs/dependency-audit.md) alongside current
CI results; its old resolved-version table is not a current security scan.
