locals {
  port = 80
}

job "sample-app" {
  datacenters = ["dc1"]
  group "app" {
    count = 2

    network {
      port "http" {
        to = local.port
      }
    }

    service {
      name     = "sample-app"
      port     = "http"
      provider = "nomad"
      tags = [
        "traefik.enable=true",
        "traefik.http.routers.sample.entrypoints=web, websecure",
        "traefik.http.routers.sample.rule=Host(`sample.nomad.localhost`)",
      ]
    }

    task "app" {

      driver = "docker"

      config {
        image = "${artifact.image}:${artifact.tag}"
        ports = ["http"]
      }

      env {
        %{ for k, v in entrypoint.env~}
        ${ k } = "${v}"
        %{ endfor~}

        PORT = local.port
        # ALLOC_ID = NOMAD_SHORT_ALLOC_ID
      }
    }
  }
}