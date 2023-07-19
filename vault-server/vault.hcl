# https://learn.hashicorp.com/tutorials/vault/getting-started-deploy?in=vault/getting-started#configuring-vault

# TODO Change to consul KV
storage "raft" {
  path    = "/home/vagrant/vault/data"
  node_id = "node1"
}

listener "tcp" {
  address     = "10.20.30.60:8200"
  tls_disable = "true"
}

api_addr = "http://10.20.30.60:8200"
cluster_addr = "https://10.20.30.60:8201"
ui = true

service_registration "consul" {
    address = "10.20.30.60:8500"
}
