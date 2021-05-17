#!/bin/bash

#mise en place du mot de passe pour vagrant
echo 'vagrant:vagrant' | sudo chpasswd

## Ajout de python3:
sudo apt -y update
sudo apt -y install python3 python3-pip

#positionnement de python3 et pip3 dans le profil
echo "alias python='/usr/bin/python3'" > ~/.bashrc
echo "alias pip=pip3" > ~/.bashrc

#Autorisation de l'acces api
ufw allow 5000/tcp

#install utilitaire de test dont flask pour expostion de l'api
sudo pip install flask pytest fastapi uvicorn