class Poste:

    def __init__(self, id=0, host='', ip='', nombre_cpu='', taille_ram='', nombre_disque='', taille_disque='', os='',
                 version_os=''):
        self.id = id
        self.host = host
        self.ip = ip
        self.nombre_cpu = nombre_cpu
        self.taille_ram = taille_ram
        self.nombre_disque = nombre_disque
        self.taille_disque = taille_disque
        self.os = os
        self.version_os = version_os
