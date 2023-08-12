from pyinfra import host
from pyinfra.facts.server import LinuxName
from pyinfra.operations import dnf, server

if host.get_fact(LinuxName) in ('Rocky Linux', ):
    dnf.repo(
        name="Add the hashicorp repo",
        src="https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo",
        _sudo=True,
    )

server.packages(
    name="Install OS dependencies",
    packages=[
        "nomad",
        "consul",
        "vault",
        "waypoint",
        "bind-utils",
        "traceroute",
        "tcpdump",
        "net-tools"
    ],
    _sudo=True,
)
