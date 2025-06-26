# Solicitar al usuario el tipo de conversion (EURO a PESO o DOLAR a PESO)
import math

# Definir monedas disponibles.
monedas_disp = ["eur", "usd"]

# Definir tipo de cambio
peso_a_usd = 950.21
peso_a_euro = 1052.94
result = 0

# Pedir a que moneda quiere cambiar.
moneda = input("A que moneda desea cambiar (EUR/USD): ").strip().lower()

# Primero me fijo que si la moneda elegida esta dentro de las disponibles.
if moneda not in monedas_disp:
    print("La moneda elegida no es valida")

# Si elige EUR
elif moneda == "eur":
    monto = float(input("ingrese monto: "))
    result = monto / peso_a_euro
    print(f"Con ${monto} pesos recibira €{result:.2f} EUR")
# Si elige USD
elif moneda == "usd":
    monto = float(input("ingrese monto: "))
    result = monto / peso_a_usd
    print(f"Con ${monto} pesos recibira ${result:.2f} USD")

 

