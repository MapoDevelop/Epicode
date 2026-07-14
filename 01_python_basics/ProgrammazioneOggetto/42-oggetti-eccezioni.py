# Crea una classe Divisione con metodo dividi(a,b) 
# che restituisce il risultato della divisione per zero
print("##############################################")
print("Esempio di gestione della divisione per zero in Python")
class Divisione:
    def dividi(self, dividendo, divisore):
        try:
            return print(f"Risultato di {dividendo} / {divisore}: {dividendo / divisore}")
        except ZeroDivisionError:
            return print("Non puoi dividere per zero!")
        

dividendo = int(input("Inserisci un dividendo: "))
divisore = int(input("Inserisci un divisore: "))

Divisione().dividi(dividendo, divisore)

# Crea una classe Persona che sollevi un ValueError se l'età è negativa

print("##############################################")
print("Esempio di gestione di un ValueError in Python")
class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        if eta < 0:
            raise ValueError("L'età non può essere negativa!")
        self.eta = eta

    def __str__(self):
        return f"Nome: {self.nome}, Età: {self.eta}"

try:

    persona2 = Persona("Luigi", -4)  # Questo solleverà un ValueError
    print(persona2)
except ValueError as e:
    print(e)

# Crea una classe Banca con metodo preleva() 
# Se il saldo è insufficiente solleva un'eccezione personalizzata.

print("##############################################")
print("Esempio di gestione di un'eccezione personalizzata in Python")
class Banca:
    def __init__(self, saldo):
        self.__saldo = saldo

    def preleva(self, importo):
        if importo > self.__saldo:
             raise SaldoInsufficienteError("Saldo insufficiente")
        self.__saldo -= importo

class SaldoInsufficienteError(Exception):
    pass

conto = Banca(2000)
print("Conto creato con saldo iniziale di 2000")
print("Tentativo di prelievo di 3000")
try:
    conto.preleva(3000)
    print("Prelievo avvenuto")
except SaldoInsufficienteError as e:
    print(e)