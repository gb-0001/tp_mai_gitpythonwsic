import bdd
from srvenvapp.vagrant.vagrant.application.Poste import Poste

listPoste = []
listPosteFile = bdd.read_bd()


def createposte():
    pass


def get_poste(host):
    for poste in get_postes():
        if poste.host == host:
            return poste
    return Poste()


def update_poste(host):
    pass


def delete_poste(host):
    for machine in listPosteFile:
        if machine["host"] == host:
            listPosteFile.remove(1)
    print(listPosteFile)


def get_postes():
    lstObjPostes = []
    for poste in listPosteFile:
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