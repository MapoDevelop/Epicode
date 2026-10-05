# Valori Mancanti

import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

# Esercizio 1 - Sostituzione Statistica
n = [77, 10, np.nan, 32, 77, 39, 77, np.nan, 39, 38]

df_num = pd.DataFrame(n, columns=["Numeri"])

print(df_num)

df_num["Numeri"] = df_num["Numeri"].fillna(50)

print(df_num)

# Esercizio 2 - Sostituzione Statistica

# Ho creato le tre colonne uguali, così da vedere la differenza
df_num["Numeri"] = df_num["Numeri"].fillna(df_num["Numeri"].mean())
df_num["Numeri_2"] = pd.DataFrame(n, columns=["Numeri_2"])
df_num["Numeri_2"] = df_num["Numeri_2"].fillna(df_num["Numeri_2"].median())
df_num["Numeri_3"] = pd.DataFrame(n, columns=["Numeri_3"])
df_num["Numeri_3"] = df_num["Numeri_3"].fillna(df_num["Numeri_3"].mode()[0])

print(df_num)

# Esercizio 3 - Sostituzione Avanzata
data = {
    "Guadagno": [3000,2500,np.nan,4500,1800,np.nan,3500,6800],
    "Ore": [77, 10, np.nan, 32, 77, 39, 77, np.nan],
}

df_num2 =  pd.DataFrame(data)

print(df_num2)

imputer = KNNImputer(n_neighbors=3)
imputer2 = KNNImputer(n_neighbors=2)
imputer3 = KNNImputer(n_neighbors=5)

df_imputed = pd.DataFrame(imputer.fit_transform(df_num2), columns=df_num2.columns)
print(df_imputed)

df_imputed2 = pd.DataFrame(imputer2.fit_transform(df_num2), columns=df_num2.columns)
print(df_imputed2)

df_imputed3 = pd.DataFrame(imputer3.fit_transform(df_num2), columns=df_num2.columns)
print(df_imputed3)
