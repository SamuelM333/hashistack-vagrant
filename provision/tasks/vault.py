from pyinfra.operations import files, server, systemd

files.directory(
    name="Create Vault data dir",
    path="/home/vagrant/vault/data",
    present=True,
)

files.directory(
    name="Create Vault config dir",
    path="/etc/vault.d",
    present=True,
    _sudo=True
)

systemd.service(
    name="Stop vault service before configuration",
    service="vault",
    running=False,
    _sudo=True,
)

files.put(
    name="Put vault config file",
    src="vault-server/vault.hcl",
    dest="/etc/vault.d/vault.hcl",
    _sudo=True
)

files.file(
    name="Delete default vault service file",
    path="/usr/lib/systemd/system/vault.service",
    present=False,
    force=True,
    _sudo=True,
)

files.put(
    name="Put vault service file",
    src="vault-server/vault.service",
    dest="/etc/systemd/system/vault.service",
    _sudo=True
)

# server.service(
#     name="Enable vault service",
#     service="vault",
#     enabled=True,
#     running=True,
#     _sudo=True
# )

systemd.service(
    name="Enable vault service",
    service="vault",
    running=True,
    enabled=True,
    restarted=True,
    _sudo=True,
)