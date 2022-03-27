data_dir       = "/opt/consul"
client_addr    = "0.0.0.0"
server         = false
bind_addr      = "{{ GetInterfaceIP `enp0s8` }}"
advertise_addr = "{{ GetInterfaceIP `enp0s8` }}"
retry_join     = ["192.168.56.10"]

datacenter         = "dc1"
leave_on_terminate = true
