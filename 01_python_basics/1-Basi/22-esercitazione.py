# Ordinare una lista di numeri per secondo elemento
print("Ordinare una lista di tuple per il secondo elemento")
tuples = [(1, 3), (2, 2), (4, 1), (3, 4)]
print("Lista originale:", tuples)
ordinata = sorted(tuples, key=lambda x: x[1])
print("Lista ordinata per secondo elemento:", ordinata)

print("############################################")

print("Tupla con i numeri pari da un'altra tupla")
tupla = (1, 2, 3, 4, 5, 6)
tupla_pari = tuple(x for x in tupla if x % 2 == 0)
print("Tupla originale:", tupla)
print("Tupla con i numeri pari:", tupla_pari)

print("############################################")

print("Invertire una tupla")
tupla_invertita = tuple(reversed(tupla))
print("Tupla originale:", tupla)
print("Tupla invertita:", tupla_invertita)

print("############################################")  

print("Convertire una stringa in caratteri unici")
stringa = "programmazione"
caratteri_unici = set(stringa)
print("Stringa originale:", stringa)
print("Caratteri unici:", caratteri_unici)

print("############################################")

print("Zippare due liste in una lista di tuple")
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']
zipped = list(zip(lista1, lista2))
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Liste zippate:", zipped)

print("############################################")

print("Differenza simmetrica di due o più set")
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = {3, 4, 5}
differenza_simmetrica = set1 ^ set2 ^ set3
print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)
print("Differenza simmetrica:", differenza_simmetrica)

print("############################################")

print("Filtra parole uniche in una frase")
frase = "Questa è una frase di esempio con parole ripetute, questa frase serve per testare il filtro delle parole uniche."
parole_uniche = set(frase.split())
print("Frase originale:", frase)
print("Parole uniche:", parole_uniche)

print("############################################")

print("Unione di set da lista di liste")
liste = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]
unione_set = set().union(*map(set, liste))
print("Liste originali:", liste)
print("Unione dei set:", unione_set)