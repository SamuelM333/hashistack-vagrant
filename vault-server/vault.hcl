# https://learn.hashicorp.com/tutorials/vault/getting-started-deploy?in=vault/getting-started#configuring-vault

# TODO Change to consul KV
storage "raft" {
  path    = "/home/vagrant/vault/data"
  node_id = "node1"
}

listener "tcp" {
  address     = "192.168.56.30:8200"
  tls_disable = "true"
}

api_addr = "http://192.168.56.30:8200"
cluster_addr = "https://192.168.56.30:8201"
ui = true

service_registration "consul" {
    address = "192.168.56.30:8500"
}
