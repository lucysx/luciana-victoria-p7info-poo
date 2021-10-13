class Ponto():
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def set_X(self, x):
        self.x = x
    
    def set_Y(self, y):
        self.y = y
    
    def get_X(self):
        return self.x

    def get_Y(self):
        return self.y

class Reta():
    def __init__(self, pA, pB):
        self.pA = pA
        self.pB = pB

    def set_pA(self, pA):
        self.pA = pA

    def set_pB(self, pB):
        self.pB = pB
    
    def get_pA(self):
        return self.pA
    
    def get_pB(self):
        return self.pB

    def distancia(self):
        eixoX = (self.get_pB().get_X() - self.get_pA().get_X())**2
        eixoY = (self.get_pB().get_Y() - self.get_pA().get_Y())**2
        d_pontos = (eixoX + eixoY) ** 0.5        
        return d_pontos

pA = Ponto(7, 1)
pB = Ponto(2, 9)

retaA = Reta(pA,pB)

print("Distância entre A e B =", retaA.distancia())
