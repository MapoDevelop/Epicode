print("Multipli di 3")
n = int(input("Inserisci un numero per vedere se è divisibile per tre: "))

if n%3 == 0:
    print("n è divisibile per 3")
else:
    print("n non è divisibile per 3")

print("#####################")

print("Voti")
voto = int(input("Inserisci il tuo voto: "))

if voto >= 18:
    print("Promosso")
else:
    print("Bocciato")

print("#####################")
print("Vocali e consonanti")
lettera = input("Inserisci una lettera: ").lower()

if lettera in "aeiou":
    print("La lettera è una vocale")
else:
    print("La lettera è una consonante")

print("#####################")
print("Positivo o negativo o zero")
numero = int(input("Inserisci un numero: "))

if numero > 0:
    print("Il numero è positivo")
elif numero < 0:
    print("Il numero è negativo")
else:
    print("Il numero è zero")

print("#####################")
print("Numero maggiore")

a,b,c = map(int, input("Inserisci tre numeri separati da spazio: ").split())

if a > b and a > c:
    print("Il numero maggiore è:", a)
elif b > a and b > c:
    print("Il numero maggiore è:", b)
else:
    print("Il numero maggiore è:", c)

print("#####################")
print("Prezzo del biglietto")

eta = int(input("Inserisci la tua età: "))
if eta < 12:
    prezzo = 5
elif eta < 65:
    prezzo = 10
else:
    prezzo = 7
print(f"Il prezzo del biglietto è: {prezzo} euro")


print("#####################")

print("Classificazione del triangolo")
a,b,c = map(int, input("Inserisci i tre lati del triangolo separati da spazio: ").split())

if a == b == c:
    print("Il triangolo è equilatero")
elif a == b or a == c or b == c:
    print("Il triangolo è isoscele")
else:
    print("Il triangolo è scaleno")