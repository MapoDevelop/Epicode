# Crea un array di numeri da 1 a 10
# Calcolare i dati cubici di ogni numero nell'array
# Creare un DataFrame con i numeri e i loro cubi
# Visualizzare un grafico

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

numeri = np.arange(1, 11)  # Crea un array di numeri da 1 a 10
quadrati = numeri ** 2  # Calcola i quadrati dei numeri
cubi = numeri ** 3  # Calcola i cubi dei numeri

data = {'Numero': numeri, 'Quadrato': quadrati, 'Cubo': cubi}  # Crea un dizionario con i dati
df = pd.DataFrame(data)  # Crea un DataFrame con i dati

# Visualizza il DataFrame
print(df)

# Visualizza un grafico dei numeri e dei loro cubi
plt.plot(df['Numero'], df['Quadrato'], marker='o', label='Quadrato')  # Crea un grafico a linee con marker
plt.plot(df['Numero'], df['Cubo'], marker='s', label='Cubo')  # Crea un grafico a linee con marker
plt.title('Quadrati e Cubi dei Numeri da 1 a 10')  # Aggiunge un titolo al grafico
plt.xlabel('Numero')  # Aggiunge un'etichetta all'asse x
plt.ylabel('Valore')  # Aggiunge un'etichetta all'asse y
plt.grid()  # Aggiunge una griglia al grafico
plt.legend()  # Mostra la legenda
plt.show()  # Mostra il grafico