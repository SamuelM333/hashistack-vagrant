from pyinfra.operations import files, systemd

systemd.service(
    name="Stop nomad service before configuration",
    service="nomad",
    running=False,
    _sudo=True,
)

files.file(
    name="Delete default nomad service file",
    path="/usr/lib/systemd/system/nomad.service",
    present=False,
    force=True,
    _sudo=True,
)

files.put(
    name="Put nomad service file",
    src="shared/nomad.service",
    dest="/etc/systemd/system/nomad.service",
    _sudo=True
)

files.put(
    name="Put nomad common file",
    src="shared/nomad-common.hcl",
    dest="/etc/nomad.d/nomad-common.hcl",
    _sudo=True
)

systemd.service(
    name="Enable nomad service",
    service="nomad",
    running=True,
    enabled=True,
    _sudo=True,
)