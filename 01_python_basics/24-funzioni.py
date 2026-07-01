# Media

def media(paramentro):
    somma = sum(paramentro)
    lunghezza = len(paramentro)
    return somma / lunghezza    
"""media come da esempio"""
print(f"La media di [1, 2, 3, 4, 5] è: {media([1, 2, 3, 4, 5])}")

parametri = int(input("Quanti numeri vuoi inserire? "))
"""media con input dell'utente"""
print("La media è:", media([int(input("Inserisci un numero: ")) for _ in range(parametri)]))