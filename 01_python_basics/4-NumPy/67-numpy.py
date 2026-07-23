import numpy as np

dati = np.random.randint(10,100, size=(6,5))
print("Dati originali: \n", dati)

print("Shape: \n", dati.shape)

print("Tipo di dato: \n", dati.dtype)

print("Prima riga: \n", dati[0])
print("Prima colonna: \n", dati[:,0])
print("Submatrice (prime 2righe, prime 3 colonne): \n", dati[:2, :3])

view = dati[:2, :3]
copy = dati[:2, :3].copy()
view[0,0] = 999
print("Dati originali dopo modifica della view: \n", dati)
print("Copy: \n", copy) 

reshaped = dati.reshape(3,10)
print("Dati reshaped: \n", reshaped)

print("Iterazione su ogni elemento con nditer:")
for element in np.nditer(reshaped):
    print(int(element),end =" ")

extra = np.random.randint(10,100, size=(6,2))
unito = np.hstack((dati, extra))
print("\nDati concatenati: \n", unito)

split = np.split(unito, 2)
print("Dati divisi: \n", split[0], "\n\n", split[1])

mask = dati > 50
print("Valori maggiori di 50: \n", dati[mask])

ordinati = np.sort(dati, axis=1)
print("Dati ordinati per riga: \n", ordinati)

radici = np.sqrt(dati)
print("Radici quadrate dei dati: \n", radici)