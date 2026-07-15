# Crea una classe Appunti che salvi in un file ogni riga scritta dall'utente
# aggiungi un metodo mostra() che stampi il contenuto del file.
# Estendi la classe con un metodo cancella() che svuoti il file.

import datetime


class Appunti:
    def __init__(self, nome_file):
        self.nome_file = nome_file

    def scrivi(self, messaggio):
        # Prima riga di intestazione con DATA;MESSAGGIO
        try:
            with open(self.nome_file, "r") as f:
                prima_riga = f.readline()
        except FileNotFoundError:
            prima_riga = ""

        with open(self.nome_file, "a") as f:
            if not prima_riga:
                f.write("DATA;MESSAGGIO\n")
            f.write(messaggio + "\n")
        print(f"Messaggio salvato su {self.nome_file}")

    def mostra(self):
        with open(self.nome_file, "r") as f:
            self.dati = f.read()
        return self.dati
    
    def cancella(self):
        with open(self.nome_file, "w") as f:
            f.write("")
        print(f"Contenuto di {self.nome_file} cancellato")
    
messaggio = input("Inserisci gliappunti da salvare: ")
appunti = Appunti("appunti.csv")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
messaggio = f"{timestamp};{messaggio}"
appunti.scrivi(messaggio)
print("## APPUNTI SALVATI: ##")
print(appunti.mostra())
print("## CANCELLARE GLI APPUNTI? ##")
cancella = input("Scrivi 'si' per cancellare gli appunti: ")
if (cancella.lower() == "si")|(cancella.lower() == "sì"):
    appunti.cancella()
else:
    print("Gli appunti non sono stati cancellati.")
