# Creare un sistema per gestire conti bancari diversi, sfruttando:
# - classi astratte
# - ereditarietà
# - polimorfismo
# - property
# - decoratori
# - operator overloading

from abc import ABC, abstractmethod

class Conto(ABC):
    def __init__(self, intestatario, saldo = 0):
        self._intestatario = intestatario
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo
    
    @staticmethod
    def valida_importo(importo):
        return importo > 0
    
    @abstractmethod
    def deposita(self, importo):
        pass
    
    @abstractmethod
    def preleva(self, importo):
        pass

    def __str__(self):
        return f"Conto intestato a {self._intestatario}, saldo: {self._saldo:.2f}€"
    
class ContoCorrente(Conto):
    commissione = 1.5  # Commissione fissa per ogni prelievo
    def deposita(self, importo):
        if self.valida_importo(importo):
            self._saldo += importo
            print(f"Deposito di {importo:.2f}€ effettuato.")
        else:
            print("Importo non valido per il deposito.")

    def preleva(self, importo):
        totale = importo + self.commissione
        if self.valida_importo(importo) and (self._saldo >= totale):
            self._saldo -= totale
            print(f"Prelievo di {importo:.2f}€ effettuato. Commissione di {self.commissione:.2f}€ applicata. Totale addebitato: {totale:.2f}€.")
            print(f"Saldo rimanente: {self._saldo:.2f}€.")
        else:
            print("Prelievo non valido o saldo insufficiente.")
    
    def __add__(self, altro):
        if isinstance(altro, Conto):
            nuovo_saldo = self._saldo + altro.saldo
            return ContoCorrente(f"{self._intestatario} & {altro._intestatario}", nuovo_saldo)
        else:
            raise ValueError("L'oggetto da sommare deve essere un'istanza di Conto.")
        
if __name__ == "__main__":
    conto1 = ContoCorrente("Mario Rossi", 1000)
    conto2 = ContoCorrente("Luigi Bianchi", 500)

    print(conto1)
    print(conto2)

    conto1.deposita(200)
    conto1.preleva(150)

    conto2.deposita(300)
    conto2.preleva(100)

    print(conto1)
    print(conto2)

    # Somma dei conti
    conto_totale = conto1 + conto2
    print(conto_totale)