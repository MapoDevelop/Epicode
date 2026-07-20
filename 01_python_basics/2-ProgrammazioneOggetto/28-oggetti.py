# Creiamo una classe Persona con attributi nome e metodo presentati()
# Poi crea una classe Studente che eredita da Persona e aggiunge un attributo corso e lo include in presentati().
# Infine rendi l'attributo nome privato e permetti di leggerlo solo tramite un metodo dedicato.

class Persona:
    def __init__(self, nome):
        self.__nome = nome
        
    def get_nome(self):
        return self.__nome
    
    def presentati(self):
        print(f"Ciao, mi chiamo {self.__nome}.")

class Studente(Persona):
    def __init__(self, nome, corso):
        super().__init__(nome)
        self.corso = corso
    
    def presentati(self):
        print(f"Ciao, mi chiamo {self.get_nome()} e sto studiando {self.corso}.")
    

studente1 = Studente("Elisa", "Intelligenza Artificiale")
studente1.presentati()