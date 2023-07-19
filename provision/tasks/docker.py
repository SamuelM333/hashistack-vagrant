from pyinfra.operations import systemd
from pyinfra_docker import deploy_docker

deploy_docker(_sudo=True)

systemd.service(
    name="Enable docker service",
    service="docker",
    running=True,
    enabled=True,
    restarted=True,
    _sudo=True,
)