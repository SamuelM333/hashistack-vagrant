consul_servers = [
    "@vagrant/consul",
]

consul_clients = [
    "@vagrant/vault",
    "@vagrant/nomad-server-1",
    "@vagrant/nomad-server-2",
    "@vagrant/nomad-server-3",
    "@vagrant/nomad-client-1",
    "@vagrant/nomad-client-2",
    "@vagrant/nomad-client-3",
]

vault_servers = [
    "@vagrant/vault",
]

nomad_servers = [
    "@vagrant/nomad-server-1",
    "@vagrant/nomad-server-2",
    "@vagrant/nomad-server-3",
]

nomad_clients = [
    "@vagrant/nomad-client-1",
    "@vagrant/nomad-client-2",
    "@vagrant/nomad-client-3",
]