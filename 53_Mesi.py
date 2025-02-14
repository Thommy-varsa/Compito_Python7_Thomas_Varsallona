mese = int(input("Inserisci un numero di un mese: "))

if mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
    print("Il mese che hai inserito ha 31 giorni")
elif mese == 4 or mese == 6 or mese == 9 or mese == 11:
    print("Il mese che hai inserito ha 30 giorni")
elif mese == 2:
    print("Il mese che hai scelto (febbraio) è l'unico mese che si distingue perchè ha 28 giorni negli anni normali e 29 giorni negli anni bisestili")
else:
    print("Numero del mese non valido. Inserisci un numero da 1 a 12.")