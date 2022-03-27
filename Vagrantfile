AGENT_COUNT = 1
CLIENT_COUNT = 1

Vagrant.configure("2") do |config|
  # config.vm.box = "fedora/35-cloud-base"
  config.vm.box = "ubuntu/focal64"
  # config.vm.box = "generic/rocky8"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
    vb.cpus = 1
  end

  config.vm.synced_folder ".", "/vagrant", owner: "vagrant", group: "vagrant"

  config.vm.provision "deps", type: "shell", inline: <<-SHELL
    # sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/fedora/hashicorp.repo
    # sudo dnf config-manager --add-repo https://rpm.releases.hashicorp.com/RHEL/hashicorp.repo
    # sudo dnf -y install nomad consul vault bind-utils traceroute tcpdump
    # sudo dnf -y install nomad consul vault
    # sudo dnf -y install unzip wget
    sudo apt install unzip

    CONSUL_VER="1.11.2"
    NOMAD_VER="1.2.4"
    VAULT_VER="1.9.3"

    wget -nv https://releases.hashicorp.com/nomad/${NOMAD_VER}/nomad_${NOMAD_VER}_linux_amd64.zip -O nomad.zip
    unzip nomad.zip
    sudo mv nomad /usr/bin
    sudo chmod +x /usr/bin/nomad
    rm nomad.zip

    wget -nv https://releases.hashicorp.com/consul/${CONSUL_VER}/consul_${CONSUL_VER}_linux_amd64.zip -O consul.zip
    unzip consul.zip
    sudo mv consul /usr/bin
    sudo chmod +x /usr/bin/consul
    rm consul.zip

    wget -nv https://releases.hashicorp.com/vault/${VAULT_VER}/vault_${VAULT_VER}_linux_amd64.zip -O vault.zip
    unzip vault.zip
    sudo mv vault /usr/bin
    sudo chmod +x /usr/bin/vault
    rm vault.zip
  SHELL

  config.vm.define "consul" do |subconfig|
    subconfig.vm.hostname = "consul"

    subconfig.vm.network :private_network, ip: "192.168.56.10"
    subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"

    subconfig.vm.provision "setup:consul", type: "shell", run: "always", inline: <<-SHELL
      mkdir -p /etc/consul.d
      cp /vagrant/consul-server/consul.hcl /etc/consul.d/

      cp /vagrant/shared/consul.service /etc/systemd/system/
      sudo systemctl enable --now consul
      sudo systemctl daemon-reload
      consul --version
    SHELL
  end

  config.vm.define "vault" do |subconfig|
    subconfig.vm.hostname = "vault"

    subconfig.vm.network :private_network, ip: "192.168.56.30"
    subconfig.vm.network "forwarded_port", guest: 8200, host: 8200, host_ip: "127.0.0.1"

    # TODO Check shared files. Vault specific files might only go here
    # subconfig.vm.provision "deps", type: "shell", inline: <<-SHELL
    #   sudo dnf -y install vault
    # SHELL

    subconfig.vm.provision "setup:vault", type: "shell", run: "always", inline: <<-SHELL
      mkdir -p /home/vagrant/vault/data

      mkdir -p /etc/{consul,vault}.d
      cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
      cp /vagrant/vault-server/vault.hcl /etc/vault.d/

      cp /vagrant/shared/consul.service /etc/systemd/system/
      cp /vagrant/vault-server/vault.service /etc/systemd/system/
      sudo systemctl enable --now consul vault
      sudo systemctl daemon-reload
      vault --version
    SHELL
  end

  (1..AGENT_COUNT).each do |i|
    config.vm.define "nomad-node#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-node#{i}"

      subconfig.vm.network :private_network, ip: "192.168.56.#{i + 10}"
      #subconfig.vm.network "forwarded_port", guest: 4646, host: "4646#{i}", host_ip: "127.0.0.1"
      #subconfig.vm.network "forwarded_port", guest: 8080, host: 8080, host_ip: "127.0.0.1"    # Nomad Autoscaler health check

      subconfig.vm.provision "setup:agent", type: "shell", run: "always", inline: <<-SHELL
        mkdir -p /etc/{consul,nomad}.d
        cp /vagrant/shared/consul-client.hcl /etc/consul.d/consul.hcl
        cp /vagrant/shared/nomad-common.hcl /etc/nomad.d/
        cp /vagrant/nomad-server/nomad.hcl /etc/nomad.d/

        cp /vagrant/shared/{consul,nomad}.service /etc/systemd/system/
        sudo systemctl enable --now consul nomad
        sudo systemctl daemon-reload
        nomad --version
      SHELL
    end
  end

  (1..CLIENT_COUNT).each do |i|
    config.vm.define "nomad-client#{i}" do |subconfig|
      subconfig.vm.hostname = "nomad-client#{i}"

      subconfig.vm.provider "virtualbox" do |vb|
        # vb.memory = "1024"
        vb.memory = "1536"
        vb.cpus = 2
      end

      subconfig.vm.network :private_network, ip: "192.168.56.#{i + 20}"
      #subconfig.vm.network "forwarded_port", guest: 8500, host: 8500, host_ip: "127.0.0.1"

      subconfig.vm.provision :docker
      subconfig.vm.provision "docker", type: "shell", inline: <<-SHELL
        usermod -aG docker vagrant
      SHELL

      subconfig.vm.provision "setup:client", type: "shell", run: "always", inline: <<-SHELL
        mkdir -p /home/vagrant/nomad/waypoint_volume

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
