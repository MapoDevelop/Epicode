# Esercizi sulle stringhe

# 1: Primo e ultimo carattere
testo = "Python"
print("##### Testo:", testo)
print("primo carattere:", testo[0])
print("ultimo carattere:", testo[-1])

# 2: Elborazione del testo
testo = "   Ciao, cOme  stAi?   "
testo = testo.upper()  # Converte tutto in maiuscolo
print("Testo in maiuscolo:", testo)
testo = testo.replace("  ", " ")  # Rimuove tutti gli spazi doppi
testo = testo.strip()  # Rimuove spazi iniziali e finali
testo = testo.lower()  # Converte tutto in minuscolo
print("Testo elaborato:", testo)

# 3: Contare le lettere
testo = "banana"
lettera = "a"
conteggio_a = testo.count(lettera)
print(f"Numero di '{lettera}' in '{testo}': {conteggio_a}")

# 4: Controllo se una parola inizia  o finisce con una certa lettera
testo = "Python è fantastico"
print("##### Testo:", testo)
print("Inizia con 'P':", testo.startswith("P"))
print("Finisce con 'o':", testo.endswith("o"))

# 5: Inverti stringa
testo = "Python"
print("##### Testo da invertire:", testo)
testo_invertito = testo[::-1]
print("Testo invertito:", testo_invertito)

# 6: Rimuovi spazi
testo = "   Ciao, come stai?   "    
print("##### Testo con spazi:", testo)
testo_senza_spazi = testo.strip()  # Rimuove spazi iniziali e finali
print("Testo senza spazi:", testo_senza_spazi)  

# 7: Duplica le prime tre lettere
testo = "Python"
print("##### Testo:", testo)
prime_tre_lettere = testo[:3]
testo_duplicato = prime_tre_lettere * 3
print("Testo con prime tre lettere duplicate:", testo_duplicato)