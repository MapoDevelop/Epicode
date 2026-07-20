import csv

def carica_studenti(file_path):
    """Carica gli studenti da un file CSV."""
    studenti = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            studenti.append(row)
    return studenti

if __name__ == '__main__':
    studenti = carica_studenti('data/studenti.csv')
    print(studenti)
