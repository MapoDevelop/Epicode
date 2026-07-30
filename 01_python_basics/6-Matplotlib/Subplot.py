import matplotlib.pyplot as plt
# Metodo di creazione di più grafici con subplots - VECCHIO METODO
# Primo subplot
plt.subplot(2, 1, 1)
plt.plot([1, 2, 3], [1, 4, 9], color='r', marker='o', linestyle='-')

# Secondo subplot
plt.subplot(2, 1, 2)
plt.plot([1, 2, 3], [1, 2, 3], color='g', marker='s', linestyle='--')

plt.show()


# Metodo di creazione di più grafici con subplots - NUOVO METODO
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot([1, 2, 3], [1, 4, 9], color='r', marker='o', linestyle='-')
axs[0, 1].plot([1, 2, 3], [1, 2, 3], color='g', marker='s', linestyle='--')
axs[1, 0].plot([1, 2, 3], [9, 4, 1], color='b', marker='^', linestyle=':')
axs[1, 1].plot([1, 2, 3], [3, 2, 1], color='m', marker='d', linestyle='-.')
plt.tight_layout()
plt.show()