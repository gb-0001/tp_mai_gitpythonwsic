class Poste:

    def __init__(self, id=0, host='', ip='', nombre_cpu='', taille_ram='', nombre_disque='', taille_disque='', os='', version_os=''):
        self._id = id
        self._host = host
        self._ip = ip
        self._nombre_cpu = nombre_cpu
        self._taille_ram = taille_ram
        self._nombre_disque = nombre_disque
        self._taille_disque = taille_disque
        self._os = os
        self._version_os = version_os

    @property
    def id(self):
        return self._id

    @property
    def host(self):
        return self._host

    @property
    def ip(self):
        return self._ip

    @property
    def nombre_cpu(self):
        return self._nombre_cpu

    @property
    def taille_ram(self):
        return self._taille_ram

    @property
    def nombre_disque(self):
        return self._nombre_disque

    @property
    def taille_disque(self):
        return self._taille_disque

    @property
    def os(self):
        return self._os

    @property
    def version_os(self):
        return self._version_os