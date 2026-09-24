import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta # per gestire le date
import csv

np.random.seed(42) # Imposto un seme per i numeri random

#  Imposto la cartella per non avere problemi di salvataggio
cartella = os.path.dirname(os.path.abspath(__file__))

cartella_dati = os.path.join(cartella, 'data') # cartella per gli output

### Dataset base

# Creo il le variabli
negozi_option = ["Milano","Roma", "Napoli", "Bologna", "Torino"]
prodotti_option = {
    "Smartphone": "Elettronica",
    "Laptop": "Informatica",
    "TV": "Elettrodomestici",
    "Tablet": "Informatica",
    "Smartwatch": "Dispositivo indossabile"
}

rows = []
start_date = datetime.now()

# Creo i dati randomizzati
for i in range(30): # Cicla su tutte le 30 righe
    data = (start_date + timedelta(days=(np.random.randint(-365, 0)))).strftime("%Y-%m-%d") # Creazione data random da oggi a un anno
    negozio = np.random.choice(negozi_option) # Scelta del negozio random
    prodotto = np.random.choice(list(prodotti_option.keys())) # Scelta del prodotto random
    categoria = prodotti_option[prodotto] # Scelta della categoria associata al prodotto random
    quantita = np.random.randint(1,100) # Quantità random
    prezzo_unitario = np.round(np.random.uniform(50.0, 2000.0),2) # Prezzo random
    
    rows.append([data,negozio,prodotto,categoria,quantita,prezzo_unitario]) # Aggiunta delle righe

# Crea il file    
with open(os.path.join(cartella_dati,"vendite.csv"), "w",newline="", encoding="utf-8") as file:
    writer = csv.writer(file) # Definisce il writer
    writer.writerow(["Data", "Negozio", "Prodotto", "Categoria", "Quantità", "Prezzo_unitario"]) # Crea la prima riga
    writer.writerows(rows) # Aggiunge le righe randomizzate
    
print("File vendite.csv generato con successo!")

# Creo il dataframe dal file
df = pd.read_csv(os.path.join(cartella_dati,"vendite.csv")) 
    
print(df.head(5)) # Visualizzo le prime 5 righe
print(df.shape) # Dati delle righe e colonne
df.info() # Informazioni del dataframe

# Creo la colonna Incasso
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

print(f"L'incasso totale è: {df['Incasso'].sum():.2f}")
print("L'incasso per negozio è:")
print(df.groupby("Negozio")["Incasso"].sum().round(2))
print("L'incasso medio per negozio è:")
print(df.groupby("Negozio")["Incasso"].mean().round(2))

# Seleziono i tre prodotti più venduti
top3 = df.groupby("Prodotto")["Quantità"].sum().sort_values(ascending=False).head(3)
print(f"I prodotti più venduti sono: \n{top3}")

# Seleziono L'incasso medio per prodotto su ogni negozio
print("Incasso medio del prodotto in ogni negozio:")
print(df.groupby(["Negozio","Prodotto"])["Incasso"].mean().round(2))

# Estraggo la colonna Quantità come array Numpy
quantita_np = df["Quantità"].to_numpy()

# Creo le statistiche
def statistiche(colonna):
    media = float(np.mean(colonna))
    minimo = float(np.min(colonna))
    massimo = float(np.max(colonna))
    deviazione = float(np.std(colonna))
    percentuale = float(np.round(((colonna > media).sum() / len(colonna)) * 100, 2))
    
    return {
        "media": media, 
        "minimo" : minimo, 
        "massimo" : massimo, 
        "deviazione" : deviazione, 
        "percentuale" : percentuale
    }

print(statistiche(quantita_np))

# Creo l'array D2 con Quantità e prezzo unitario
array_np = df[["Quantità","Prezzo_unitario"]].to_numpy()

# Calcolo per ogni riga l'incasso
incasso_np = array_np[:,0] * array_np[:,1]

# Confronto i risultati con la colonna Incasso del DataFrame
confronto = np.allclose(incasso_np, df["Incasso"])

# Stampo i valori
print("Array NumPy 2D: ")
print(array_np)
print("\nIncasso calcolato con NumPy")
print(incasso_np)
print("\nConfronto con la colonna Incasso del DataFrame")
print(confronto)

# Creo il grafico a barre: incasso totale per ogni negozio
incasso_negozio = df.groupby("Negozio")["Incasso"].sum()
plt.figure(figsize=(10,5))
plt.bar(incasso_negozio.index, incasso_negozio.values, label='Incassi per ogni negozio')
plt.title("Incasso per ogni negozio")
plt.xlabel("Negozi")
plt.ylabel("Incasso (€)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Creo il grafico a torta: percentuale di incassi per ciascun prodotto
vendite_prodotto_percentuale = df.groupby("Prodotto")["Incasso"].sum()
plt.figure(figsize=(10,5))
plt.pie(vendite_prodotto_percentuale.values, labels=vendite_prodotto_percentuale.index, autopct="%1.2f%%")
plt.title('Percentuale delle vendite per Prodotto')
plt.legend()
plt.show()

# Creo il grafico a linee: andamento giornaliero degli incassi totali
incasso_giornaliero = df.groupby("Data")["Incasso"].sum().sort_index()
plt.figure(figsize=(10,5))
plt.plot(incasso_giornaliero.index, incasso_giornaliero.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Incassi giornalieri')
plt.xlabel('Giorno')
plt.ylabel('Incasso')
plt.title('Andamento delle vendite giornaliere')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ANALISI AVANZATA
# Creo i valori delle nuove colonne
categoria_incasso_medio = df.groupby("Categoria")["Incasso"].mean()
categoria_quantita_media = df.groupby("Categoria")["Quantità"].mean()

# Creo il dataframe
new_df = pd.concat([categoria_incasso_medio, categoria_quantita_media], axis=1)
new_df.index.name = "Categoria"
# Aggiungo i titoli alle colonne
new_df.columns = ["Incasso Medio","Quantità Media"]
print("ANALISI AVANZATA")
print(new_df)

# Salvo il file
new_df.to_csv(os.path.join(cartella_dati, "vendite_analizzate.csv"))
print("File vendite_analizzate.csv salvato!")

# Creo un grafico combinato:
# Incasso Medio x Categoria - grafico a barre
# + linea della quantità media venduta

#Creo un grafico combinato
fig,ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
# Grafico1 a barre con incasso medio per categoria
ax1.bar(categoria_incasso_medio.index, categoria_incasso_medio.values, color='orange', label='Incasso Medio per Categoria')
ax1.set_xlabel('Categoria')
ax1.set_ylabel('Incasso medio (€)')
ax1.set_title('Valori Medi per Categoria')
ax1.grid(True, linestyle='--', alpha=0.7)

# Grafico2 linea quantità media venduta
ax2.plot(categoria_quantita_media.index, categoria_quantita_media.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Quantità Media per Categoria')
ax2.set_ylabel('Quantità media')
h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1 + h2, l1 + l2, loc='upper right')
plt.tight_layout()
plt.show()

# Creo una funzione che restituisca n prodotti che hanno fatto più incassi
def top_n_prodotti(n):
    """
    Restituisce gli n prodotti che hanno avuto più incassi

    Args:
        n (int): numero di prodotti da mostrare
    """
    incasso_prodotti = df.groupby("Prodotto")["Incasso"].sum()
    return incasso_prodotti.sort_values(ascending=False).head(n)

# Chiedo quanti prodotti vuole vedere l'utente
n_prodotti = int(input("Quanti prodotti vuoi vedere? "))
# Calcolo quali siano i prodotti con più incassi
print(top_n_prodotti(n_prodotti))