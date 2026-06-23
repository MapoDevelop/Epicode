# Crea una tupla con 3 colori
colors = ("rosso", "verde", "blu")
print("Tupla di colori:", colors)
# Stampa il primo e l'ultimo colore della tupla
print("Primo colore:", colors[0])
print("Ultimo colore:", colors[-1])

# Seconda tupla con 10 colori alcuni dei quali ripetuti
more_colors = ("rosso", "giallo", "verde", "blu", "verde", "arancione", "rosso", "verde", "blu", "bianco")
#Conta quante volte un colore appare nella tupla
count = more_colors.count("verde") #variante con più colori e ripetizioni
# count = colors.count("verde")
print("Il colore 'verde' appare", count, "volte nella tupla.")