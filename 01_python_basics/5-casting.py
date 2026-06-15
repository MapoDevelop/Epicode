num = input("Inserisci un numero: ")

try:
    print(float(num))
    print("Hai inserito il numero: " + str(num))
except ValueError:
    print("Non hai inserito un numero valido.")