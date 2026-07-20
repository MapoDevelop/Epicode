# Costruiiamo un piccolo sistema per gestire figure geometriche:
# Definiamo una classe astratta Forma con due metodi astratti:
# - area() che calcola l'area della forma
# - perimetro() che calcola il perimetro della forma

from abc import ABC, abstractmethod
import math

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    def __eq__(self, altra):
        return math.isclose(self.area(), altra.area())
    
    def __str__(self):
        return f"{self.__class__.__name__}, Area: {self.area():.2f}, Perimetro: {self.perimetro():.2f}"
    
    def __add__(self, altra):
        return FiguraComposta(self, altra)

# Due figure concrete: 
# - Rettangolo
# - Cerchio

class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)

class Cerchio(Forma):
    def __init__(self, raggio):
        self._raggio = raggio

# Funzionalità extra:
# - @property per calcolare il diametro del cerchio
    @property
    def raggio(self):
        return self._raggio
    
    @property
    def diametro(self):
        return self._raggio * 2
    
    def area(self):
        return math.pi * self._raggio ** 2

    def perimetro(self):
        return 2 * math.pi * self._raggio

# - Overloading dell'operatore + per combinare due figure in una terza 
#   che rappresenti la loro area totale.
# - Overloading di __eq__ per confrontare due figure in base alla loro area.
# - Polimorfismo con una lista di figure diverse.
class FiguraComposta(Forma):
    def __init__(self, forma1, forma2):
        self.forma1 = forma1
        self.forma2 = forma2

    def area(self):
        return self.forma1.area() + self.forma2.area()
    
    def perimetro(self):
        return self.forma1.perimetro() + self.forma2.perimetro()
    
    def __str__(self):
        return f"Figura Composta: {self.forma1} + {self.forma2}, Area Totale: {self.area():.2f}, Perimetro Totale: {self.perimetro():.2f}"

if __name__ == "__main__":
    rettangolo = Rettangolo(4, 5)
    cerchio = Cerchio(3)
        
    figure = [rettangolo, cerchio]
    for figura in figure:
        print(figura)  # Stampa le informazioni di ciascuna figura

    print(f"Diametro del cerchio: {cerchio.diametro}")  # Diametro del cerchio: 6

    # Confronto tra figure
    print("Il rettangolo e il cerchio hanno la stessa area?", rettangolo == cerchio)  # False
    
    # Combinazione di figure con l'operatore +
    figura_combinata = rettangolo + cerchio
    print(figura_combinata)  # Figura Composta: Rettangolo, Area: 20.00, Perimetro: 18.00 + Cerchio, Area: 28.27, Perimetro: 18.85, Area Totale: 48.27