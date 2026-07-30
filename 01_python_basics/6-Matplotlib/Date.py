import matplotlib.pyplot as plt
import pandas as pd

date = pd.date_range(start='2023-01-01', periods=6, freq='ME')

valori = [10, 15, 7, 12, 20, 18]

plt.plot(date, valori, marker='o', linestyle='-', color='b')
plt.title('Valori Mensili') 
plt.xlabel('Data')
plt.ylabel('Valori')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
