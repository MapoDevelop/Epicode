# Immaginiamo due corsi universitari, uno di matematica e uno di informatica. 
# Ogni corso ha un insieme di studenti iscritti. 
# Vogliamo trovare 
# - gli studenti che sono iscritti a entrambi i corsi.
# - gli studenti che sono iscritti a matematica ma non a informatica.
# - gli studenti che sono iscritti a informatica ma non a matematica.
# - gli studenti che sono iscritti a almeno uno dei due corsi.
# - quanti studenti unici ci sono in totale.

A = {"Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"}
B = {"Charlie", "David", "Eve", "Frank", "Ivan", "Judy", "Mallory", "Niaj"}

# Studenti iscritti a entrambi i corsi
both = A & B
print("Studenti iscritti a entrambi i corsi:", both)

# Studenti iscritti a matematica ma non a informatica
only_math = A - B
print("Studenti iscritti a matematica ma non a informatica:", only_math)

# Studenti iscritti a informatica ma non a matematica
only_cs = B - A
print("Studenti iscritti a informatica ma non a matematica:", only_cs)

# Studenti iscritti a almeno uno dei due corsi
either = A | B
print("Studenti iscritti a almeno uno dei due corsi:", either)

# Numero totale di studenti unici
total_unique = len(either)
print("Numero totale di studenti unici:", total_unique)