# 1: Verificare se un numero è positivo, negativo o zero
number = float(input("Inserisci un numero: "))
if number > 0:
    print("Il numero è positivo.")  
elif number < 0:
    print("Il numero è negativo.")
elif number == 0:
    print("Il numero è zero.")
else:
    print("Input non valido.")

# 2: Verificare se due stringhe sono uguali 
s1 = "Ciao"
s2 = "Ciao"

print("Stringa 1:", s1)
print("Stringa 2:", s2)

if s1 == s2:
    print(s1 == s2)
    print("Le stringhe sono uguali.")
else:
    print("Le stringhe sono diverse.")

# 3: Verificare se due numeri sono positivi
a = float(input("Inserisci il primo numero: "))
b = float(input("Inserisci il secondo numero: "))   

if a > 0 and b > 0:
    print("Entrambi i numeri sono positivi.")
else:
    print("Almeno uno dei numeri non è positivo.")


#Esercizio Booleani
# Scrivi un programma che 
# chieda all'utente la sua età e se ha la patente di guida.
 
# se l'età è maggiore o uguale a 18 e l'utente ha la patente,
#   Il programma dovrebbe stampare "True" e "Puoi guidare" 
# altrimenti 
#   dovrebbe stampare "False" e "Non puoi guidare".

print("########################")
print("Esercizio Patente di guida")
age = int(input("Inserisci la tua età: "))
has_license = input("Hai la patente di guida? (sì/no): ").strip().lower()
if age >= 18 and (has_license == "sì" or has_license == "si"):
    print("True")
    print("Puoi guidare.")
else:
    print("False")
    print("Non puoi guidare.")

########################

print("########################")
print("Esercizio Biblioteca")

# Un utente può entrare in biblioteca se:
# - non è in ritardo con la restituzione dei libri
# oppure
# - ha un abbonamento premium

# Chiedi all'utente se è in ritardo con la restituzione dei libri (sì/no)
# Chiedi all'utente se ha un abbonamento premium (sì/no)

# Se l'utente non è in ritardo o ha un abbonamento premium, stampa "True" e "Puoi entrare in biblioteca"
# Altrimenti, stampa "False" e "Non puoi entrare in biblioteca"

is_late = input("Sei in ritardo con la restituzione dei libri? (sì/no): ").strip().lower()
has_premium = input("Hai un abbonamento premium? (sì/no): ").strip().lower()

if is_late == "no" or (has_premium == "sì" or has_premium == "si"):
    print("True")
    print("Puoi entrare in biblioteca.")
else:
    print("False")
    print("Non puoi entrare in biblioteca.")