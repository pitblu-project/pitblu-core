# Security policy

## Supported deployment

The published v0.9.0 release and v1.0.0rc1 candidate are intended for loopback
or an explicitly trusted LAN. Do not expose HTTP or the MQTT broker directly to
the internet. There is no built-in HTTPS, end-user account system or safety alarm.

The administrator token grants full control. Keep it in a password manager or
trusted backend. The database and backups contain protected device identity and
may contain MQTT credentials; handle them as secrets.

## Reporting

Report suspected security problems privately to the repository maintainer through
an existing private project channel. Provide the affected version, a sanitised
reproduction and expected versus actual behaviour. Do not post credentials,
private addresses or database backups in public issues.

The [security review](docs/security-review.md) records the v0.9.0 checks and
remaining limits. Apply OS security updates and review dependency audit results.
Avoid upgrades or restarts during an active cook.
