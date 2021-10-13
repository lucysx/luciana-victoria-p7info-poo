class Cachorro:
    def __init__(self, nome):
        self.nome = nome
        self.truques = []

    def add_truque(self, truque):
        self.truques.append(truque)
