#!/bin/bash

#mise en place du mot de passe pour vagrant
echo 'vagrant:vagrant' | sudo chpasswd

## Ajout de python3:
sudo apt -y update
sudo apt -y install python3 python3-pip

#Autorisation de l'acces api
ufw allow 8000/tcp

#install utilitaire de test  pour exposition de l'api
sudo pip install pytest fastapi uvicorn

#Installation de l'appli suivant instructions donnés
mkdir /home/vagrant/Application
mkdir /home/vagrant/Application-flastapi
cd /home/vagrant/Application
wget -O bdd.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/bdd.py
wget -O crud.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/crud.py
wget -O inventory.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/inventory.py
wget -O poste.json https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/poste.json

cd /home/vagrant/Application-flastapi
wget -O bdd.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/Application-flastapi/bdd.py
wget -O crud.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/Application-flastapi/crud.py
wget -O Machine.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/Application-flastapi/Machine.py
wget -O poste.json https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/Application-flastapi/poste.json
wget -O main.py https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Application/Application-flastapi/main.py
