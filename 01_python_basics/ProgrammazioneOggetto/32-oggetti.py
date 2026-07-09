# Crea un a classe "Automobile" con:
# - Variabile di classe ruote = 4
# - Variabile di istanza modello

# Crea due automobili con modelli diversi e stampa il numero di ruote e il modello di ciascuna automobile.

class Automobile:
    ruote = 4

    def __init__(self, modello):
        self.modello = modello

auto1 = Automobile("Fiat")
auto2 = Automobile("Ferrari")

print(f"Prima auto: {auto1.modello} ha {auto1.ruote} ruote")
print(f"Prima auto: {auto2.modello} ha {auto2.ruote} ruote")