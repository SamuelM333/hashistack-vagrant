server {
  enabled = false
}

client {
  enabled = true
  host_volume "waypoint" {
    path      = "/home/vagrant/nomad/waypoint_volume"
    read_only = false
  }
}

ui {
  enabled =  false
}
