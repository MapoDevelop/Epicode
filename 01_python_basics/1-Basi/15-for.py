# Scrivi una lista di nomi
# Stampa ogni nome preceduto dal proprio indice
# Usa enumerate per ottenere sia l'indice che il nome
nomi = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("Lista dei nomi con indice:")
for indice, nome in enumerate(nomi, start=1):
    print(f"{indice}: {nome}")  

print("####################")