server {
  enabled = false
}

client {
  enabled = true

  host_volume "waypoint_server" {
    path      = "/home/vagrant/nomad/volumes/waypoint_server"
    read_only = false
  }

  host_volume "waypoint_runner" {
    path      = "/home/vagrant/nomad/volumes/waypoint_runner"
    read_only = false
  }
}

ui {
  enabled = false
}
