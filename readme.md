**ORGANISATION**

Pour info: Absence Gerald le vendredi 14 en congé

*-Git*
-Sur github la branch master est la principale PROD
Les branch de type hb branch Henri
Les branch de type gb000X branch Gerald

Pull request validé par le binôme suivant les éléments traités
Les pull request validés par soit meme si pas de conflit sinon contact avec le binome (tchat, appel tel) pour verifier.

Initialisation et récupération du git en local:
git clone https://github.com/gb-0001/tp_mai_gitpythonwsic.git
création des 2 branches de dev sur le site github
création des 2 branches de dev localement avec sa branche respective hg ou gb0001 ou gb0002
avec git checkout -b hg/gb000X
Association des branches respectives
git branch --set-upstream-to=origin/gb0002 gb0002
git fetch pour MAJ
git pull pour la récupération des modification en remote
git add . + git commit -m "montext" + git push --set-upstream-to origin gb000X ou hg
Sur github le pull request de la branch en push + merge et git fetch localement pour rafraichir

Point de situation le matin, point d'avancement sur les éléménents du jours ou blocage en début d'après midi.


*-Répartition du travail comme suit sur le kanban du github dans l'onglet projet:*

https://github.com/gb-0001/tp_mai_gitpythonwsic/projects/1

- Taches d'infra gerald Vagrant file + script + doc jenkins et Nexus + readme.md Et Verfication Henri
- Taches Appli python + swagger + doc Henri
- Taches gradle gerald
- Taches jenkins Gerald par mode job + doc + xml


*-Description de l'architecture de l'application:*








**Plan de séquencement d'installation et configuration:**

1- procéder à l'installation ci-dessous des vm avec vagrant INFRA dans l'ordre suivant:
    - srvnexus
    - srvicjenkins
    - srvenvapp

2- Configurer le serveur Nexus utiliser la doc:

https://github.com/gb-0001/tp_mai_gitpythonwsic/blob/master/Documentation/srvnexus/doc_nexus.docx

3- Configurer le serveur jenkins avec la doc suivante:

https://github.com/gb-0001/tp_mai_gitpythonwsic/blob/master/Documentation/srvicjenkins/doc_jenkins.docx

4- Utilisation de l'application





**Les retours demandés:**

- Dossiers github:
    Application ==> appli python
    Documentation ==> par serveur
    Elements_chaine_IC ==> par serveur contient les vagrantfile préconfigurés et les scripts d'installation liés au vagrantfile dans le sous dossier vagrant
    A la racine le fichier build.gradle et versionCode.gradle utilisé par jenkins

- Pour le job jenkins et les traces de fonctionnement du job:
https://github.com/gb-0001/tp_mai_gitpythonwsic/blob/master/Documentation/srvicjenkins/config.xml
https://github.com/gb-0001/tp_mai_gitpythonwsic/blob/master/Documentation/srvicjenkins/doc_jenkins.docx

- Fichier gradle:
https://github.com/gb-0001/tp_mai_gitpythonwsic/blob/master/build.gradle






**INSTALLATION DES VAGRANTFILE POUR INSTALLER L'INFRA**

**0 - Prérequis:**
- Avoir installé git bash et vagrant
- Ne pas avoir de vm vagrant démarré utilisant les mêmes IP et ports en forward(8080,8081) virtualbox sinon éteindre les vm virtualbox déjà présente le temps de la vérification.
- Adapter l' adresse ip dans les vagrantfile afin d'etre dans le même réseau à adapter suivant la configuration local.

A partir de l'explorateur windows, dans le dossier vagrant des différents serveur faire un clic droit git bash here puis saisir vagrant up pour tous les hosts ci-dessous :

L'utilisateur utilisé est vagrant et sont password vagrant.

*Plan d'adressage IP préconfiguré dans les vagrantfile du git clone et ordre d'installation et le chemin du vagrantfile suivant:*
1. serveur nexus 192.168.1.200          ==> remplacer *MAVM* ci-dessous par: srvnexus
2. serveur build 192.168.1.201          ==> remplacer *MAVM* ci-dessous par: srvbuild (OPTIONNEL)
3. serveur icjenkins 192.168.1.202      ==> remplacer *MAVM* ci-dessous par: srvicjenkins
4. serveur envapp 192.168.1.203           ==> remplacer *MAVM* ci-dessous par: srvenvapp



Matrice de flux:

| Description               | IP source   | IP destination  | Port destination|
|---------------------------|-------------|-----------------|-----------------|
|Serveur Jenkins vers Nexus |192.168.1.202| 192.168.1.200   |       8081      |
|Serveur GitHub vers jenkins|GITHUB       | 192.168.1.202   |       8080      |
|srvenvapp vers|l'api Nexus |192.168.1.203| 192.168.1.200   |       8081

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

**2 - A partir du git clone pour le serveur NEXUS avec vagrant faire:**

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

**3 - A partir du git clone pour le serveur jenkins avec vagrant faire:**

```shell
Dans le git bash du dossier tp_mai_gitpythonwsic/Elements_chaine_IC/srvicjenkins/vagrant/ préalablement ouvert (avec git bash here clic droit) faire:
vagrant up
A la fin de l\'installation récupérer et stocker le mot de passe pour finir l\'installation jenkins demandé sur la page web.

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
ping 192.168.1.202
POur la partie build saisir la commande gradle --version pourle bon fonctionnement de la commande et doit retoourner la version:
gradle --version
```
- Vérifier le fonctionnement ouvrir le navigateur et saisir http://192.168.1.202:8080/ vérifier si la page du site apparait saisir le mot de passe jenkins récupéré avant.
Dans Documentation\srvicjenkins\doc_jenkins.docx terminer l'installation et la configuration une fois tous les serveurs installés.


**3 - (optionnel élément de préparation) A partir du git clone pour le serveur build avec vagrant faire:**

```shell
Dans le git bash du dossier tp_mai_gitpythonwsic/Elements_chaine_IC/srvbuild/vagrant/ préalablement ouvert (avec git bash here clic droit) faire:
vagrant up

Serveur optionnel en installation sert à préparer le build.gradle disponible sur le git avec versionCode.gradle

```
puis se connecter à la vm:
```shell
Faire:
vagrant ssh
```

TEST DE FONCTIONNEMENT:
```shell
Faire:
Vérifier le retour OK du ping vers le nexus
ping 192.168.1.200
POur la partie build saisir la commande gradle --version pourle bon fonctionnement de la commande et doit retourner la version:
gradle --version

Test manuel optionnel pris en charge par le pipe jenkins:
dans /home/vagrant
git clone https://github.com/gb-0001/tp_mai_gitpythonwsic.git
cd tp_mai_gitpythonwsic/Application
wget -O versionCode.gradle https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Elements_chaine_IC/srvbuild/build.gradle
wget -O build.gradle https://github.com/gb-0001/tp_mai_gitpythonwsic/raw/master/Elements_chaine_IC/srvbuild/versionCode.gradle
build manuel du fichier python vers le nexus:
gradle task write --no-daemon --info

```


**4 - A partir du git clone pour la machine d'environnement avec vagrant faire:**

```shell
Dans le git bash du dossier tp_mai_gitpythonwsic/Env_Exec_App/srvenvapp/vagrant/ préalablement ouvert (avec git bash here clic droit) faire:
vagrant up
A la fin de l\'installation récupérer et stocker le mot de passe pour finir l\'installation jenkins demandé sur la page web.

```
puis se connecter à la vm:
```shell
Faire:
vagrant ssh
```

TEST DE FONCTIONNEMENT:
```shell
Faire:
Vérifier le retour OK du ping du serveur jenkins
ping 192.168.1.202
saisir la commande python --version pour le bon fonctionnement de la commande et doit retourner la version:
python --version
```

Dans Documentation\srvicjenkins\doc_envapp.docx terminer l'installation et la configuration une fois tous les serveurs installés.


