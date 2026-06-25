# Crea un dizionario che rappresenti uno studente con le seguenti informazioni: 
# nome, età e corso di studi. Poi stampa il dizionario.

# - Modifica il valore età
# - Aggiungi una nuova chiave "matricola"
# - Usa get() per recuperare un valore sconosciuto senza errore
# - Itera su tutte le coppie chiave-valore e stampale
student = {
    "nome": "Alice",
    "eta": 20,
    "corso": "Informatica"
}
print("Studente:", student)
 
student["eta"] = 21
print("Età modificata:", student["eta"])

student["matricola"] = "9462574"
print("Matricola aggiunta:", student["matricola"])
print("Studente dopo le modifiche:", student)

telefono = student.get("telefono", "Numero di telefono non disponibile")
print("Telefono:", telefono)

for chiave, valore in student.items():
    print(f"{chiave}: {valore}")