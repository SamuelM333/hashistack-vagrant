server {
  enabled          = true
  bootstrap_expect = 1
}

plugin "docker" {
  allow_privileged = true
}

ui {
  enabled =  true

  consul {
    ui_url = "http://192.168.56.10:8500/ui"
  }

  # vault {
  #   ui_url = "https://vault.example.com:8200/ui"
  # }
}
