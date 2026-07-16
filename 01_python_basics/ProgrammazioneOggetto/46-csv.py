import csv

class GestoreLibri:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def write(self, libro):
        try:
            with open(self.nome_file, "r") as f:
                prima_riga = f.readline()
        except FileNotFoundError:
            prima_riga = ""
        
        with open(self.nome_file, "a") as f:
            if not prima_riga:
                f.write("TITOLO;AUTORE;ANNO\n")
            f.write(libro + "\n")
        print("Libro inserito!")
 
    def read(self):
        libri = []
        try:
            with open(self.nome_file, "r") as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    libro = f"{row['TITOLO']} - {row['AUTORE']} - {row['ANNO']}"
                    libri.append(libro)
        except FileNotFoundError:
            print("File non trovato")
        
        return libri

    def filter_author(self, autore):
        libri_filtrati = []
        try:
            with open(self.nome_file, "r") as f:
                reader = csv.DictReader(f, delimiter=';')
                for row in reader:
                    if row['AUTORE'] == autore:
                        libro = f"{row['TITOLO']} - {row['AUTORE']} - {row['ANNO']}"
                        libri_filtrati.append(libro)
        except FileNotFoundError:
            print("File non trovato")

        return libri_filtrati

# Inizializzazione del file
libri = GestoreLibri("libri.csv")

# creo un menu per l'utente
while True:
    print("\nMenu:")
    print("1. Inserisci un nuovo libro")
    print("2. Visualizza tutti i libri")
    print("3. Filtra libri per autore")
    print("4. Esci")
    
    scelta = input("Scegli un'opzione: ")
    
    if scelta == "1":
        titolo = input("Inserisci il titolo del libro: ")
        autore = input("Inserisci l'autore del libro: ")
        anno = input("Inserisci l'anno di pubblicazione del libro: ")
        libro = f"{titolo};{autore};{anno}"
        libri.write(libro)
    elif scelta == "2":
        print("### Elenco dei libri: ###")
        for libro in libri.read():
            print(libro)
    elif scelta == "3":
        autore_da_filtrare = input("Inserisci l'autore da filtrare: ")
        for libro in libri.filter_author(autore_da_filtrare):
            print(libro)
    elif scelta == "4":
        break
    else:
        print("Opzione non valida") 