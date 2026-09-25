# Install pitblu-core v1.0.0 on a Raspberry Pi

This guide is for Raspberry Pi OS/Debian 13 (Trixie), 64-bit ARM, with Python
3.13, systemd and a powered Bluetooth controller. Use the Pi terminal or an
interactive SSH session. Do not install or upgrade during a cook.

If pitblu-core is **already installed**, use [Upgrade an existing installation](#upgrade-an-existing-installation)
below. If a different gateway or service is installed, read
[migration](rename-migration.md) first. Do not run two gateways against the
same iGrill.

## Get the v1.0.0 source

If Git is not installed, install it first:

```bash
sudo apt-get update
sudo apt-get install git
```

Then get the published version in a new directory:

```bash
git clone --branch v1.0.0 --depth 1 https://github.com/pitblu-project/pitblu-core.git pitblu-core-v1.0.0
cd pitblu-core-v1.0.0
git rev-parse HEAD
./pitblu-core-install check
```

The check reports supported hardware, Python, required packages and Bluetooth
state without changing the installation. If the directory already exists,
choose another empty directory rather than overwriting it. A detached Git
checkout of a release tag is normal.

## New installation

After the prerequisite check succeeds, run:

```bash
./pitblu-core-install install
```

Read each prompt. The installer explains any missing packages and asks before
installing them. It then asks for `sudo` only for the system changes it needs.
Allow it to enable and start the service if you want it to run now and after
reboot. It checks service state, installed version, local health and Bluetooth
when finished.

The administrator token appears **once**. Save it in a password manager at
that moment. Do not paste it into chat, a command, a screenshot or a log.
Do not delete the database to recover a lost token; use a planned local
recovery procedure.

The installer may offer to open guided configuration. Choose Yes, or run this
later:

```bash
pitblu-core-config igrill
```

Turn on the iGrill, choose it from the scan, register it and connect. The
service does not automatically connect to a nearby, unregistered device.
MQTT is optional and starts disabled. If you want it, first set up an
authenticated broker, then use `pitblu-core-config mqtt`. The gateway
installer does not install or configure Mosquitto.

## Upgrade an existing installation

Use a fresh v1.0.0 checkout following the source steps above.
Check the host and keep the existing protected backup. Then run:

```bash
./pitblu-core-install upgrade
```

The upgrade makes a protected backup before switching releases. Review the
post-install checks and use [backup and rollback](upgrade-and-rollback.md) if
the service or physical readings do not recover. Do not discard an older
working release or backup until the new installation is verified.

## Verify readings

Run the guided support check:

```bash
pitblu-core-config check
```

Enter the administrator token at the hidden prompt. Look for version
`1.0.0`, an active service, healthy local API, a connected/polling iGrill,
recent communication and fresh **physical** probe readings. Compare the
temperatures with the iGrill display. A healthy API alone does not prove
Bluetooth readings are reaching the Pi. A socket with no probe inserted
should be shown as absent, not as a live temperature.

If the check reports a failure, follow [troubleshooting](troubleshooting.md).
The [release status](release-status.md) describes physical checks that had not
been completed when v1.0.0 was published. Continue independent temperature
checks during a cook.

## What the installer changes

The guided installer creates a dedicated `pitblu-core` service account,
a versioned Python environment under `/opt/pitblu-core/releases`, a protected
SQLite database under `/var/lib/pitblu-core`, configuration under
`/etc/pitblu-core`, and a systemd service. It uses a deployment lock and
retains backups in `/var/backups/pitblu-core`. Source and configuration are
root-owned; the service runs without root privileges. Package-index access is
required, but Docker is not.

The default API listens only on `127.0.0.1:8080` with token authentication.
Only use a network-facing bind address on a trusted LAN with appropriate
controls. Never expose the API or an unauthenticated MQTT broker directly to
the internet. No automatic software upgrades or firewall changes are made.

For normal setup and diagnostic options, see [guided terminal tools](terminal-tools.md).
For expert backup, rollback and uninstall operations, see
[backup and rollback](upgrade-and-rollback.md). Existing databases are not
imported automatically when moving from a differently named deployment.
