server {
  enabled          = true
  bootstrap_expect = 3
}

client {
  enabled = false
}

plugin "docker" {
  allow_privileged = true
}

ui {
  enabled =  true

  consul {
    ui_url = "http://localhost:8500/ui"
  }

   vault {
    ui_url = "http://localhost:8200/ui"
  }
}
