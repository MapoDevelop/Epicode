print("Numeri da 1 a 5")
i = 1
while i <= 5:
    print(i)
    i += 1

print("Ciclo terminato")
print("####################")

# Numeri pari da 2 a 10
print("Numeri pari da 2 a 10")
i = 2
while i <= 10:
    print(i)
    i += 2

print("Ciclo terminato")
print("####################")

# Sommare i numeri da 1 a 100
print("Calcolo della somma dei numeri da 1 a 10")
i = 1
somma = 0

while i <= 10:
    somma += i
    i += 1
print("La somma dei numeri da 1 a 10 è:", somma)
print("####################")

# Stampa la tabellina di n
print("Tabellina di un numero")

n = int(input("Inserisci un numero: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
print("####################")

print("Somma dei numeri")
n = int(input("Inserisci un numero ( inserisci 0 per uscire): "))

somma = 0
while n != 0:
    somma += n
    n = int(input("Inserisci un numero ( inserisci 0 per uscire): "))
print("La somma dei numeri inseriti è:", somma)
print("####################")

print("Indovina il numero segreto")
import random
numero_segreto = random.randint(1, 100)
tentativo = 0
while tentativo != numero_segreto:
    tentativo = int(input("Indovina il numero segreto (tra 1 e 100): "))
    if tentativo < numero_segreto:
        print("Troppo basso! Riprova.")
    elif tentativo > numero_segreto:
        print("Troppo alto! Riprova.")

print("Congratulazioni! Hai indovinato il numero segreto:", numero_segreto)

print("####################")

print("Stampa numeri da 1 a 15")
i = 1
while i <= 15:
    print(i)
    i += 1

print("Ciclo terminato")
print("####################")

print("Calcola la somma delle cifre di un numero")
numero = int(input("Inserisci un numero: "))
somma_cifre = 0

cifre = list(str(numero))
for cifra in cifre:
    somma_cifre += int(cifra)
    print("Cifra:", cifra, "Somma parziale:", somma_cifre)

print("La somma delle cifre del numero inserito è:", somma_cifre)
print("####################")
