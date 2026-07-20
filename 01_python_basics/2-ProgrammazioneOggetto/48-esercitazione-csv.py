# Creo un file csv

import csv

# Creo un file CSV con i dati degli studenti
with open("studenti.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["NOME", "ETA", "CORSO"])
    writer.writerow(["Mario Rossi", 15, "Informatica"])
    writer.writerow(["Luigi Bianchi", 16, "Matematica"])
    writer.writerow(["Anna Verdi", 19, "Fisica"])
    writer.writerow(["Giulia Neri", 17, "Informatica"])
    writer.writerow(["Paolo Gialli", 21, "Chimica"])


## Lettura in forma di dizionario
with open("studenti.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"NOME: {row['NOME']}, ETA: {row['ETA']}, CORSO: {row['CORSO']}")

# Filtro i risultati
with open("studenti.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("\nStudenti iscritti al corso di Informatica:")
    for row in reader:
        if row["CORSO"] == "Informatica":
            print(f"NOME: {row['NOME']}, ETA: {row['ETA']}, CORSO: {row['CORSO']}")

# Creare un nuovo file CSV con i dati filtrati per studenti maggiorenni
with open("studenti.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    with open("maggiorenni.csv", mode="w", newline="", encoding="utf-8") as new_file:
        writer = csv.DictWriter(new_file, fieldnames=["NOME", "ETA", "CORSO"])
        writer.writeheader()
        for row in reader:
            if int(row["ETA"]) >= 18:
                writer.writerow(row)

print("\nFile 'maggiorenni.csv' creato con successo!")
with open("maggiorenni.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"NOME: {row['NOME']}, ETA: {row['ETA']}, CORSO: {row['CORSO']}")