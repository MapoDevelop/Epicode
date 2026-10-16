import pandas as pd
import numpy as np
from datetime import datetime

# Esercizio 1 - Nomi
# Crea una colonna si stringhe con nomi sporchi (spazi e maiuscole casuali)
# Pulisci i nomi

# Esercizio 3 - Date
# Crea delle date e calcola l'età

dati = {'nomi': ['MarIo giuLio  ',' giuSeppe   ','  GioGio'],'birthday':['24.05.2010','20.10.2017','23.05.1930']}
df = pd.DataFrame(dati)

df['nomi'] = df['nomi'].str.strip().str.title()
df['birthday'] = pd.to_datetime(df['birthday'], format='%d.%m.%Y', dayfirst=True)

oggi = datetime.now()
compleanno_passato = (df['birthday'].dt.month < oggi.month) | ((df['birthday'].dt.month == oggi.month) & (df['birthday'].dt.day <= oggi.day))
df['età'] = oggi.year - df['birthday'].dt.year - (~compleanno_passato).astype(int)

print(df)


# Esercizio 3 - Date
date = pd.date_range(start='2026-09-01', end='2026-10-31', freq='D')
df_date = pd.DataFrame({
    'Data':date,
    'Vendite': np.random.randint(1_000,5_000,len(date))
})

print(df_date)

print('Media settimanale:')
media_settimanale = df_date.resample("W", on="Data")["Vendite"].mean()
print(media_settimanale)

massimo_mensile = df_date.resample("ME", on="Data")['Vendite'].max()
print('Massimale mensile')
print(massimo_mensile)

df_date['Somma Cumulativa'] = df_date['Vendite'].cumsum()
print('Somma cumulativa:')
print(df_date)