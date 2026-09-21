# Progetto d'Esame – Analisi di un Sistema di Prenotazione Viaggi

## Scenario Reale

Un'agenzia di viaggi online vuole realizzare un sistema informatico per gestire le prenotazioni dei clienti. Il sistema deve permettere di:

- memorizzare le informazioni dei clienti e dei viaggi prenotati,
- calcolare statistiche sulle vendite,
- analizzare i dati con strumenti avanzati,
- visualizzare i risultati in forma grafica.

## Consegna (da svolgere in Python)

### Parte 1 – Variabili e Tipi di Dati

1. Definisci variabili per rappresentare le seguenti informazioni di un cliente:
   - nome (stringa),
   - età (intero),
   - saldo conto (float),
   - stato VIP (booleano).

   ✅ Esempio: `nome = "Mario Rossi"`, `eta = 34`, `saldo = 2500.75`, `vip = True`
2. Crea una lista di destinazioni disponibili (almeno 5 città).
3. Definisci un dizionario che associa ogni destinazione a un prezzo medio del viaggio.

### Parte 2 – Programmazione ad Oggetti (OOP)

1. Crea una classe `Cliente` con attributi: nome, età, vip.
2. Aggiungi un metodo per stampare le informazioni.
3. Crea una classe `Viaggio` con attributi: destinazione, prezzo, durata in giorni.
4. Crea una classe `Prenotazione` che colleghi un cliente a un viaggio.
5. Deve calcolare l'importo finale, con sconto del 10% se il cliente è VIP.
6. Aggiungi un metodo `dettagli()` che stampa le informazioni complete.

### Parte 3 – NumPy

1. Genera un array NumPy di 100 prenotazioni simulate, con prezzi casuali fra 200 e 2000 €.
2. Calcola e stampa:
   - prezzo medio,
   - prezzo minimo e massimo,
   - deviazione standard,
   - percentuale di prenotazioni sopra la media.

### Parte 4 – Pandas

1. Crea un DataFrame Pandas con colonne: Cliente, Destinazione, Prezzo, Giorno_Partenza, Durata, Incasso.
2. Calcola con Pandas:
   - incasso totale dell'agenzia,
   - incasso medio per destinazione,
   - top 3 destinazioni più vendute.

### Parte 5 – Matplotlib

1. Crea un grafico a barre che mostri l'incasso per ogni destinazione.
2. Crea un grafico a linee che mostri l'andamento giornaliero degli incassi.
3. Crea un grafico a torta che mostri la percentuale di vendite per ciascuna destinazione.

### Parte 6 – Analisi Avanzata

1. Raggruppa i viaggi in categorie:
   - "Europa", "Asia", "America", "Africa". (Puoi usare un dizionario che associa ogni destinazione a una categoria).
2. Calcola con Pandas:
   - incasso totale per categoria,
   - durata media dei viaggi per categoria.
3. Salva il DataFrame aggiornato in un CSV chiamato `prenotazioni_analizzate.csv`.

### Parte 7 – Estensioni

1. Crea una funzione che restituisce i N clienti con più prenotazioni.
2. Realizza un grafico combinato (barre + linea) che mostri:
   - barre = incasso medio per categoria,
   - linea = durata media per categoria.
