# Importazioni
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

np.random.seed(42)  # per risultati riproducibili

#### Parte1 - Variabili 
#  Definisco le variabili:
nome : str = 'Mario Rossi'
eta : int = 30
saldo_conto : float = 3560.0
is_VIP : bool = True
# Definisco le destinazioni in una lista
destinazioni : list = ['Parigi', 'Malta', 'Giappone', 'Messico', 'Roma','India', 'New York', 'Madagascar', 'Sud America']
# creo i prezzi
prezzo_medio : int = np.random.randint(100,1000, len(destinazioni))
# Creo un dizionario con le destinazioni e il prezzo medio di ognuna
tour : dict = dict(zip(destinazioni, prezzo_medio))

# Parte2 - Programmazione ad Oggetti
# Creo la classe Cliente
class Cliente: 
    # Inizializzo Cliente
    def __init__(self, nome, eta, vip):
        """
        Inizializzo Cliente 
        
        Args:
            nome (str): nome del cliente
            eta (int): età del cliente
            vip (bool): se il cliente è vip
        """
        self.nome : str = nome
        self.eta : int = eta
        self.vip : bool = vip
    
    # Metodo di stampa di cliente    
    def __str__(self):
        """
        Metodo per stampare Cliente

        Returns:
           str: stampo le informazioni di Cliente
        """
        return f"Il sig. {self.nome}, ha {self.eta} anni, {'è' if self.vip else 'non è'} un cliente VIP"
    
# Creo una classe Viaggio
class Viaggio:
    def __init__(self, destinazione, prezzo, giorni):
        """
        Informazioni sul viaggio

        Args:
            destinazione (str):luogo di destinzione del viaggio
            prezzo (float): prezzo del viaggio
            giorni (int): durata del viaggio in giorni
        """
        self.destinazione : str = destinazione
        self.prezzo : float = prezzo
        self.giorni : int = giorni

# Creo una classe Prenotazione
class Prenotazione:
    def __init__(self, cliente,viaggio):
        self.cliente = cliente
        self.viaggio = viaggio
    
    # creo una funzione di scontistica per i clienti vip
    def calcolo_prezzo(self):
        """
        Se il cliente è vip calcola il prezzo meno uno sconto del 10%

        Returns:
            int: prezzo finale, scontato se il cliente è vip
        """
        if self.cliente.vip:
            return self.viaggio.prezzo * 0.9
        return self.viaggio.prezzo 
    
    # Creo un metodo di stampa
    def __str__(self):
        return f"Il cliente {self.cliente.nome} ha prenotato un viaggio con destinazione {self.viaggio.destinazione} ad un prezzo finale {self.calcolo_prezzo()}"   
    
    # Creo un metodo con le informazioni complete
    def dettagli(self):
        return (
            f"Nome cliente: {self.cliente.nome} - "
            f"Età: {self.cliente.eta} - "
            f"Cliente vip? {'SI' if self.cliente.vip else 'NO'} - "
            f"Destinazione: {self.viaggio.destinazione} - {self.viaggio.giorni} giorni - "
            f"Prezzo {'scontato' if self.cliente.vip else ''} {self.calcolo_prezzo()}"
            )

cliente1 = Cliente("Mario Rossi", 30, True)


print(cliente1)
viaggio1 = Viaggio("Malta", 600.0, 7)
prenotazione1 = Prenotazione(cliente1,viaggio1)
print(prenotazione1)
print(prenotazione1.dettagli())

### NUMPY ####
# Genero un array Numpy di prenotazioni simulate
prenotazioni = np.round(np.random.uniform(200,2000, 100), 2)
print(f"Array di Numpy con 100 prenotazioni casuali:")
print(prenotazioni)

# creo una funzione per calcolare le statistiche
def statistiche(prenotazioni):
    media = np.mean(prenotazioni)
    num_max = np.max(prenotazioni)
    num_min = np.min(prenotazioni)
    deviazione = np.std(prenotazioni)
    sup_media = (prenotazioni > media).sum()
    percentuale = np.round((sup_media / len(prenotazioni)) * 100, 2)
    
    return media, num_max, num_min, deviazione, percentuale
    

# Richiamo la funzione statistiche
media, num_max, num_min, deviazione, percentuale = statistiche(prenotazioni)

print(f"Prezzo medio: {media}")
print(f"Prezzo massimo: {num_max} - Prezzo minimo: {num_min}")
print(f"Deviazione standard: {deviazione:.2f}")
print(f"Percentuale di prenotazioni sopra la media {percentuale}")


### PANDAS ###

n = 20

# creo altri clienti
cliente2 = Cliente("Luca Bianchi", 45, False)
cliente3 = Cliente("Anna Verdi", 27, True)
cliente4 = Cliente("Sara Neri", 33, False)
cliente5 = Cliente("Marco Blu", 52, True)
cliente6 = Cliente("Elena Gialli", 24, False)
cliente7 = Cliente("Paolo Rosa", 38, True)
cliente8 = Cliente("Giulia Viola", 29, False)

clienti_option = np.random.choice([cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8], n)
nomi_clienti = [c.nome for c in clienti_option]
destinazioni_random = np.random.choice(destinazioni, n)          # pesca a caso dalle 5 città
prezzi = np.random.choice(prenotazioni, n, replace=False)
giorni_partenza = np.random.randint(1, 31, n)                    # giorno del mese, 1-30
durata = np.random.randint(3, 15, n)                              # durata in giorni

df = pd.DataFrame({
    "Cliente": nomi_clienti,
    "Destinazione": destinazioni_random,
    "Prezzo": prezzi,
    "Giorno_Partenza": giorni_partenza,
    "Durata": durata,
})

# Calcolo l'incasso (scontato se vip)
df['Incasso'] = [
    Prenotazione(cliente, Viaggio(destinazione,prezzo,giorni)).calcolo_prezzo()
    for cliente, destinazione,prezzo,giorni in zip(clienti_option, df['Destinazione'], df['Prezzo'], df['Durata'])
]
print(f"Incasso totale: {np.sum(df['Incasso']):.2f}")

print(df)

# Calcolo l'incasso per ogni destinazione
incasso_medio = df.groupby("Destinazione")["Incasso"].mean()
print(f"Incasso medio per destinazione: ")
print(f"{incasso_medio.round(2)}")

# Calcolo la destinazione più veduta
top3 = df["Destinazione"].value_counts().head(3)
print(f"Destinazioni più vendute:")
print(f"{top3}")

## MATPLOTLIB

# Calcolo l'incasso per destinazione
incasso_destinazione = df.groupby("Destinazione")["Incasso"].sum()

# Creo un grafico a barre 
# per l'incasso di ogni destinazione
plt.figure(figsize=(10,5))
plt.bar(incasso_destinazione.index, incasso_destinazione.values, label='Incassi per destinazione')
plt.title("Incasso per destinazione")
plt.xlabel("Destinazione")
plt.ylabel("Incasso (€)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Calcolo l'incasso giornaliero
incasso_giornaliero = df.groupby("Giorno_Partenza")["Incasso"].sum()
# Creo un grafico a linee 
# per l'andamento giornaliero degli incassi
plt.figure(figsize=(10,5))
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Incassi giornalieri')
plt.xlabel('Giorno')
plt.ylabel('Incasso')
plt.title('Andamento delle vendite giornaliere')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Calcolo le vendite per destinazione
vendite_destinazione = df["Destinazione"].value_counts()

# Creo un grafico a torta
# che mostri la percentuale di vendite
# di ciascuna destinazione
plt.figure(figsize=(10,5))
plt.pie(vendite_destinazione.values, labels=vendite_destinazione.index, autopct="%1.2f%%")
plt.title('Percentuale delle vendite per Destinazione')
plt.legend()
plt.show()

## Parte6
# Raggruppo i viaggi per categorie
categorie: dict = {
    'Parigi': 'Europa',
    'Malta': 'Europa',
    'Roma': 'Europa',
    'Giappone': 'Asia',
    'India': 'Asia',
    'Messico': 'America',
    'New York': 'America',
    'Sud America': 'America',
    'Madagascar': 'Africa'
}

# Aggiungo al Dataframe la categoria
df["Categoria"] = df["Destinazione"].map(categorie)
# Legge dove ci sono le città e inserisce Europa quando trova Parigi

incasso_categoria= df.groupby("Categoria")["Incasso"].sum()
durata_media_categoria = df.groupby("Categoria")["Durata"].mean()

# Cartella dove si trova lo script
cartella_script = os.path.dirname(os.path.abspath(__file__))
#salvataggio del file nella cartella dello script
df.to_csv(os.path.join(cartella_script,"prenotazioni_analizzate.csv"), index=False)

## Parte 7 
# Funzione per calcolare i clienti
def top_clienti(df,n):
    """
    Restituisce gli n clienti con più prenotazioni

    Args:
        df (DataFrame): dabella delle prenotazioni
        n (int): numero dei clienti da restituire
    """
    return df["Cliente"].value_counts().head(n)

# Chiedo quanti clienti vuole vedere l'utente
n_clienti = int(input("Quanti clienti vuoi vedere? "))
# Calcolo quali siano i clienti con più prenotazioni
print(top_clienti(df,n_clienti))

#Creo un grafico combinato
fig,ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
# Grafico1 a barre con incasso medio per categoria
incasso_medio_categoria = df.groupby("Categoria")["Incasso"].mean()
ax1.bar(incasso_medio_categoria.index, incasso_medio_categoria.values, color='orange', label='Incasso Medio per Categoria')
ax1.set_xlabel('Categoria')
ax1.set_ylabel('Incasso medio (€)')
ax1.set_title('Valori Medi per Categoria')
ax1.grid(True, linestyle='--', alpha=0.7)

# Grafico2 linea con durata media per categoria
ax2.plot(durata_media_categoria.index, durata_media_categoria.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Durata Media per Categoria')
ax2.set_ylabel('Durata media (giorni)')
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper right')
plt.tight_layout()
plt.show()