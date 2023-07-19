datacenter = "dc1"
server     = false

data_dir       = "/opt/consul"
client_addr    = "0.0.0.0"
bind_addr      = "{{ GetInterfaceIP `eth1` }}"
advertise_addr = "{{ GetInterfaceIP `eth1` }}"
retry_join     = ["10.20.30.40"]  # TODO Remove hardcoded IP

leave_on_terminate = true
