lato1 = float(input("Inserire il primo lato: "))
lato2 = float(input("Inserire il secondo lato: "))
lato3 = float(input("Inserire il terzo lato: "))


if (lato1 < lato2 + lato3) and (lato2 < lato1 + lato3) and (lato3 < lato1 + lato2):
    print("Le misure inserite possono formare un triangolo.")
else:
    print("Le misure inserite NON possono formare un triangolo.")