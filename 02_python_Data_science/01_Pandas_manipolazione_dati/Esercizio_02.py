import pandas as pd
import numpy as np
# Esercizio - 1 : Conversione Temperature
# Creo una colonna di temperature Celsius
c = {"Celsius":[1,10,20,30,40,50,60,70,80,90,100]}
df_temperature = pd.DataFrame(c, dtype="int32")

# Aggiungo una colonna con la conversione in Fahrenheit
df_temperature["Fahrenheit"] = df_temperature["Celsius"] *9/5 +32

print(df_temperature)

# Esercizio - 2 : Promosso/Bocciato
# Creo dei valori numerici
n = np.random.randint(1,30,10)
voti = {"Voti": n}
# Imposto il dataframe
df_votazioni = pd.DataFrame(voti)

# Creo la colonna "Esito"
df_votazioni["Esito"] = np.where(df_votazioni["Voti"] >= 18, "Promosso", "Bocciato")

print(df_votazioni)

# Esercizio - 3 : Busta paga
# Creo due colonne "Ore lavorate" e "Paga oraria"
ore = np.random.randint(20,50,20)
paga_oraria = np.random.randint(15,30,20)
df_paghe = pd.DataFrame({"Ore lavorate": ore , "Paga oraria":paga_oraria})

# Creo una colonna che calcoli il salario  settimanale
df_paghe["Salario settimanale"] = np.where(
    df_paghe["Ore lavorate"] > 40,
    df_paghe["Ore lavorate"]*df_paghe["Paga oraria"]*1.10,
    df_paghe["Ore lavorate"]*df_paghe["Paga oraria"]
    )
# Controllo senza straoridinari
df_paghe["Salario settimanale base"] = df_paghe["Ore lavorate"]*df_paghe["Paga oraria"]
print(df_paghe)