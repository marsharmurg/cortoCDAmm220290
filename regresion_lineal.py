# regresion_lineal.py

def regresion_lineal():
    print("\n--- Regresión lineal por mínimos cuadrados ---")
    n = int(input("Ingrese el número de puntos: "))
    x_vals = []
    y_vals = []

    for i in range(n):
        x = float(input(f"Ingrese x[{i}]: "))
        y = float(input(f"Ingrese y[{i}]: "))
        x_vals.append(x)
        y_vals.append(y)

    suma_x = sum(x_vals)
    suma_y = sum(y_vals)
    suma_x2 = sum(x ** 2 for x in x_vals)
    suma_xy = sum(x_vals[i] * y_vals[i] for i in range(n))

    # Cálculo de los coeficientes
    denominador = n * suma_x2 - suma_x ** 2
    if denominador == 0:
        print("Error: División por cero al calcular la regresión.")
        return

    a = (n * suma_xy - suma_x * suma_y) / denominador
    b = (suma_y * suma_x2 - suma_x * suma_xy) / denominador

    print(f"\nRecta de regresión: y = {a:.4f}x + {b:.4f}")
