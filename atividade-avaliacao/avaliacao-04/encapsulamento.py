class Perfil(object):
    def __init__(self):
        self._curtidas = 0

    def curtir(self):
        self._curtidas += 1

    def obter_curtidas(self):
        return self._curtidas
