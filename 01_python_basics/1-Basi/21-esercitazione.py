import random
print("Somma dei numeri pari di una lista")

# crea dieci numeri random
numeri = [random.randint(1, 100) for _ in range(10)]
print("Numeri generati:", numeri)
somma_pari = sum(num for num in numeri if num % 2 == 0)
print("La somma dei numeri pari è:", somma_pari)

print("###########################")

print("Crea una lista senza duplicati ")
lista = [1, 2, 2, 3, 4, 4, 5]
lista_senza_duplicati = []

for n in lista:
    if n not in lista_senza_duplicati:
        lista_senza_duplicati.append(n)

print("Lista senza duplicati:", lista_senza_duplicati)

print("###########################")

print("Lista ruotata")
lista = [1, 2, 3, 4, 5]
k = 2  # numero di posizioni da ruotare
rotated_lista = lista[-k:] + lista[:-k]
print("Lista ruotata:", rotated_lista)

print("###########################")

print("Intersezione di due liste")
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
intersezione = [n for n in lista1 if n in lista2]
print("Intersezione:", intersezione)

print("###########################")

print("Converti una lista di tuple in un dizionario")
coppie = [("a", 1), ("b", 2), ("c", 3)]
dizionario = dict(coppie)
print("Dizionario:", dizionario)

print("###########################")

print("Somma di tutte le tuple in una lista")
tuple_lista = [(1, 2), (3, 4), (5, 6)]
somma_tuple = sum(sum(t) for t in tuple_lista)
print("Somma di tutte le tuple:", somma_tuple)

print("###########################")

print("Usare la tupla  con massimo e minimo")
tupla = tuple(random.randint(1, 100) for _ in range(10))
print("Tupla generata:", tupla)
massimo = max(tupla)
minimo = min(tupla)
print("Massimo:", massimo)
print("Minimo:", minimo)

print("###########################")