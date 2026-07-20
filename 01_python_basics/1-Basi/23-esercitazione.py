nomi = {"Alice", "Bob", "Charlie", "Diana", "Eve"}
nomi2 = {"Frank", "Grace", "Heidi", "Ivan", "Judy"}

print("Nomi nel primo insieme:", nomi)
print("Nomi nel secondo insieme:", nomi2)

print("Unione dei due insiemi:", nomi | nomi2)
print("Intersezione dei due insiemi:", nomi & nomi2)
print("Differenza tra il primo e il secondo insieme:", nomi - nomi2)
print("Differenza tra il secondo e il primo insieme:", nomi2 - nomi)
print("Differenza simmetrica tra i due insiemi:", nomi ^ nomi2)
print("Totale unici nomi:", len(nomi | nomi2))

print("############################################")

import random
print("Generazione di una libreria di numeri casuali tra 1 e 100")
numeri_casuali = [random.randint(1, 100) for _ in range(10)]
print("Numeri casuali generati:", numeri_casuali)

print("#############################################")

print("Generazione di conteggio delle occorrenze di parole in un testo")
testo = "Cantami o diva del Pelide Achille l'ira funesta che infiniti addusse lutti agli Achei, molte anzi tempo all'Orco generose travolse alme d'eroi, e di cani e d'augelli orrido pasto lor salme abbandonò (così di Giove l'alto consiglio s'adempì), da quando primamente disgiunse aspra contesa il re de' prodi Atride e il divo Achille."
parole = testo.replace(",", "").replace(".", "").replace("'", "").split()
conteggio_parole = {}
for p in parole:
    conteggio_parole[p] = conteggio_parole.get(p, 0) + 1
print("Testo originale:", testo)
print("Conteggio delle occorrenze delle parole:", conteggio_parole)

print("#############################################")

print("Invertire chiave e valore in un dizionario")
dizionario = {"a": 1, "b": 2, "c": 3}
dizionario_invertito = {v: k for k, v in dizionario.items()}
print("Dizionario originale:", dizionario)
print("Dizionario invertito:", dizionario_invertito)

print("#############################################")

print("Creazione di un dizionario da due liste")
chiavi = ["nome", "cognome", "eta"]
valori = ["Alice", "Rossi", 25]
dizionario = dict(zip(chiavi, valori))
print("Dizionario creato:", dizionario)

print("#############################################")

print("Raggruppare parole per lunghezza")
parole = ["casa", "albero", "gatto", "cane", "elefante", "topo"]
gruppi = {}
for parola in parole:
    gruppi.setdefault(len(parola), []).append(parola)
print("Parole raggruppate per lunghezza:", gruppi)

print("#############################################")

print("Quanta frequenza sono ripetuti i caratteri in un testo")
testo = "Il gatto e il cane sono amici. Il gatto gioca con il cane."
frequenze = {}
for carattere in testo.replace(" ", "").replace(".", "").replace(",", "").lower():
    frequenze[carattere] = frequenze.get(carattere, 0) + 1
print("Frequenza dei caratteri nel testo:", frequenze)

print("#############################################")