from pyinfra import local
from pyinfra.operations import files, systemd

local.include('provision/tasks/nomad_common.py')

files.directory(
    name="Create Waypoint server volume directory",
    path="/home/vagrant/nomad/volumes/waypoint_server",
    present=True,
    _sudo=True
)

files.directory(
    name="Create Waypoint runner volume directory",
    path="/home/vagrant/nomad/volumes/waypoint_runner",
    present=True,
    _sudo=True
)

files.put(
    name="Put nomad config file",
    src="nomad-client/nomad.hcl",
    dest="/etc/nomad.d/nomad.hcl",
    _sudo=True
)

systemd.service(
    name="Enable nomad service",
    service="nomad",
    running=True,
    enabled=True,
    _sudo=True,
)