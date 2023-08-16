job "whoami" {
  datacenters = ["dc1"]

  type = "system"

  group "demo" {
    network {
       port "http" {
         to = 80
       }
    }

    service {
      name = "whoami"
      port = "http"
      provider = "nomad"

      tags = [
        "traefik.enable=true",
        "traefik.http.routers.whoami.entrypoints=web, websecure",
        "traefik.http.routers.whoami.rule=Host(`whoami.nomad.localhost`)",
      ]
    }

    task "server" {
      env {
        WHOAMI_PORT_NUMBER = "${NOMAD_PORT_http}"
      }

      driver = "docker"

      config {
        image = "traefik/whoami"
        ports = ["http"]
      }

      resources {
        cpu    = 10
        memory = 16
      }

    }
  }
}