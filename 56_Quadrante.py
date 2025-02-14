x = float(input("Inserisci la coordinata x: "))
y = float(input("Inserisci la coordinata y: "))

if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
    print("Il punto appartiene al primo o al terzo quadrante.")
else:
    print("Il punto appartiene al secondo o al quarto quadrante.")

if x == y:
    print("Il punto si trova sulla bisettrice y = x.")
elif x == -y:
    print("Il punto si trova sulla bisettrice y = -x.")
else:
    print("Il punto non si trova su nessuna delle bisettrici.")
