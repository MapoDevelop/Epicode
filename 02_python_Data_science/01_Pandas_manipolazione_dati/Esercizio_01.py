import pandas as pd
import matplotlib.pyplot as plt

# La richiesta dell'esercizio è di aggiungere delle funzionalità al codice mostrato in lezione
# Creiamo un dataset di esempio
dati = {'Settimana': [1, 2, 3, 4, 5, 6],
'Vendite': [250, 300, 400, 350, 450, 500]}

df = pd.DataFrame(dati)

# Calcoliamo la media delle vendite
media_vendite = df['Vendite'].mean()
print("Media vendite: ", media_vendite)

# Calcolo la settimana con vendite massime
top_week = df.loc[df['Vendite'].idxmax(),'Settimana']
top_sales = df['Vendite'].max()
print("Settimana con vendite  maggiori: ", top_week)

# Imposto la variabile del colore
# Rosso se le venditesono sotto la media, verde se sono sopra
colori = ['crimson' if sales < media_vendite else 'green' for sales in df['Vendite']]

# Creo un grafico combinato
fig,ax1 =plt.subplots(figsize=(10,5))
#Grafico1 a barre
ax1.bar(df['Settimana'], df['Vendite'], color=colori)
# Creo una linea media
ax1.axhline(media_vendite, color='red', linestyle='--', label='Media')
# Inserisco l'etichetta sopra la barra massima
ax1.annotate(f'Max: {top_sales}',
             xy=(top_week,top_sales),
             xytext=(top_week, top_sales+20),
             ha='center',
             arrowprops=dict(arrowstyle='->'))
ax1.set_xlabel('Settimana')
ax1.set_ylabel('Vendite')
ax1.set_title('Vendite settimanali')
ax1.grid(True, linestyle='--', alpha=0.7)

#Grafico2 - linea per visualizzare meglio il trend
ax1.plot(df['Settimana'],df['Vendite'], marker='o', linewidth=2, color='darkblue', linestyle='--', label='Trend')

plt.show()

