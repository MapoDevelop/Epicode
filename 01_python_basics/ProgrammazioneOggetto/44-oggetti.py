# Crea una classe Studente che chieda all'utente di inserire il nome e l'età
# e abbia un metodo presentati()
#Aggiungi a Studente un metodo __str_ che restituisca una stringa leggibile

class Student:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def presentati(self):
        return f"Piacere, sono {self.nome}, ho {self.eta} anni"
    
    def __str__(self):
        return f"Studente {self.nome} di {self.eta} è stato creato"
    
studente1 = Student("Marco", 23)
print(studente1)
print(studente1.presentati())

# Crea una classe Diario che salvi su file un messaggio passato dal'utente.
# Aggiungi un metodo che legga dal file e stampi i messaggi salvati.

class Diario:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def scrivi(self, messaggio):
        with open(self.nome_file, "a") as f:
            f.write(messaggio + "\n")
        print(f"Messaggio salvato su {self.nome_file}")

    def leggi(self):
        with open(self.nome_file, "r") as f:
            self.dati = f.read()
        return self.dati

messaggio = input("Inserisci un messaggio da salvare nel diario: ")
diario = Diario("diario.txt")
diario.scrivi(messaggio)
print(diario.leggi())
