# Progetto – Analisi di Vendite in una Catena di Negozi

Di seguito trovi la traccia del progetto conclusivo del primo modulo.
Carica il tuo esercizio in questa sezione tramite l’opzione di upload con GitHub.

Il tuo progetto verrà valutato dal docente e riceverai una notifica con il feedback una volta completata la correzione.

---

## Scenario reale

Una catena di negozi di elettronica vuole analizzare i dati delle vendite per migliorare la gestione e capire l’andamento del mercato. I dati vengono raccolti giornalmente e comprendono informazioni su prodotti, quantità vendute, prezzo, incassi e negozi.

Si richiede di sviluppare un programma in Python che utilizzi:

- NumPy per elaborazioni numeriche veloci
- Pandas per la gestione e analisi di dataset
- Matplotlib per la visualizzazione dei dati in grafici

---

## Parte 1 – Dataset di base

Creare un file CSV chiamato **vendite.csv** con almeno **30 righe** che contenga le seguenti colonne:

1. Data (formato YYYY-MM-DD)
2. Negozio (stringa: es. Milano, Roma, Napoli…)
3. Prodotto (stringa: es. Smartphone, Laptop, TV…)
4. Quantità (intero)
5. Prezzo_unitario (float)

**Esempio riga:**

2023-09-01, Milano, Smartphone, 5, 499.99

---

## Parte 2 – Importazione con Pandas

Importare il file CSV in un DataFrame Pandas e stampare:

1. Le prime 5 righe (`head()`)
2. Il numero di righe e colonne (`shape`)
3. Le informazioni generali (`info()`)

---

## Parte 3 – Elaborazioni con Pandas

1. Aggiungere una colonna **Incasso** calcolata come `Quantità * Prezzo_unitario`.
2. Calcolare con Pandas:
   - l’incasso totale di tutta la catena
   - l’incasso medio per negozio
   - i 3 prodotti più venduti (in termini di quantità totale)
   - raggruppare i dati per **Negozio** e **Prodotto** e mostrare l’incasso medio

---

## Parte 4 – Uso di NumPy

Estrarre la colonna **Quantità** come array NumPy e calcolare:

- media
- minimo
- massimo
- deviazione standard
- percentuale di vendite sopra la media

**Esempio parziale:**

import numpy as np  
q = df["Quantità"].to_numpy()  
media = np.mean(q)  
massimo = np.max(q)

Creare un array NumPy 2D che contenga solo **Quantità** e **Prezzo_unitario** e calcolare per ogni riga l’incasso.  
Confrontare i risultati con la colonna _Incasso_ del DataFrame.

---

## Parte 5 – Visualizzazioni con Matplotlib

Creare i seguenti grafici:

1. Grafico a barre: incasso totale per ogni negozio.
2. Grafico a torta: percentuale di incassi per ciascun prodotto.
3. Grafico a linee: andamento giornaliero degli incassi totali della catena.

**Esempio parziale (grafico a barre):**

import matplotlib.pyplot as plt  
df.groupby("Negozio")["Incasso"].sum().plot(kind="bar")  
plt.show()

---

## Parte 6 – Analisi Avanzata

1. Creare una nuova colonna **Categoria** che raggruppi i prodotti in grandi famiglie (es. Smartphone e Laptop → Informatica, TV → Elettrodomestici).
2. Calcolare per ogni categoria:
   - incasso totale
   - quantità media venduta
3. Salvare il DataFrame aggiornato con le nuove colonne in un nuovo file **vendite_analizzate.csv**.

---

## Parte 7 – Estensioni (per i più bravi)

1. Creare un grafico combinato: incasso medio per categoria (grafico a barre) + linea della quantità media venduta.
2. Creare una funzione `top_n_prodotti(n)` che restituisca i n prodotti più venduti in termini di incasso totale.
