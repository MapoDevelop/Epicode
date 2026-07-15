# Creauna classe Studente con attributo eta
# Se l'età è negativa, lancia un'eccezione personalizzata EtaNonValidaError
# Organizza le tue eccezioni sotto una classe base ErroreScuola

class Studente:
    def __init__(self,nome, eta):
        if eta < 0:
            raise EtaNonValidaError()
        self.nome = nome
        self.eta = eta
class ErroreScuola(Exception):
    pass

class EtaNonValidaError(ErroreScuola):
    def __init__(self, message="L'età non può essere negativa!"):
        super().__init__(message)

studente1 = Studente("Mario", 20)
print(f"Studente creato: {studente1.nome}, Età: {studente1.eta}")
try:
    studente2 = Studente("Luigi", -4)  # Questo solleverà un EtaNonValidaError
    print(studente2)
except EtaNonValidaError as e:
    print(e)   

# Crea una classe Magazzino con metodo rimuovi_prodotto(nome,quantita)
# Se non ci sono abbastanza prodotti, lancia un'eccezione personalizzata ProdottoEsauritoError
# Organizza le tue eccezioni sotto una classe base ErroreMagazzino

class ErroreMagazzino(Exception):
    pass

class ProdottoEsauritoError(ErroreMagazzino):
    def __init__(self, message="Hai superato la disponibilità a magazzino"):
        super().__init__(message)

class Magazzino:
    def __init__(self, nome, quantita):
        self.nome = nome
        self.quantita = quantita

    def rimuovi_prodotto(self, nome, quantita):
        if (self.quantita - quantita) < 0:
            raise ProdottoEsauritoError()
        self.quantita -= quantita

prodotto1 = Magazzino("Prodotto1", 10)
print(f"Prodotto creato: {prodotto1.nome}, Quantità: {prodotto1.quantita}")
try:   
    prodotto1.rimuovi_prodotto("Prodotto1", 15)  # Questo solleverà un ProdottoEsauritoError
    print(prodotto1)
except ProdottoEsauritoError as e:
    print(e)