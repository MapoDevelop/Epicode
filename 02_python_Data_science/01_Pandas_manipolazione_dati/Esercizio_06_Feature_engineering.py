import pandas as pd
import numpy as np

# Esercizio 1 - 
# Crea due colonne Larghezza e Lunghezza
# Cacola la colonna Area del rettangolo

dati = {
    'Larghezza': [2, 3, 4, 5],
    'Lunghezza': [5, 6, 7, 8]
}

df_rettangolo = pd.DataFrame(dati)

df_rettangolo["Area Rettangolo"] = df_rettangolo["Larghezza"] * df_rettangolo["Lunghezza"]

print(df_rettangolo)

# Esercizio 2
# Crea un Dataframe con Categorie e Valori
# Applica one-hot encoding alla colonna "Tipo"
dati = {
    'Tipo': ["A","B","C","B","C","A"],
    'Valore' : [30,56,38,28,19,65]
}

df_categorie = pd.DataFrame(dati)

df_encoded = pd.get_dummies(df_categorie, columns=['Tipo'], prefix='Tipo')

print(df_encoded)

# Esercizio 3
# Crea un dataframe con date giornaliere e valori casuali
# Estrai il giorno della settimana, mese differenza rispetto al giorno di prima

inizio = pd.Timestamp("2026-01-01")
giorni = np.random.randint(0,365,20)
date_random = inizio + pd.to_timedelta(giorni, unit="D")

df_date = pd.DataFrame({
    "Data":date_random,
    "Vendite":np.random.randint(1_000, 5_000, 20)
})

# Mette le date in ordine
df_date = df_date.sort_values("Data").reset_index(drop=True)

df_date["Giorno"] = df_date["Data"].dt.day_name()
df_date["Mese"] = df_date["Data"].dt.month_name()
df_date["Differenza"] = df_date["Vendite"].diff()

print(df_date)