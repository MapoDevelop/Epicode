# Scrivere un programma che analizzi un testo e calcoli le varie statisiche.

# Contare il numero di parole.

# Calcolare la frequenza di ogni parola.

# Estrarre le parole uniche usando un set.

# Mostrare le 5 parole più frequenti.

# Calcolare la lunghezza media delle parole.

# funzione per puliere il testo rimuovendo la punteggiatura e convertendo tutto in minuscolo
def pulisci_testo(testo):
    import string
    testo = testo.translate(str.maketrans("", "", string.punctuation))  # Rimuovi la punteggiatura
    return testo.lower()

# Contare il numero di parole
def conta_parole(testo):
    parole = testo.split()
    return len(parole)

# Calcolare la frequenza di ogni parola
def frequenza_parole(testo):
    parole = testo.split()
    frequenza = {}
    for parola in parole:
        frequenza[parola] = frequenza.get(parola, 0) + 1  #incrementa il conteggio della parola
    return frequenza

# Estrarre le parole uniche usando un set
def parole_uniche(frequenza):
    return set(frequenza.keys())

# Mostrare le 5 parole più frequenti
def parole_frequenti(frequenza, n=5):
    return sorted(frequenza.items(), key=lambda x: x[1], reverse=True)[:n] # ordina le parole in ordine decrescentee restituisce le prime n

# Calcolare la lunghezza media delle parole
def lunghezza_media(frequenza):
    totale_caratteri = sum(len(parola) * count for parola, count in frequenza.items())
    totale_parole = sum(frequenza.values())
    return totale_caratteri / totale_parole if totale_parole > 0 else 0

testo = "Ciao! Questo è un esempio di testo. Questo testo serve per testare le funzioni del programma. Ciao ciao!"

testo_pulito = pulisci_testo(testo)
print("Numero di parole: ", conta_parole(testo_pulito))

frequenza = frequenza_parole(testo_pulito)
print("Frequenza delle parole: ", frequenza)

print("Parole uniche: ", parole_uniche(frequenza))
print("5 parole più frequenti: ", parole_frequenti(frequenza))

print("Lunghezza media delle parole: ", round(lunghezza_media(frequenza), 2))
