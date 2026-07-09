# Crea una classe astratta "Veicolo" con metodo astratto "muovi()"
# Crea due classi concrete:
# - Auto -> muovi() stampa "L'auto si muove su strada"
# - Aereo -> muovi() stampa "L'aereo si muove nel cielo"
# Infine scrivi una funzione che accetti un generico Veicolo e chiami il metodo muovi().

from abc import ABC, abstractmethod

class Veicolo(ABC):
    @abstractmethod
    def muovi(self):
        pass

class Auto(Veicolo):
    def muovi(self):
        print("L'auto si muove su strada")
    
class Aereo(Veicolo):
    def muovi(self):
        print("L'aereo si muove nel cielo")

auto = Auto()
aereo = Aereo()

auto.muovi()
aereo.muovi()