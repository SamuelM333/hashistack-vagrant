from pyinfra.operations import files, server, systemd

# systemd.service(
#     name="Stop consul service before configuration",
#     service="consul",
#     running=False,
#     _sudo=True,
# )

files.put(
    name="Put consul config file",
    src="consul-server/consul.hcl",
    dest="/etc/consul.d/consul.hcl",
    _sudo=True
)

systemd.service(
    name="Enable consul service",
    service="consul",
    running=True,
    enabled=True,
    restarted=True,
    _sudo=True,
)