data_dir = "/opt/nomad"

bind_addr = "{{ GetInterfaceIP `eth1` }}"

advertise {
  http = "{{ GetInterfaceIP `eth1` }}"
  rpc  = "{{ GetInterfaceIP `eth1` }}"
  serf = "{{ GetInterfaceIP `eth1` }}"
}

consul {
  address = "10.20.30.40:8500" # TODO Remove hardcoded IP
}
