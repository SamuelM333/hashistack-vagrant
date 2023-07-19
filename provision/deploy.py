from pyinfra import host, local

local.include('provision/tasks/dependencies.py')
local.include('provision/tasks/firewall.py')

if 'consul_servers' in host.groups:
    local.include('provision/tasks/consul_common.py')
    local.include('provision/tasks/consul_server.py')

if 'consul_clients' in host.groups:
    local.include('provision/tasks/consul_common.py')
    local.include('provision/tasks/consul_client.py')

if 'vault_servers' in host.groups:
    local.include('provision/tasks/vault.py')

if 'nomad_servers' in host.groups:
    local.include('provision/tasks/nomad_common.py')
    local.include('provision/tasks/nomad_server.py')
    
if 'nomad_clients' in host.groups:
    local.include('provision/tasks/docker.py')
    local.include('provision/tasks/nomad_common.py')
    local.include('provision/tasks/nomad_client.py')