from pyinfra import local
from pyinfra.operations import files, systemd

local.include('provision/tasks/nomad_common.py')

files.put(
    name="Put nomad config file",
    src="nomad-server/nomad.hcl",
    dest="/etc/nomad.d/nomad.hcl",
    _sudo=True
)

systemd.daemon_reload(_sudo=True)

systemd.service(
    name="Enable nomad service",
    service="nomad",
    running=True,
    enabled=True,
    _sudo=True,
)
