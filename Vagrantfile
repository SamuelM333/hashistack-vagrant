AGENT_COUNT = 3
CLIENT_COUNT = 3

Vagrant.configure("2") do |config|
  config.vm.box = "fedora/35-cloud-base"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
    vb.cpus = 2
  end

  #config.vm.synced_folder "aws/", "/home/vagrant/aws", owner: "vagrant", group: "vagrant"

  # TODO Install with binary
  # https://releases.hashicorp.com/nomad/1.2.4/nomad_1.2.4_linux_amd64.zip
  config.vm.provision "deps", type: "shell", inline: <<-SHELL
    sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
    sudo dnf -y install nomad consul vault bind-utils traceroute tcpdump
  SHELL

  config.vm.define "consul" do |subconfig|
    subconfig.vm.network :private_network, ip: "192.168.56.10"
    subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"

    subconfig.vm.provision "app:setup", type: "shell", run: "always", inline: <<-SHELL
      mkdir -p /etc/consul.d
      cp /vagrant/consul-server/consul.hcl /etc/consul.d/

      cp /vagrant/shared/consul.service /etc/systemd/system/
      sudo systemctl enable --now consul
      sudo systemctl daemon-reload
    SHELL
  end

  config.vm.define "vault" do |subconfig|
    subconfig.vm.network :private_network, ip: "192.168.56.30"
    subconfig.vm.network "forwarded_port", guest: 8200, host: 8200, host_ip: "127.0.0.1"

    # TODO Check shared files. Vault specific files might only go here
    # subconfig.vm.provision "deps", type: "shell", inline: <<-SHELL
    #   sudo dnf -y install vault
    # SHELL

    subconfig.vm.provision "app:setup", type: "shell", run: "always", inline: <<-SHELL
      mkdir -p $HOME/vault/data
      
      mkdir -p /etc/{consul,vault}.d
      cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
      cp /vagrant/vault-server/vault.hcl /etc/vault.d/
      
      cp /vagrant/shared/consul.service /etc/systemd/system/
      cp /vagrant/vault-server/vault.service /etc/systemd/system/
      sudo systemctl enable --now consul vault
      sudo systemctl daemon-reload
    SHELL
  end

  (1..AGENT_COUNT).each do |i|
    config.vm.define "nomad-node#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-node#{i}"
      subconfig.vm.network :private_network, ip: "192.168.56.#{i + 10}"
      #subconfig.vm.network "forwarded_port", guest: 4646, host: "4646#{i}", host_ip: "127.0.0.1"
      #subconfig.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"    # Nomad Autoscaler health check
    
      subconfig.vm.provision "app:setup", type: "shell", run: "always", inline: <<-SHELL
        mkdir -p /etc/{consul,nomad}.d
        cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
        cp /vagrant/shared/nomad-common.hcl /etc/nomad.d/
        cp /vagrant/nomad-server/nomad.hcl /etc/nomad.d/

        cp /vagrant/shared/{consul,nomad}.service /etc/systemd/system/
        sudo systemctl enable --now consul nomad
        sudo systemctl daemon-reload
      SHELL
    end
  end
  
  (1..CLIENT_COUNT).each do |i|
    config.vm.define "nomad-client#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-client#{i}"

      subconfig.vm.network :private_network, ip: "192.168.56.#{i + 20}"
      #subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"

      subconfig.vm.provision :docker
      subconfig.vm.provision "docker", type: "shell", inline: <<-SHELL
        usermod -aG docker vagrant
      SHELL

      subconfig.vm.provision "app:setup", type: "shell", run: "always", inline: <<-SHELL
        mkdir -p /etc/{consul,nomad}.d
          cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
          cp /vagrant/shared/nomad-common.hcl /etc/nomad.d/
          cp /vagrant/nomad-client/nomad.hcl /etc/nomad.d/

          cp /vagrant/shared/{consul,nomad}.service /etc/systemd/system/
          sudo systemctl enable --now consul nomad
          sudo systemctl daemon-reload
      SHELL
    end
  end
end
