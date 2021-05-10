#!/usr/bin/bash

#Test si openjdk est installé
dpkg -l | grep openjdk-8-jdk
RETOUR_INSTALL_OPENJDK=$?
#Test presence du binaire nexus
RETOUR_BIN_NEXUS=/opt/nexus/bin/nexus

if [[ $RETOUR_INSTALL_OPENJDK = 0 ]] && [[ ! -f $RETOUR_BIN_NEXUS ]]; then
    echo "Serveur Nexus déjà installé"
    exit 0
fi

#mise en place du mot de passe pour vagrant
echo 'vagrant:vagrant' | sudo chpasswd

sudo apt -y update
sudo apt -y install openjdk-8-jdk

#Test si le user nexus existe
RETOUR_USER_NEXUS=sudo cat /etc/passwd | grep -i nexus
#creation du user nexus et positionnement dans le sudoers
if [[ $RETOUR_USER_NEXUS != 0 ]]; then
    useradd -M -d /opt/nexus -s /bin/bash -r nexus
    echo "nexus   ALL=(ALL)       NOPASSWD: ALL" > /etc/sudoers.d/nexus
fi

#Download des sources
URLDL=https://sonatype-download.global.ssl.fastly.net/repository/downloads-prod-group/3/nexus-3.29.2-02-unix.tar.gz
wget $URLDL
sleep 5s
if [[ ! -f nexus-3.29.2-02-unix.tar.gz ]]; then
    echo "Problème de download $URLDL \n"
    exit 0
fi

#creation du dossier cible
if [ ! -d "/opt/nexus" ]; then
        sudo mkdir /opt/nexus
        #decompression des sources dans le dossier cible
        tar xzf nexus-3.29.2-02-unix.tar.gz -C /opt/nexus --strip-components=1
        #positionnement du proprietaire dans le dossier cible
        chown -R nexus: /opt/nexus
fi

#positionnement du user nexus
grep "run_as_user=\"nexus\"" /opt/nexus/bin/nexus.rc
if [[ ! $? = 0 ]]; then
    sed -i 's/#run_as_user=""/run_as_user="nexus"/' /opt/nexus/bin/nexus.rc
fi

## Ajustement des chemins
sudo sed -i 's/..\/sonatype-work/.\/sonatype-work/g' /opt/nexus/bin/nexus.vmoptions
sudo sed -i 's/2073/1024/g' /opt/nexus/bin/nexus.vmoptions

#Demarrage de nexus
sudo -u nexus /opt/nexus/bin/nexus start

# Creation du serviceService
cat > /etc/systemd/system/nexus.service << 'EOL'
[Unit]
Description=nexus service
After=network.target

[Service]
Type=forking
LimitNOFILE=65536
ExecStart=/opt/nexus/bin/nexus start
ExecStop=/opt/nexus/bin/nexus stop
User=nexus
Restart=on-abort

[Install]
WantedBy=multi-user.target
EOL
#arret du service
/opt/nexus/bin/nexus stop
#activation du service au reboot machine
systemctl daemon-reload
systemctl enable --now nexus.service

#Autorisation de l'acces
ufw allow 8081/tcp

# Affiche le mot de passe
echo 'Mot de passe admin dans 5min en cours de generation PATIENTEZ SVP...:\n'
#Attente pour la generation du password
sleep 5m
cat /opt/nexus/sonatype-work/nexus3/admin.password
echo '\n\n'