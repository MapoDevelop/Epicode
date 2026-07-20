# Crea una classe ContoBancario con:
# - Variabile di istanza saldo iniziale
# - Metodo deposita(importo) che aggiunge un importo al saldo
# - Metodo preleva(importo) che sottrae un importo dal saldo solo se sufficiente

class ContoBancario:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
    
    def set_deposita(self, importo):
        if importo > 0:
            self.__saldo = self.__saldo + importo
    
    def set_preleva(self, importo):
        if self.__saldo >= importo:           
            self.__saldo = self.__saldo - importo
    

saldo_iniziale = int(input("Inserisci il saldo iniziale del conto: "))
conto = ContoBancario(saldo_iniziale)

versamento = int(input("Quanto vuoi versare? " ))

conto.set_deposita(versamento)

prelievo = int(input("Quanto vuoi prelevare? " ))
conto.set_preleva(prelievo)

print(f"Saldo del conto: {conto.get_saldo()}")


