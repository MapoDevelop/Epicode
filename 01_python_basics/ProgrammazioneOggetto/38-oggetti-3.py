# Crea una classe Frazione che rappresenti una frazione con numeratore e denominatore. 

from math import gcd


class Frazione:
# Implementa i seguenti operatori:
# - (+) somma tra frazioni
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
    
    def __add__(self, altro):
        nuovo_numeratore = self.numeratore * altro.denominatore + altro.numeratore * self.denominatore
        nuovo_denominatore = self.denominatore * altro.denominatore
        return Frazione(nuovo_numeratore, nuovo_denominatore)

# - (==) uguaglianza tra frazioni, semplificando i valori
    def riduci(self):
        fattore_comune = gcd(self.numeratore, self.denominatore) #usato metodo math.gcd per trovare il massimo comune divisore
        return Frazione(self.numeratore // fattore_comune, self.denominatore // fattore_comune)
    
    def __eq__(self, altro):
        a = self.riduci()
        b = altro.riduci()
        return a.numeratore == b.numeratore and a.denominatore == b.denominatore
    
# - (__str__) stampare la frazione come "numeratore/denominatore"
    def __str__(self):
        return f"{self.numeratore}/{self.denominatore}"
    

frazione1 = Frazione(1, 2)
frazione2 = Frazione(1, 3)

frazione3 = frazione1 + frazione2
print(f"Somma: {frazione3}")

frazione4 = Frazione(2, 4)
if frazione1 == frazione4:
    print(f"Uguali: {frazione1} e {frazione4}")
else:
    print(f"Diverse: {frazione1} e {frazione3}")