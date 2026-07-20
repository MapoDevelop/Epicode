import numpy as np
import time

# crea numero random tra 1 e 100
np.random.seed(int(time.time()))  # Imposta il seed diverso ogni volta che esegui il codice
print(np.random.randint(1, 101))