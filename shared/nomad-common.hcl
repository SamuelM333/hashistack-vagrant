data_dir = "/opt/nomad"

bind_addr = "{{ GetInterfaceIP `enp0s8` }}"

advertise {
  http = "{{ GetInterfaceIP `enp0s8` }}"
  rpc  = "{{ GetInterfaceIP `enp0s8` }}"
  serf = "{{ GetInterfaceIP `enp0s8` }}"
}

# TODO Remove hardcoded IP
consul {
  address = "192.168.56.10:8500"
}