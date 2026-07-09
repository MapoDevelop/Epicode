# Crea una classe Studente con attributi nome ed eta
# Istanzia due studenti e stampa i dati
# Aggiungi alla classe Studente un metodo presentati() che stampa "Ciao, sono [nome] e ho [eta] anni"
# Prova ad aggiungere un attributo al volo 
# a uno studente, ad esempio corso e stampalo

class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        print(f"Ciao, sono {self.nome} e ho {self.eta} anni")

studente1 = Studente("Mario", 20)
studente2 = Studente("Luigi", 22)

studente1.presentati() 
studente2.presentati() 

studente1.corso = "Informatica"
print(f"Sono {studente1.nome}, iscritto al corso {studente1.corso}")