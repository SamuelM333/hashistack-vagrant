datacenter = "dc1"
server     = true
node_name  = "consul" 
data_dir   = "/opt/consul"

client_addr      = "{{ GetPrivateInterfaces | exclude \"type\" \"ipv6\" | join \"address\" \" \" }}"
// bind_addr        = "0.0.0.0"
bind_addr        = "{{ GetInterfaceIP `eth1` }}"
advertise_addr   = "{{ GetInterfaceIP `eth1` }}"
bootstrap_expect = 1

ui_config {
  enabled = true
}

connect {  
  enabled = true
}

ports {
  grpc = 8502
}
