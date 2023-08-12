from pyinfra import local
from pyinfra.operations import files, systemd

local.include('provision/tasks/consul_common.py')

files.put(
    name="Put consul config file",
    src="shared/consul-client.hcl",
    dest="/etc/consul.d/consul.hcl",
    _sudo=True
)

systemd.daemon_reload(_sudo=True)

systemd.service(
    name="Enable consul service",
    service="consul",
    running=True,
    enabled=True,
    _sudo=True,
)