# Esercizio 1:

nome= input("Qual è il tuo nome? ")
eta= int(input("Quanti anni hai? "))
citta= input("In quale città vivi? ")

print("Il tuo nome è " + nome + ", hai " + str(eta) + " anni e vivi a " + citta + ".")

# Esercizio 2:
x = int(input("Inserisci un numero: "))
print("Il valore di x è:", x)
x = int(input("Inserisci un nuovo numero: "))
print("Il nuovo valore di x è:", x)

# Esercizio 3:
x = int(input("Inserisci il primo numero: "))
y = int(input("Inserisci il secondo numero: "))
print("La somma dei due numeri è:", x + y)

# Esercizio 4:
x = int(input("Inserisci il primo numero: "))
print("Il valore di x è:", x)
y = int(input("Inserisci il secondo numero: "))
print("Il valore di y è:", y)

x, y = y, x
print("Dopo lo scambio, x è:", x)
print("Dopo lo scambio, y è:", y)

# Esercizio 5:
base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza del rettangolo: "))
area = base * altezza
print("L'area del rettangolo è:", area)

# Esercizio 6:
a = float(input("Inserisci un numero intero: "))
b = float(input("Inserisci un numero decimale: "))
print("La somma di a e b è:", a + b)

# Esercizio 7:
x = float(input("Inserisci il primo numero: "))
y = float(input("Inserisci il secondo numero: "))
z = float(input("Inserisci il terzo numero: "))
media = (x + y + z) / 3
print("La media dei tre numeri è:", media)

# Esercizio 8:
s1 = "Mi piace: "
s2 = input("Inserisci qualcosa che ti piace: ")
print(s1 + s2)

# Esercizio 9:
print("Ciao!" * 3)

# Esercizio 10:
print("Esercizio 10: Booleani")
a = int(input("Inserisci un numero: "))
b = int(input("Inserisci un altro numero: "))
c = int(input("Inserisci un terzo numero: "))
print("a:", a)
print("b:", b)
print("c:", c)
print("a > b?", a > b)
print("b < c?", b < c)
print("a > c?", a > c)

# Esercizio 11:
x = 10
y = float(x)
print("Il valore di x è:", x)
print("Il valore di y è:", y)

# Esercizio 12:
n = input("Inserisci un numero intero: ")
s = str(n)
print("Il numero inserito è:", s)