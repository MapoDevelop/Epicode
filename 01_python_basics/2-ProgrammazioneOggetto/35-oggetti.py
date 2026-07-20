# Crea una classe base Forma con metodo area()
# Crea due classi derivate:
# - Rettangolo -> area() calcola l'area del rettangolo (base * altezza)
# - Cerchio -> area() calcola l'area del cerchio (pi * raggio^2)

# Crea una lista di forme e stampa l'area di ciascuna usando il metordo area()

import math

class Forma:
    def area(self):
        pass

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

forme = [Rettangolo(3, 4), Cerchio(5), Rettangolo(2, 6), Cerchio(2)]
for forma in forme:
    print(forma.area())