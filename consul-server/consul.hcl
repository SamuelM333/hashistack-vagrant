datacenter = "dc1"
server     = true
node_name  = "consul" 
data_dir   = "/opt/consul"

client_addr      = "0.0.0.0"
#bind_addr        = "0.0.0.0"
bind_addr        = "{{ GetInterfaceIP `enp0s8` }}"
# advertise_addr   = "{{ GetInterfaceIP `enp0s8` }}"
bootstrap_expect = 1

ui_config {
  enabled = true
}

connect {  
  enabled = true
}

ports {
  grpc  = 8502
}
