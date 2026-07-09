# Crea una classe Studente con:
# Attributo di classe scuola = "Liceo Classico"
# Attributo di instanza nome
# Metodo di istanza: saluta() che stampa "Ciao, sono [nome] e frequento [scuola]"
# Metodo di classe: cambia_scuola(cls, nuova_scuola) che modifica la scuola per tutti gli studenti

class Studente:
    scuola = "Liceo Classico" # attributo di classe

    def __init__(self, nome):
        self.nome = nome #attributo di instanza

    def saluta(self): # metodo di instanza
        print(f"Ciao, sono {self.nome} e frequento {self.scuola}")

    @classmethod
    def cambia_scuola(cls, nuova_scuola): # metodo di classe
        cls.scuola = nuova_scuola
        return cls.scuola
    

# Creazione di due istanze della classe Studente
studente1 = Studente("Mario")
studente2 = Studente("Luigi")

studente1.saluta()  # Output: Ciao, sono Mario e frequento Liceo Classico
studente2.saluta()  # Output: Ciao, sono Luigi e frequento Liceo Classico

print("Cambio scuola per tutti gli studenti...")
studente1.cambia_scuola("Liceo Scientifico") 
studente1.saluta()  
studente2.saluta()  