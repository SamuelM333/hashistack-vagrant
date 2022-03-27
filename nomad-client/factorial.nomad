job "factorial" {
  datacenters = ["dc1"]

  group "api" {
    count = 3

    // network {
    //   port "http" {
    //     to = 8080
    //   }
    // }

    service {
      name = "factorial"
      port = "http"

      // check {
      //   name = "ping"
      //   type = "http"
      //   path = "/"
      //   interval = "60s"
      //   timeout  = "25s"
      // }
    }

    task "factorial" {
      driver = "docker"

      config {
        image = "samuelm333/container-factorial:latest"
        // ports = ["http"]
      }

      resources {
        cpu    = 500
        memory = 256
      }
    }
  }
}
