import numpy as np
# Scenario reale
# Un centro di analisi mediche deve informatizzare parte della gestione dei pazienti, 
# dei medici e dei referti di laboratorio. Si richiede la progettazione 
# e la realizzazione di un programma in Python che permetta di gestire i dati in maniera strutturata, 
# utilizzando programmazione a oggetti (OOP) e la libreria NumPy per l’elaborazione numerica dei dati 
# clinici.

# Parte 1 – Variabili e Tipi di Dati
# Definire le variabili necessarie per rappresentare:
# - Nome, 
# - cognome e 
# - codice fiscale di un paziente (stringhe).
# - Età e 
# - peso del paziente (interi e float).
# - Lista delle analisi effettuate (lista di stringhe).

# Esempio:
# - nome = "Mario"
# - cognome = "Rossi"
# - eta = 45
# - peso = 78.5
# - analisi = ["emocromo", "glicemia", "colesterolo"]

# ➡️ Scrivere almeno 3 pazienti diversi.
paziente1 = {
    
    "nome" : "Mario",
    "cognome" : "Rossi",
    "codice_fiscale" : "RSSMRA80A01H501U",
    "eta" : 45,
    "peso" : 78.5,
    "analisi" : ["emocromo", "glicemia", "colesterolo"]
}

paziente2 = {
    "nome": "Luigi",
    "cognome": "Bianchi",
    "codice_fiscale": "BNCLGU85B02H501V",
    "eta": 38,
    "peso": 82.3,
    "analisi": ["emocromo", "glicemia", "trigliceridi"]
}

paziente3 = {
    "nome": "Giulia",
    "cognome": "Verdi",
    "codice_fiscale": "VRDGIL90C03H501W",
    "eta": 29,
    "peso": 65.0,
    "analisi": ["emocromo", "glicemia", "colesterolo", "trigliceridi"]
}

# Parte 2 – Classi e OOP
# Creare una classe Paziente con:Attributi: 
# - nome, 
# - cognome, 
# - codice_fiscale, 
# - eta, 
# - peso, 
# - analisi_effettuate.
# - Metodo scheda_personale() che restituisca una stringa con i dati principali del paziente.
class Paziente:
    def __init__(self, nome : str, cognome : str, codice_fiscale : str, eta : int, peso : float, analisi_effettuate : list, risultati_analisi : list):
        self.nome = nome
        self.cognome = cognome
        self.codice_fiscale = codice_fiscale
        self.eta = eta
        self.peso = peso
        self.analisi = [Analisi(tipo,risultato) for tipo, risultato in zip(analisi_effettuate, risultati_analisi)]
        self.risultati_analisi = np.array(risultati_analisi)

    def scheda_personale(self):
        return f"Nome: {self.nome}, Cognome: {self.cognome}, Codice Fiscale: {self.codice_fiscale}, Età: {self.eta}, Peso: {self.peso}, Analisi Effettuate: {', '.join([analisi.tipo for analisi in self.analisi])}"

    def __str__(self):
        return f"{self.nome} {self.cognome}"

# Parte 4 – Integrazione OOP + NumPy

# Aggiornare la classe Paziente inserendo un attributo risultati_analisi 
# che sia un array NumPy contenente i valori numerici delle analisi svolte.
# Creare un metodo statistiche_analisi() che calcoli:
# - Media dei valori
# - Minimo e massimo
# - Deviazione standard utilizzando NumPy.
    def statistiche_analisi(self):
        if self.risultati_analisi.size == 0:
            return "Nessun risultato di analisi disponibile."
        media = np.mean(self.risultati_analisi)
        minimo = np.min(self.risultati_analisi)
        massimo = np.max(self.risultati_analisi)
        deviazione_standard = np.std(self.risultati_analisi)
        return f"{self.nome} {self.cognome}: Statistiche Analisi - Media: {media}, Minimo: {minimo}, Massimo: {massimo}, Deviazione Standard: {deviazione_standard}"



# Creare una classe Medico con:Attributi: 
# - nome, 
# - cognome, 
# - specializzazione.
# - Metodo visita_paziente(paziente) che stampi quale medico sta visitando quale paziente.
class Medico:
    def __init__(self, nome, cognome, specializzazione):
        self.nome= nome
        self. cognome = cognome
        self.specializzazione = specializzazione

    def visita_paziente(self, paziente):
        return f"Il dottor {self.nome} {self.cognome} sta visitando il signor {paziente}"

# Creare una classe Analisi che contenga:
# - Tipo di analisi (es. glicemia, colesterolo).
# - Risultato numerico.
# - Metodo valuta() che stabilisca se il valore è nella norma (criteri inventati da voi).

class Analisi(Paziente):
    def __init__(self, tipo, risultato):
        self.tipo = tipo
        self.risultato =  risultato

    def valuta(self):
        # Criteri inventati
        if self.tipo ==  "glicemia":
            if 70<= self.risultato <= 100:
                return "Glicemia nella norma"
            elif self.risultato <70:
                return "Glicemia bassa"
            else:
                return "Glicemia alta"
        elif self.tipo == "colesterolo":
            if self.risultato < 200:
                return "Colesterolo nella norma"
            elif 200 <= self.risultato <= 239:
                return "Colesterolo borderline"
            else:
                return "Colesterolo alto"
        elif self.tipo == "pulsazioni":
            if 60 <= self.risultato <= 100:
                return "Pulsazioni nella norma"
            elif self.risultato < 60:
                return "Pulsazioni basse"
            else:
                return "Pulsazioni alte"
        elif self.tipo == "vitamina D":
            if 30 <= self.risultato <= 100:
                return "Vitamina D nella norma"
            elif self.risultato < 30:
                return "Vitamina D bassa"
            else:
                return "Vitamina D alta"
        elif self.tipo == "emocromo":
            if 12 <= self.risultato <= 16:
                return "Emocromo nella norma"
            elif self.risultato < 12:
                return "Emocromo basso"
            else:
                return "Emocromo alto"
        elif self.tipo == "ferro":
            if 60 <= self.risultato <= 170:
                return "Ferro nella norma"
            elif self.risultato < 60:
                return "Ferro basso"
            else:
                return "Ferro alto"
        elif self.tipo == "trigliceridi":
            if self.risultato < 150:
                return "Trigliceridi nella norma"
            elif 150 <= self.risultato <= 199:
                return "Trigliceridi borderline"
            else:
                return "Trigliceridi alti"
        else:
            return "Tipo di analisi non riconosciuto"

# Parte 5 – Applicazione completa
# Creare un piccolo programma principale (main) che:
# - Inserisca almeno 3 medici e 5 pazienti.
# - Ogni paziente deve avere almeno 3 risultati di analisi.
# - Stampi la scheda di ogni paziente.
# - Mostri quale medico visita quale paziente.
# - Stampi le statistiche delle analisi per ciascun paziente.

paziente1 = Paziente(
    nome="Mario",
    cognome="Rossi",
    codice_fiscale="RSSMRA80A01H501U",
    eta=45,
    peso=78.5,
    analisi_effettuate=["glicemia", "colesterolo", "pulsazioni"],
    risultati_analisi=np.array([98, 180, 105])
)

paziente2 = Paziente(
    nome="Luigi",
    cognome="Bianchi",
    codice_fiscale="BNCLGU85B02H501V",
    eta=38,
    peso=82.3,
    analisi_effettuate=["glicemia", "vitamina D", "emocromo"],
    risultati_analisi=np.array([85, 45, 14.2])
)

paziente3 = Paziente(
    nome="Giulia",
    cognome="Verdi",
    codice_fiscale="VRDGIL90C03H501W",
    eta=29,
    peso=65.0,
    analisi_effettuate=["colesterolo", "glicemia", "pulsazioni"],
    risultati_analisi=np.array([210, 115, 150])
)

paziente4 = Paziente(
    nome="Francesca",
    cognome="Rissa",
    codice_fiscale="RSSFNC92D04H501X",
    eta=32,
    peso=70.2,
    analisi_effettuate=["glicemia", "emocromo", "ferro"],
    risultati_analisi=np.array([90, 13.5, 90])
)

paziente5 = Paziente(
    nome="Giovanni",
    cognome="Neri",
    codice_fiscale="NRIGNN85E05H501Y",
    eta=40,
    peso=85.0,
    analisi_effettuate=["colesterolo", "trigliceridi", "glicemia"],
    risultati_analisi=np.array([250, 180, 105])
)

lista_pazienti = [paziente1, paziente2, paziente3, paziente4, paziente5]
print("---Schede dei pazienti:---")
for paziente in lista_pazienti:
    print(paziente.scheda_personale())

medico1 = Medico(
    nome="Alessandro",
    cognome="Neri",
    specializzazione="Cardiologia"
)

medico2 = Medico(
    nome="Francesca",
    cognome="Russo",
    specializzazione="Endocrinologia"
)

medico3 = Medico(
    nome="Giovanni",
    cognome="Ferrari",
    specializzazione="Neurologia"
)

print("---Visite Mediche:---")
print(medico1.visita_paziente(paziente1))
print(medico2.visita_paziente(paziente2))
print(medico3.visita_paziente(paziente3))

# Parte 3 – Uso di NumPy
# Supponiamo che il centro raccolga i risultati di un certo esame per 10 pazienti.
# Rappresentare i valori in un array NumPy.
# Calcolare con NumPy: media, valore massimo, valore minimo e deviazione standard.

## valori di glicemia per 10 pazienti


# creo valori random per 10 pazienti
np.random.seed(42)
glicemia = np.random.randint(60, 130, size=10)

print("Valori di glicemia dei 10 pazienti:", glicemia)
print("Media:", np.mean(glicemia))
print("Valore massimo:", np.max(glicemia))
print("Valore minimo:", np.min(glicemia))
print("Deviazione standard:", np.std(glicemia))

print("---Valutazione Analisi per Paziente:---")
for paziente in lista_pazienti:
    print(paziente.statistiche_analisi())



print("---Valutazione Analisi Specifica:---")

for oggetto_esame in paziente1.analisi:
    print(f"{paziente1}: {oggetto_esame.tipo}, {oggetto_esame.risultato}, {oggetto_esame.valuta()}")

for oggetto_esame in paziente2.analisi:
    print(f"{paziente2}: {oggetto_esame.tipo}, {oggetto_esame.risultato}, {oggetto_esame.valuta()}")

for oggetto_esame in paziente3.analisi:
    print(f"{paziente3}: {oggetto_esame.tipo}, {oggetto_esame.risultato}, {oggetto_esame.valuta()}")

for oggetto_esame in paziente4.analisi:
    print(f"{paziente4}: {oggetto_esame.tipo}, {oggetto_esame.risultato}, {oggetto_esame.valuta()}")

for oggetto_esame in paziente5.analisi:
    print(f"{paziente5}: {oggetto_esame.tipo}, {oggetto_esame.risultato}, {oggetto_esame.valuta()}")
