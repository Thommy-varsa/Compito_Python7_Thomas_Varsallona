def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

anno = int(input("Inserisci un anno: "))

if is_leap_year(anno) :
 print(f"L'anno {anno} è bisestile.")
else:
 print(f"L'anno {anno} non è bisestile.")