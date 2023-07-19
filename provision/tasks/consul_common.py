from pyinfra.operations import files, server, systemd

systemd.service(
    name="Stop consul service before configuration",
    service="consul",
    running=False,
    _sudo=True,
)

files.file(
    name="Delete default consul service file",
    path="/usr/lib/systemd/system/consul.service",
    present=False,
    force=True,
    _sudo=True,
)

files.put(
    name="Put consul service file",
    src="shared/consul.service",
    dest="/etc/systemd/system/consul.service",
    _sudo=True
)

# server.service(
#     name="Enable consul service",
#     service="consul",
#     enabled=True,
#     running=True,
#     _sudo=True
# )

systemd.service(
    name="Enable consul service",
    service="consul",
    running=True,
    enabled=True,
    restarted=True,
    _sudo=True,
)