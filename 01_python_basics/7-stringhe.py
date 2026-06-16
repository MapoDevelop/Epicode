stringa = input("Inserisci una stringa: ")
stringa_inversa = stringa[::-1]

print("La stringa inversa è:", stringa_inversa)

if stringa == stringa_inversa:
    print("La stringa è un palindromo.")
else:
    print("La stringa non è un palindromo.")