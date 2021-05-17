import bdd
from poste import Poste

listPoste = []


def add_new_poste_in_file(new_poste):
    new_post_list = get_postes()
    new_post_list.append(new_poste)
    bdd.write_bd(new_post_list)
    printAllData(get_postes())


def generat_id():
    lastId = 0
    for poste in get_postes():
        if poste.id > lastId:
            lastId = poste.id

    return lastId + 1


def create_poste():
    print("Saisir les information du poste a ajouter")
    host = input("Saisir nom du hote:")
    ip = input("Saisir l'adresse IP du hote:")
    nombre_cpu = input("Saisir le nombre de CPU du hote:")
    taille_ram = input("Saisir la taille RAM du hote:")
    nombre_disque = input("Saisir le nombre de disque:")
    taille_disque = input("Saisir la taille disque dur du hote:")
    os = input("Saisir l'OS du hote:")
    version_os = input("Saisir la version de l'os:")
    newPoste = Poste(
        generat_id(),
        host,
        ip,
        nombre_cpu,
        taille_ram,
        nombre_disque,
        taille_disque,
        os,
        version_os)
    add_new_poste_in_file(newPoste)


def get_poste(host):
    for poste in get_postes():
        if poste.host == host:
            return poste
    return None


def update_poste(host):
    poste_to_update = get_poste(host)
    if poste_to_update != None:
        while (True):
            print("1. host")
            print("2. l'adresse Ip")
            print("3. Nombre CPU")
            print("4. Taille de la RAM")
            print("5. Nombre disque")
            print("6. Taille disque")
            print("7. OS (operating system)")
            print("8. version OS")
            print("E pour Enregistrer")
            inputValue = input("Choisissez la donnée à modififier : ")

            if inputValue == '1':
                poste_to_update.host = input("nouvelle valeur : ")
            elif inputValue == '2':
                poste_to_update.ip = input("nouvelle valeur : ")
            elif inputValue == '3':
                poste_to_update.nombre_cpu = input("nouvelle valeur : ")
            elif inputValue == '4':
                poste_to_update.taille_ram = input("nouvelle valeur : ")
            elif inputValue == '5':
                poste_to_update.nombre_disque = input("nouvelle valeur : ")
            elif inputValue == '6':
                poste_to_update.taille_disque = input("nouvelle valeur : ")
            elif inputValue == '7':
                poste_to_update.os = input("nouvelle valeur : ")
            elif inputValue == '8':
                poste_to_update.version_os = input("nouvelle valeur : ")
            elif inputValue.upper() == 'E':
                poste_list_with_updated = [poste_to_update if x.id == poste_to_update.id else x for x in get_postes()]
                bdd.write_bd(poste_list_with_updated)
                printAllData(get_postes())
                break


def delete_poste(host):
    new_post_list = get_postes()
    deleted_poste = [poste for poste in new_post_list if poste.host == host][0]
    index = new_post_list.index(deleted_poste)
    new_post_list.pop(index)

    ## suppression dans le fichier
    bdd.write_bd(new_post_list)
    printAllData(get_postes())


def get_postes():
    lstObjPostes = []
    for poste in bdd.read_bd():
        instance_poste = Poste(poste["id"], poste["host"], poste["ip"], poste["nombre_cpu"],
                               poste["taille_ram"], poste["nombre_disque"],
                               poste["taille_disque"], poste["os"], poste["version_os"])
        lstObjPostes.append(instance_poste)
    return lstObjPostes


def printAllData(lstObjPostes):
    lstDataPoste = []
    for data in lstObjPostes:
        lstDataPoste.append(str(data.id) + " " + str(
            data.host) + " " + str(
            data.ip) + " " + str(
            data.nombre_cpu) + " " + str(
            data.taille_ram) + " " + str(
            data.nombre_disque) + " " + str(
            data.taille_disque) + " " + str(data.os) + " " + str(data.version_os))
    print(str(lstDataPoste))


def printData(data):
    strData = str(data.id) + " " + str(
        data.host) + " " + str(
        data.ip) + " " + str(
        data.nombre_cpu) + " " + str(
        data.taille_ram) + " " + str(
        data.nombre_disque) + " " + str(
        data.taille_disque) + " " + str(data.os) + " " + str(data.version_os)
    print(strData)
