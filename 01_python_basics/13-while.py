# Utilizzando il ciclo while, 
# scrivere un programma che chieda all'utente di inserire un numero intero positivo 
# Se l'utente inserisce un numero negativo o zero, il programma deve chiedere nuovamente l'input fino a quando non viene inserito un numero valido.
# quando l'utente inserisce un numero valido, il programma deve stampare "Hai inserito il numero positivo: " seguito dal numero inserito.
# termina il programma.

while True:
    numero = int(input("Inserisci un numero intero positivo: "))
    if numero > 0:
        print("Hai inserito il numero positivo:", numero)
        break
    else:
        print("Numero non valido. Riprova.")