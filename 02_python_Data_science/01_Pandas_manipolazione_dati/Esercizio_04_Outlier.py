# Esercizio 1 - 
# Crea un dataframe con 10 valori numerici casuali
# Invividua gli outlier usando la deviazione standard.
import pandas as pd
import numpy as np

n = np.random.randint(1,100,9)
n = np.append(n, 150)
df_num = pd.DataFrame(n, columns=["Numeri"])

media = df_num["Numeri"].mean()
deviazione_standard = df_num["Numeri"].std()

df_num["Outlier"] = (abs(df_num["Numeri"] - media) > 2 * deviazione_standard)

print(df_num)

# Esercizio 2 -
# Genera 20 valori applica un metodo IQR
# Rimuovi le righe con outlier per mostrareil dataset pulito

n20 = np.random.randint(4_000, 5_000, 18)
n20 = np.append(n20, [50,8_000])
df_num20 = pd.DataFrame(n20, columns=["Numeri"])

Q1 = df_num20["Numeri"].quantile(0.25)
Q3 = df_num20["Numeri"].quantile(0.75)

IQR = Q3 - Q1

# esclude gli outlier -- ho invertito mggiore e minore
df_pulito = df_num20[
    (df_num20["Numeri"] >= Q1 - 1.5 * IQR) & 
    (df_num20["Numeri"] <= Q3 + 1.5 * IQR) 
]

print(df_pulito)

# Esercizio 3 -
# Utilizzio di Machilne Learning
# su un dataset con due colonne numeriche (Altezza e Peso)
# Individua gli outlier e visualizza i risultati 
# in un DataFrame con una colonna aggiuntiva che indichi i valori anormali

from sklearn.ensemble import IsolationForest

data = {"Peso" : [60,70,130,25,65,68], "Altezza": [165,160,170,40,175,300]}

df = pd.DataFrame(data)

isolater =  IsolationForest(contamination=0.3, random_state=42)

df["Outlier_Peso"] = (isolater.fit_predict(df[["Peso"]]) == -1) | (isolater.fit_predict(df[["Altezza"]]) == -1)

print(df)



