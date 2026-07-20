# Crea una serie di date (30 giorni consecutivi)
# Genera valori casuali associati alle date.
# Crea un DataFrame con indice temporale.
# Fai un grafico a linea con i valori nel tempo.

import pandas as pd
import numpy as np

# Crea una serie di date (30 giorni consecutivi)
date = pd.date_range(start='2026-07-20', periods=30, freq='D') # Crea un intervallo di date a partire dal 20 luglio 2026, per 30 giorni consecutivi

# Genera valori casuali associati a date
np.random.seed(int(date[0].timestamp()))  # Imposta il seed basato sulla prima data
values = np.random.randint(1, 101, size=len(date)) # Genera valori casuali tra 1 e 100, il numero dei valori dipende quanti numeri ha date

# Crea un DataFrame con indice temporale
df = pd.DataFrame({'Date': date, 'Value': values})

# Crea un grafico a linea con i valori nel tempo
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5)) # crea il grafico con dimensioni personalizzate
# Date come asse x e valori come asse y, con marker e linee
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='b')
plt.title('Valori casuali nel tempo') # Titolo del grafico 
plt.xlabel('Data') # Etichetta dell'asse x
plt.ylabel('Valore') # Etichetta dell'asse y
plt.xticks(rotation=45) # Ruota le etichette dell'asse x per una migliore leggibilità
plt.grid() # Aggiunge una griglia al grafico
plt.tight_layout() # Ottimizza il layout del grafico per evitare sovrapposizioni
plt.show() # Mostra il grafico
