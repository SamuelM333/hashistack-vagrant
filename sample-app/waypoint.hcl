project = "sample-app"

app "sample-app" {
  url {
    auto_hostname = true
  }

  build {
    use "docker" {}
    registry {
      use "docker" {
        image = "samuelm333/sample-app"
        tag   = "latest"
      }
    }
  }

  deploy {
    use "nomad-jobspec" {
      jobspec = templatefile("${path.app}/app.nomad.tpl")
    }
  }

  // release {
  //   use "nomad-jobspec-canary" {
  //     groups = [
  //       "app"
  //     ]
  //   }
  // }
}
