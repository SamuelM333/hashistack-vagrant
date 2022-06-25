SERVER_COUNT = 3
CLIENT_COUNT = 3

Vagrant.configure("2") do |config|
  config.vm.box = "generic/rocky8"

  config.vm.provider "libvirt" do |provider|
    provider.memory = "512"
    provider.cpus = 1
  end

  config.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant"

  config.vm.provision "deps", type: "shell", inline: <<-SCRIPT
    sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
    sudo dnf -y install nomad consul vault waypoint bind-utils traceroute tcpdump
    sudo rm /etc/nomad.d/nomad.hcl
  SCRIPT

  config.vm.provision "firewall", type: "shell", inline: <<-SCRIPT
    # Consul
    # https://www.consul.io/docs/install/ports
    sudo firewall-cmd --permanent --add-port=8500/tcp
    sudo firewall-cmd --permanent --add-port=8600/udp
    sudo firewall-cmd --permanent --add-port=8600/tcp
    sudo firewall-cmd --permanent --add-port=8301/tcp
    sudo firewall-cmd --permanent --add-port=8301/udp
    sudo firewall-cmd --permanent --add-port=8302/tcp
    sudo firewall-cmd --permanent --add-port=8302/udp
    sudo firewall-cmd --permanent --add-port=8300/tcp

    # Nomad
    # https://www.nomadproject.io/docs/install/production/requirements#ports-used=
    sudo firewall-cmd --permanent --add-port=4646/tcp
    sudo firewall-cmd --permanent --add-port=4647/tcp
    sudo firewall-cmd --permanent --add-port=4648/tcp
    sudo firewall-cmd --permanent --add-port=4648/udp

    sudo firewall-cmd --reload
  SCRIPT

  config.vm.define "consul" do |subconfig|
    subconfig.vm.hostname = "consul"

    subconfig.vm.network :private_network, ip: "10.20.30.40"
    subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"

    subconfig.vm.provision "setup:consul", type: "shell", run: "always", inline: <<-SCRIPT
      sudo useradd consul
      mkdir -p /etc/consul.d
      cp /vagrant/consul-server/consul.hcl /etc/consul.d

      cp /vagrant/shared/consul.service /etc/systemd/system/consul.service
      mkdir -p /etc/systemd/system/consul.d

      sudo chown --recursive consul:consul /etc/consul.d
      sudo chown --recursive consul:consul /opt/consul

      sudo systemctl enable --now consul
      sudo systemctl daemon-reload
      consul --version
    SCRIPT
  end

  # config.vm.define "vault" do |subconfig|
  #   subconfig.vm.hostname = "vault"

  #   subconfig.vm.network :private_network, ip: "192.168.56.30"
  #   subconfig.vm.network "forwarded_port", guest: 8200, host: 8200, host_ip: "127.0.0.1"

  #   # TODO Check shared files. Vault specific files might only go here
  #   # subconfig.vm.provision "deps", type: "shell", inline: <<-SCRIPT
  #   #   sudo dnf -y install vault
  #   # SCRIPT

  #   subconfig.vm.provision "setup:vault", type: "shell", run: "always", inline: <<-SCRIPT
  #     mkdir -p /home/vagrant/vault/data

  #     mkdir -p /etc/{consul,vault}.d
  #     cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
  #     cp /vagrant/vault-server/vault.hcl /etc/vault.d/

  #     cp /vagrant/shared/consul.service /etc/systemd/system/
  #     cp /vagrant/vault-server/vault.service /etc/systemd/system/
  #     sudo systemctl enable --now consul vault
  #     sudo systemctl daemon-reload
  #     vault --version
  #   SCRIPT
  # end

  (1..SERVER_COUNT).each do |i|
    config.vm.define "nomad-server-#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-server-#{i}"

      subconfig.vm.network :private_network, ip: "10.20.30.#{40 + i}"

      subconfig.vm.provision "setup:agent", type: "shell", run: "always", inline: <<-SCRIPT
        mkdir -p /etc/{consul,nomad}.d
        cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
        cp /vagrant/shared/nomad-common.hcl /etc/nomad.d/
        cp /vagrant/nomad-server/nomad.hcl /etc/nomad.d/

        cp /vagrant/shared/{consul,nomad}.service /etc/systemd/system/
        sudo systemctl enable --now consul nomad
        sudo systemctl daemon-reload
        nomad --version
      SCRIPT
    end
  end

  (1..CLIENT_COUNT).each do |i|
    config.vm.define "nomad-client-#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-client-#{i}"

      subconfig.vm.provider "libvirt" do |provider|
        provider.memory = "1024"
        # provider.memory = "1536"
        provider.cpus = 2
      end

      subconfig.vm.network :private_network, ip: "10.20.30.#{50 + i}"

      subconfig.vm.provision :docker
      subconfig.vm.provision "docker", type: "shell", inline: <<-SCRIPT
        usermod -aG docker vagrant
      SCRIPT

      subconfig.vm.provision "setup:client", type: "shell", run: "always", inline: <<-SCRIPT
        mkdir -p /home/vagrant/nomad/waypoint_volume

        mkdir -p /etc/{consul,nomad}.d
        cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
        cp /vagrant/shared/nomad-common.hcl /etc/nomad.d/
        cp /vagrant/nomad-client/nomad.hcl /etc/nomad.d/

        cp /vagrant/shared/{consul,nomad}.service /etc/systemd/system/
        sudo systemctl enable --now consul nomad
        sudo systemctl daemon-reload
      SCRIPT
    end
  end
end
