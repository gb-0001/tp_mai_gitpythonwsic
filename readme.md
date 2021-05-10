**0 - Prérequis:**
- Avoir installé git bash et vagrant
- Ne pas avoir de vm vagrant démarré utilisant les mêmes ports en forward(8080,8081) virtualbox sinon éteindre les vm virtualbox déjà présente le temps de la vérification.
- Adapter l' adresse ip dans les vagrantfile afin d'etre dans le même réseau à adapter suivant la configuration local.

A partir de l'explorateur windows, dans le dossier vagrant des différents serveur faire un clic droit git bash here puis saisir vagrant up pour tous les hosts ci-dessous :

L'utilisateur utilisé est vagrant et sont password vagrant.

*Plan d'adressage IP préconfiguré dans les vagrantfile du git clone et ordre d'installation suivant:*
1. serveur nexus 192.168.1.200          ==> remplacer *MAVM* par: srvnexus      ==>tp_mai_gitpythonwsic/Elements_chaine_IC/srvnexus/vagrant/
2. serveur build 192.168.1.201          ==> remplacer *MAVM* par: srvbuild      ==>tp_mai_gitpythonwsic/Elements_chaine_IC/srvbuild/vagrant/
3. serveur icjenkins 192.168.1.202      ==> remplacer *MAVM* par: srvicjenkins  ==>tp_mai_gitpythonwsic/Elements_chaine_IC/srvicjenkins/vagrant/
4. serveur envapp 192.168.1.203         ==> remplacer *MAVM* par: srvenvapp     ==>tp_mai_gitpythonwsic/Env_Exec_App/srvenvapp/vagrant/

Schema d'architecture:


Matrice de flux:
Description - IP source - IP destination - port

**1 - Faire un git clone**
Le lancement des vm vagrant s'effectura à partir du dossier repectif des vagrantfile et dans l'arboresence du git clone
```shell
ouvrir git bash chosir un dossier de travail puis:
git clone https://github.com/gb-0001/tp_mai_gitpythonwsic.git
puis depuis l\'explorateur se positionner dans tp_mai_gitpythonwsic/*MONDOSSIER*/*MAVM*/vagrant/ à remplacer avec le bon nom ci-dessus pour faire le vagrant up ensuite:

```

- ADAPTER LE CHEMIN POUR CHAQUE VM au niveau tp_mai_gitpythonwsic/*MONDOSSIER*/*MAVM*/vagrant/,
- faire clic droit git bash here ou se situ le vagrantfile depuis l'explorateur windows exemple tp_mai_gitpythonwsic/*MONDOSSIER*/*MAVM*/vagrant/vagrantfile

- git bash ouvert, sur les hosts du plan d'adressage ci-dessus faire:
```shell
vagrant up
```



**Installation pour chaque type de machine:**
La commande d'installation pour executer le script install.sh est inclus directement dans le vagrantfile et l'installation s'effectue au moment du vagrant up.

**2 - A partir du git clone pour le serveur NEXUS avec vagrant ssh faire:**

```shell
Dans le git bash du dossier tp_mai_gitpythonwsic/Elements_chaine_IC/srvnexus/vagrant/ préalablement ouvert (avec git bash here clic droit) faire:
vagrant up
A la fin de l\'installation récupérer et stocker le mot de passe pour le compte admin du nexus sans les deux '\n\n' à la fin.

```
puis se connecter à la vm:
```shell
Faire:
vagrant ssh
```

TEST DE FONCTIONNEMENT:
```shell
Faire:
Vérifier le retour OK du ping
ping 192.168.1.200

```
- Vérifier le fonctionnement ouvrir le navigateur et saisir http://192.168.1.200:8081/ vérifier si la page du site apparait.
Dans Documentation\srvnexus\doc_nexus.docx terminer l'installation et la configuration une fois tous les serveurs installés.

