from pyinfra.operations import files, server, systemd

# systemd.service(
#     name="Stop nomad service before configuration",
#     service="nomad",
#     running=False,
#     _sudo=True,
# )

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
    restarted=True,
    _sudo=True,
)