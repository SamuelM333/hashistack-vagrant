job "factorial" {
  datacenters = ["dc1"]

  group "api" {
    count = 1

    network {
      port "kek" {
        to = 8080
      }
      // mode = "bridge"
    }

    task "factorial" {
      driver = "docker"

      config {
        image = "samuelm333/container-factorial:latest"
        ports = ["kek"]
      }

      resources {
        cpu    = 128
        memory = 128
      }
    }

    service {
      name = "factorial"
      port = "8080"
      tags = ["urlprefix-/"]

      // Maybe it is trying to hit the service from another node, not being able to reach it
      check {
        type     = "http"
        port     = "kek"
        path     = "/"
        interval = "15s"
        timeout  = "2s"
      }

      // check {
      //   type = "tcp"
      //   interval = "10s"
      //   timeout = "2s"
      // }
      
      // connect {
      //   sidecar_service {
      //     proxy {}
      //   }
      // }
    }
  }
}
