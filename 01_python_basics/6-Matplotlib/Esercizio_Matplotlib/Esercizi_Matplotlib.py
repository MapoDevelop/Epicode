# Hai a disposizione dei dati fittizzi sulle vendite mensili di un negozio
# e sulle caratteristiche dei clienti.
# L'andamento delle vendite nel tempo.
# La distribuzione delle età dei clienti.
# La relazione tra età e spesa media dei clienti.
# Un confronto tra più grafici con subplots.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Cartella dove si trova lo script
cartella_script = os.path.dirname(os.path.abspath(__file__))
# Leggo il file CSV con i dati vendite_negozio.csv presente nella stessa cartella dello script sotto la cartella input
data = pd.read_csv(os.path.join(cartella_script, 'input_esercizio', 'vendite_negozio.csv'))
# Visualizzo le prime righe del DataFrame
print(data.head())
# sommo le vendite mensili per ottenere il totale delle vendite
# ciclando sulla colonna mese
vendite_mensili = data.groupby('mese')['importo_speso'].sum()
print("vendite_mensili: ", vendite_mensili)

# Calcolo la spesa media per ogni fascia di età
spesa_media_per_eta = data.groupby('eta_cliente')['importo_speso'].mean()
print("spesa_media_per_eta: ", spesa_media_per_eta)


# Creazione del grafico dell'andamento delle vendite nel tempo
plt.figure(figsize=(10, 5))
plt.plot(vendite_mensili.index, vendite_mensili.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Vendite Mensili')
plt.xlabel('Mese')
plt.ylabel('Vendite')
plt.title('Andamento delle vendite nel tempo')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Creazione del grafico per la media delle vendite per fascia di età
plt.figure(figsize=(10, 5))
plt.bar(spesa_media_per_eta.index, spesa_media_per_eta.values, color='orange', label='Spesa Media')
plt.xlabel('Fascia di età')
plt.ylabel('Spesa media')
plt.title('Spesa media per fascia di età')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# Creazione dei due grafici in un unico subplot
fig, axs = plt.subplots(2, 1, figsize=(10, 10))
axs[0].plot(vendite_mensili.index, vendite_mensili.values, marker='o', linewidth=2, color='blue', linestyle='--', label='Vendite Mensili')
axs[0].set_xlabel('Mese')
axs[0].set_ylabel('Vendite')
axs[0].set_title('Andamento delle vendite nel tempo')
axs[0].legend()
axs[1].bar(spesa_media_per_eta.index, spesa_media_per_eta.values, color='orange', label='Spesa Media')
axs[1].set_xlabel('Fascia di età')
axs[1].set_ylabel('Spesa media')
axs[1].set_title('Spesa media per fascia di età')
axs[1].legend()
axs[1].grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()