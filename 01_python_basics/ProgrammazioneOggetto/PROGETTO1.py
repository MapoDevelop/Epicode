"""
Parte 1 - Variabili e tipi di dati

Dichiarare e stampare alcune variabili di esempio:

Titolo di un libro (stringa)

Numero di copie disponibili (intero)

Prezzo medio di un libro (float)

Stato "disponibile/non disponibile" (booleano)
(Esempio: titolo = "Il Signore degli Anelli", copie = 5, ecc.)

Parte 2 - Strutture dati

Creare una lista con almeno 5 titoli di libri.

Creare un dizionario che mappi il titolo del libro al numero di copie disponibili.

Creare un insieme (set) che contenga tutti gli utenti registrati alla biblioteca.

Parte 3 - Classi e OOP

Creare una classe Libro con attributi:

titolo

autore

anno

copie_disponibili

Aggiungere un metodo info() che restituisca una stringa descrittiva del libro.

Creare una classe Utente con attributi:

nome

età

id_utente

Aggiungere un metodo scheda() che stampi i dati dell’utente.

Creare una classe Prestito che colleghi un Utente a un Libro e contenga:

utente (oggetto Utente)

libro (oggetto Libro)

giorni (numero di giorni del prestito)

Aggiungere un metodo dettagli() che stampi tutte le informazioni sul prestito.

Parte 4 - Funzionalità

Creare una funzione presta_libro(utente, libro, giorni) che:

Verifichi se il libro ha almeno 1 copia disponibile

Se sì → riduca il numero di copie e crei un nuovo oggetto Prestito

Se no → stampi un messaggio di errore

Simulare almeno 3 prestiti con utenti e libri diversi

Stampare a video:

• L’elenco aggiornato delle copie disponibili per ciascun libro
• I dettagli di ogni prestito effettuato
""" 

### VARIABILI E TIPI DI DATI
titolo: str = "Il Signore degli Anelli"
copie: int = 5
prezzo_medio: float = 15.99
disponibile: bool = True

### STRUTTURE DATI
lista_libri: list = ["Il Signore degli Anelli", "1984", "Il Piccolo Principe", "Harry Potter e la Pietra Filosofale", "Il Codice Da Vinci"]

dizionario_copie: dict = {
    "Il Signore degli Anelli": 5,
    "1984": 3,
    "Il Piccolo Principe": 2,
    "Harry Potter e la Pietra Filosofale": 4,
    "Il Codice Da Vinci": 1
}

insieme_utenti: set = {"Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"}

### CLASSI E OOP
class Libro:
    def __init__(self, titolo: str, autore: str, anno: int, copie_disponibili: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.copie_disponibili = copie_disponibili

    def info(self) -> str:
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Copie disponibili: {self.copie_disponibili}"
    

class Utente:
    def __init__(self, nome: str, eta: int, id_utente: int):
        self.nome = nome
        self.eta = eta
        self.id_utente = id_utente

    def scheda(self) -> None:
        print(f"Nome: {self.nome}, Età: {self.eta}, ID Utente: {self.id_utente}")

class Prestito:
    def __init__(self, utente: Utente, libro: Libro, giorni: int):
        self.utente = utente
        self.libro = libro
        self.giorni = giorni

    def dettagli(self) -> None:
        print(f"Utente: {self.utente.nome}, Libro: {self.libro.titolo}, Giorni: {self.giorni}")

    ### FUNZIONALITÀ
    def presta_libro(self, utente, libro, giorni):
        # verifica se c'è almeno una copia
        try:
            if libro.copie_disponibili >= 1:
                libro.copie_disponibili -= 1
                # crea un nuovo oggetto Prestito
                prestito = Prestito(utente, libro, giorni)
                return prestito
            else:
                print(f"Errore: Il libro '{libro.titolo}' non è disponibile.")
                return None
        except AttributeError:
            print("Errore: Oggetto libro non valido.")
            return None
        
# Inizializzazione di alcuni oggetti Libro e Utente per la simulazione dei prestiti
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1954, 0)
libro2 = Libro("1984", "George Orwell", 1949, 3)
utente1 = Utente("Alice", 30, 1)
utente2 = Utente("Bob", 25, 2)
utente3 = Utente("Charlie", 35, 3)

# Stampa elenco aggiornato delle copie disponibili per ciascun libro
print("\nElenco aggiornato delle copie disponibili:")
print(f"{libro1.titolo}: {libro1.copie_disponibili} copie disponibili")
print(f"{libro2.titolo}: {libro2.copie_disponibili} copie disponibili")

# Simulazione di prestiti
prestito1 = Prestito(utente1, libro1, 14)
prestito2 = Prestito(utente2, libro2, 7)
prestito3 = Prestito(utente3, libro1, 21)
print("Dettagli Prestito 1:")
prestito1.dettagli()
print("Dettagli Prestito 2:")
prestito2.dettagli()
print("Dettagli Prestito 3:")
prestito3.dettagli()

print("\nCreazione di un oggetto Prestito tramite la funzione presta_libro")
print("Prestito 4: Alice prende in prestito 'Il Signore degli Anelli' per 10 giorni")
prestito4 = Prestito.presta_libro(Prestito, utente1, libro1, 10)
if prestito4:
    print("\nDettagli Prestito 4:")
    prestito4.dettagli()
    print(f"{libro1.titolo}: {libro1.copie_disponibili} copie disponibili")
print("\nPrestito 5: Alice prende in prestito '1984'")
prestito5 = Prestito.presta_libro(Prestito, utente1, libro2, 10)
if prestito5:
    print("Dettagli Prestito 5:")
    prestito5.dettagli()
    print(f"{libro2.titolo}: {libro2.copie_disponibili} copie disponibili")

# Stampa elenco aggiornato delle copie disponibili per ciascun libro
print("\nElenco aggiornato delle copie disponibili:")
print(f"{libro1.titolo}: {libro1.copie_disponibili} copie disponibili")
print(f"{libro2.titolo}: {libro2.copie_disponibili} copie disponibili")