# Aggiungere un contatto (nome, cognome, numero, email di telefono) alla rubrica
# Modificare un contatto esistente
# Eliminare un contatto dalla rubrica
# Cercare un contatto per nome o cognome
# Visualizzare tutti i contatti presenti nella rubrica

rubrica = []

# Funzione per AGGIUNGERE un contatto alla rubrica
def aggiungi_contatto(nome, cognome, numero, email):
    contatto = {
        'nome': nome,
        'numero': numero,
        'cognome': cognome,
        'email': email
    }
    rubrica.append(contatto)
    print(f"Contatto {nome} {cognome} aggiunto con successo.")

# Funzione per MODIFICARE un contatto esistente nella rubrica
def modifica_contatto(nome, cognome, nuovo_numero=None, nuova_email=None):
    for contatto in rubrica:
        if contatto['nome'].lower() == nome.lower() and contatto['cognome'].lower() == cognome.lower():
            if nuovo_numero:
                contatto['numero'] = nuovo_numero
            if nuova_email:
                contatto['email'] = nuova_email
            print(f"Contatto {nome} {cognome} modificato con successo.")
            return
    print(f"Contatto {nome} {cognome} non trovato.")
    

# Funzione per ELIMINARE un contatto dalla rubrica
def elimina_contatto(nome, cognome):
    for contatto in rubrica:
        if contatto['nome'].lower() == nome.lower() and contatto['cognome'].lower() == cognome.lower():
            rubrica.remove(contatto)
            print(f"Contatto {nome} {cognome} eliminato con successo.")
            return
    print(f"Contatto {nome} {cognome} non trovato.")

# Funzione per CERCARE un contatto per nome o cognome
def cerca_contatto(nome=None, cognome=None):
    risultati = []
    for contatto in rubrica:
        if (nome and contatto['nome'].lower() == nome.lower()) or (cognome and contatto['cognome'].lower() == cognome.lower()):
            
            risultati.append(contatto)
    print("###############################")
    print(f"CONTATTI TROVATI: {len(risultati)}")
    print("###############################")

    return risultati

# Funzione per VISUALIZZARE tutti i contatti presenti nella rubrica
def visualizza_contatti():
    if not rubrica:
        print("La rubrica è vuota.")
        return
    
    print("###############################")
    print("RUBRICA TELEFONICA:")
    print("###############################")
    ordinati = sorted(rubrica, key=lambda x: (x['cognome'].lower(), x['nome'].lower()))
    for contatto in ordinati:
        print(f"{contatto['nome']} {contatto['cognome']}: {contatto['numero']}, {contatto['email']}")

# Creo un menu per interagire con la rubrica
while True:
    print("\nRubrica Telefonica")
    print("1. Aggiungi contatto")
    print("2. Modifica contatto")
    print("3. Elimina contatto")
    print("4. Cerca contatto")
    print("5. Visualizza tutti i contatti")
    print("6. Esci")

    scelta = input("Seleziona un'opzione: ")

    if scelta == '1':
        nome = input("Inserisci il nome: ")
        cognome = input("Inserisci il cognome: ")
        numero = input("Inserisci il numero di telefono: ")
        email = input("Inserisci l'email: ")
        aggiungi_contatto(nome, cognome, numero, email)
    elif scelta == '2':
        nome = input("Inserisci il nome del contatto da modificare (Obbligatorio): ")
        cognome = input("Inserisci il cognome del contatto da modificare (Obbligatorio): ")
        # TODO: Aggiungere la verifica se il contatto esiste prima di chiedere i nuovi valori
        risultati = cerca_contatto(nome, cognome)
        if not risultati:
            print("Contatto non trovato.")
            continue
        print("Ora puoi modificare il numero di telefono e l'email del contatto.")
        print("Lascia vuoto il campo se non vuoi modificare il valore.")
        nuovo_numero = input("Inserisci il nuovo numero di telefono (lascia vuoto se non vuoi modificare): ")
        nuova_email = input("Inserisci la nuova email (lascia vuoto se non vuoi modificare): ")
        modifica_contatto(nome, cognome, nuovo_numero if nuovo_numero else None, nuova_email if nuova_email else None)
    elif scelta == '3':
        nome = input("Inserisci il nome del contatto da eliminare (Obbligatorio): ")
        cognome = input("Inserisci il cognome del contatto da eliminare (Obbligatorio): ")
        elimina_contatto(nome, cognome)
    elif scelta == '4':
        nome = input("Inserisci il nome da cercare (lascia vuoto se non vuoi cercare per nome): ")
        cognome = input("Inserisci il cognome da cercare (lascia vuoto se non vuoi cercare per cognome): ")
        risultati = cerca_contatto(nome if nome else None, cognome if cognome else None)
        if risultati:
            for contatto in risultati:
                print(f"{contatto['nome']} {contatto['cognome']}: {contatto['numero']}, {contatto['email']}")
        else:
            print("Nessun contatto trovato.")
    elif scelta == '5':
        visualizza_contatti()
    elif scelta == '6':
        print("Uscita dalla rubrica.")
        break
    else:
        print("Opzione non valida. Riprova.")