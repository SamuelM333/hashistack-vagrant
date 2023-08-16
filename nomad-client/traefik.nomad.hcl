job "traefik" {
  datacenters = ["dc1"]
  type        = "service"

  group "traefik" {
    count = 1

    network {
      port  "http"{
         static = 80
      }
      port  "https"{
         static = 443
      }
      port  "admin"{
         static = 8080
      }
    }

    service {
      name = "traefik-http"
      provider = "nomad"
      port = "admin"

        check {
          type     = "tcp"
          port     = "http"
          interval = "10s"
          timeout  = "2s"
        }

        check {
          type     = "http"
          name     = "app_health"
          path     = "/dashboard"
          interval = "60s"
          timeout  = "5s"
          
          check_restart {
            limit = 3
            grace = "90s"
            ignore_warnings = false
          }
        }
    }

    task "server" {
      driver = "docker"
      config {
        image = "traefik:3.0"
        // image = "traefik:2.10"
        ports = ["admin", "http"]
        args = [
          "--api.dashboard=true",
          "--api.insecure=true", ### For Test only, please do not use that in production
          "--entrypoints.web.address=:${NOMAD_PORT_http}",
          "--entrypoints.websecure.address=:${NOMAD_PORT_https}",
          "--entrypoints.traefik.address=:${NOMAD_PORT_admin}",
          "--providers.nomad=true",
          "--providers.nomad.endpoint.address=http://10.20.30.41:4646", ### IP to your nomad server
        ]
      }
    }
  }
}