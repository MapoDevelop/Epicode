print("Stampa numeri da 1 a 10")
for i in range(1, 11):
    print(i)
print("####################")

print("Stampa numeri pari da 1 a 20")
for i in range(2, 21, 2):
    print(i)

print("####################")

print("Stampa ogni lettera della parola 'Python'")
parola = "Python"
for lettera in parola:
    print(lettera)

print("####################")

print("Somma dei numeri da 1 a 100")
somma = 0
for i in range(1, 101):
    somma += i
    print("Somma parziale:", somma)
print("Somma totale:", somma)

print("####################")


n = int(input("Inserisci un numero: "))
print(f"Stampa tabellina del numero {n}")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("####################")

print(f"Stampa il numero fattoriale del numero {n} (che hai inserito prima)")
fattoriale = 1
for i in range(1, n + 1):
    fattoriale *= i
print(f"Il fattoriale di {n} è {fattoriale}")

print("####################")

print("Conta le vocali in una parola")
parola = input("Inserisci una parola: ").lower() 
vocali = "aeiou"
conteggio = 0
for lettera in parola:
    if lettera in vocali:
        conteggio += 1
print(f"Il numero di vocali nella parola '{parola}' è: {conteggio}")

print("####################")

print("Stampa una matrice 3x3")
for i in range(3):
    for j in range(3):
        print(f"{i+1},{j+1}", end="  ")
    print()

print("####################")

print("stampa i numeri da uno a 10 saltando il numero 5")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

print("####################")

print("stampa i numeri da uno a 10 fermandoti al numero 7")
for i in range(1, 11):
    if i == 8:
        break
    print(i)