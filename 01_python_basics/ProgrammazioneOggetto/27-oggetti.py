# Scrivi una classe "Studente"
# attributi: nome, corso
# metodi: presentati() che stampi una frase di presentazione

class Studente:
    def __init__(self, nome, corso):
        self.nome = nome
        self.corso = corso

    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} e sto studiando {self.corso}.")

studente1 = Studente("Elisa", "Intelligenza Artificiale")
studente1.presentati()