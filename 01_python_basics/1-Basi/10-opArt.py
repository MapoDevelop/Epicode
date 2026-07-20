import math

# Chiedi all'utente quanti euro ha a disposizione
euro = float(input("Quanti euro hai a disposizione? ").replace(',', '.'))

# Chiedi il prezzo di un oggetto
# conerti la virgola in punto decimale per evitare errori di conversione
prezzo = float(input("Qual è il prezzo dell'oggetto che vuoi comprare? ").replace(',', '.'))

# Calcola quanti oggetti può comprare
# usa //  per calclare quante unità intere può comprare
quantita = int(euro // prezzo)

# Calcola quanti euro rimarranno dopo l'acquisto
resto = euro % prezzo

print(f"Puoi comprare {quantita} oggetti e ti rimarranno {resto:.2f} euro.")