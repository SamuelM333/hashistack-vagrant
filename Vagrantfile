SERVER_COUNT = 3
CLIENT_COUNT = 3

Vagrant.configure("2") do |config|
  config.vm.box = "rockylinux/9"

  config.vm.provider "libvirt" do |provider|
    provider.memory = "512"
    provider.cpus = 1
  end

  config.vm.define "consul" do |subconfig|
    subconfig.vm.hostname = "consul"

    subconfig.vm.network :private_network, ip: "10.20.30.40"
    subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"
  end

  config.vm.define "vault" do |subconfig|
    subconfig.vm.hostname = "vault"

    subconfig.vm.network :private_network, ip: "10.20.30.60"
    subconfig.vm.network "forwarded_port", guest: 8200, host: 8200, host_ip: "127.0.0.1"
  end

  (1..SERVER_COUNT).each do |i|
    config.vm.define "nomad-server-#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-server-#{i}"

      subconfig.vm.network :private_network, ip: "10.20.30.#{40 + i}"
    end
  end

  (1..CLIENT_COUNT).each do |i|
    config.vm.define "nomad-client-#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-client-#{i}"

      subconfig.vm.provider "libvirt" do |provider|
        provider.cpus = 2
        provider.memory = "1024"
      end

      subconfig.vm.network :private_network, ip: "10.20.30.#{50 + i}"
    end
  end
end
