# Crea una classe Studente con:
class Studente:
    def __init__(self,nome,eta,corso):
        self.nome = nome
        self.__eta = eta
        self.corso = corso

# @classmethod per creare uno studente a partire da una stringa "Luca-20-Matematica"
    @classmethod
    def conversione_stringa(cls,stringa):
        nome,eta,corso=stringa.split("-")
        return cls(nome,int(eta),corso)
    
# @property per calcolare l'anno di nascita a partire dall'età
    @property
    def anno_nascita(self):
        return 2026 - self.__eta
    
# @property con setter per impedire che l'età sia negativa
    @property
    def eta(self):
        return self.__eta
    
    @eta.setter
    def eta(self, eta):
        if eta < 0:
            print("L'età non può essere negativa")
        else:
            self.__eta = eta

studente = Studente.conversione_stringa("Luca-20-Matematica")
print(f"Sono {studente.nome}, ho {studente.eta} e faccio {studente.corso}")

print(f"Sono nato nel {studente.anno_nascita}")

studente.eta = 25

studente.anno_nascita
print(f"Sono nato nel {studente.anno_nascita} e ho {studente.eta} anni")