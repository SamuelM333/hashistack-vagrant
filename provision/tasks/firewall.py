from pyinfra.operations import server


server.service(
    name="Enable firewalld service",
    service="firewalld",
    enabled=True,
    running=True,
    _sudo=True,
)

server.shell(
    name="Open firewall ports",
    commands=[
        # Consul
        # https://www.consul.io/docs/install/ports
        "firewall-cmd --permanent --add-port=8500/tcp",
        "firewall-cmd --permanent --add-port=8600/udp",
        "firewall-cmd --permanent --add-port=8600/tcp",
        "firewall-cmd --permanent --add-port=8301/tcp",
        "firewall-cmd --permanent --add-port=8301/udp",
        "firewall-cmd --permanent --add-port=8302/tcp",
        "firewall-cmd --permanent --add-port=8302/udp",
        "firewall-cmd --permanent --add-port=8300/tcp",

        # Nomad
        # https://www.nomadproject.io/docs/install/production/requirements#ports-used
        "firewall-cmd --permanent --add-port=4646/tcp",
        "firewall-cmd --permanent --add-port=4647/tcp",
        "firewall-cmd --permanent --add-port=4648/tcp",
        "firewall-cmd --permanent --add-port=4648/udp",

        # Vault
        "firewall-cmd --permanent --add-port=8200/tcp",
        "firewall-cmd --permanent --add-port=8200/udp",
        "firewall-cmd --permanent --add-port=8201/tcp",
        "firewall-cmd --permanent --add-port=8201/udp",

        # Traefik
        "firewall-cmd --permanent --add-port=8080/tcp",
                
        # Waypoint
        "firewall-cmd --permanent --add-port=9701/tcp",
        "firewall-cmd --permanent --add-port=9702/tcp",
    ],
    _sudo=True,
)

server.shell(
    name="Reload firewall service",
    commands=["firewall-cmd --reload"],
    _sudo=True,
)