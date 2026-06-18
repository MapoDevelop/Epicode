# Scrivi un programma che:
# - Ha una variabile eta
# - Se eta è minore a 18 stampa "Sei minorenne"
# - Se eta è minore di 65 stampa "Sei maggiorenne"
# - Altrimenti stampa "Sei anziano"

eta = int(input("Inserisci la tua età: "))

if eta < 18:
    print("Sei minorenne")
elif eta < 65:
    print("Sei maggiorenne")
else:
    print("Sei anziano")