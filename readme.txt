**0 - Prérequis:**
- Avoir installé git bash et vagrant
- Ne pas avoir de vm vagrant démarré utilisant les mêmes ports en forward(8080,8081,8082) virtualbox sinon éteindre les vm virtualbox déjà présente le temps de la vérification.
- Adapter l' adresse ip dans les vagrantfile afin d'etre dans le même réseau

A partir de l'explorateur windows, dans le dossier vagrant des différents serveur faire un clic droit git bash here puis saisir vagrant up pour tous les hosts ci-dessous :

L'utilisateur utilisé est vagrant et sont password vagrant.

*Plan d'adressage IP préconfiguré dans les vagrantfile du git clone et ordre d'installation suivant:*
1. serveur nexus 192.168.1.200          ==> remplacer *MAVM* ci-dessous par: srvnexus
2. serveur build 192.168.1.201          ==> remplacer *MAVM* ci-dessous par: srvbuild
3. serveur icjenkins 192.168.1.202      ==> remplacer *MAVM* ci-dessous par: srvicjenkins
4. serveur envapp 192.168.1.203           ==> remplacer *MAVM* ci-dessous par: srvenvapp

Schema d'architecture:


Matrice de flux:
Description - IP source - IP destination - port

**1 - Faire un git clone**
```shell
ouvrir git bash chosir un dossier de travail puis:
git clone https://github.com/gb-0001/tp_mai_gitpythonwsic.git
puis se positionner dans tp_mai_gitpythonwsic/*MAVM*/vagrant/ à remplacer avec le bon nom ci-dessus pour faire le vagrant up ensuite:

```

- ADAPTER LE CHEMIN POUR CHAQUE VM au niveau tp_mai_gitpythonwsic/*MAVM*/vagrant/,
- faire clic droit git bash here ou se situ le vagrantfile exemple tp_mai_gitpythonwsic/*MAVM*/vagrant/vagrantfile

- git bash ouvert, sur les hosts du plan d'adressage ci-dessus faire:
```shell
vagrant up
```