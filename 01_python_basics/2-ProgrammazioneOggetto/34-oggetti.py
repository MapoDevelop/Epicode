#Crea una classe Animale con:
# - attributo di istanza nome
# - metodo verso()

# Crea due classi detivate:
# - Cane -> verso() stampa "Bau" 
# - Gatto -> verso() stampa "Miao"

class Animale:
    def __init__(self, nome):
        self.nome = nome

    def verso(self):
        pass
class Cane(Animale):
    def verso(self):
        print(f"{self.nome} dice Bau")

class Gatto(Animale):
    def verso(self):
        print(f"{self.nome} dice Miao")

gatto1 = Gatto("Whiskers")
cane1 = Cane("Fido")

gatto1.verso()
cane1.verso()