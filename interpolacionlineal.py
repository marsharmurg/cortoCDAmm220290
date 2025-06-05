def interpolacion_lineal():
    print("\n--- Método de Interpolación Lineal ---")
    x1 = float(input("Ingrese x1: "))
    y1 = float(input("Ingrese y1: "))
    x2 = float(input("Ingrese x2: "))
    y2 = float(input("Ingrese y2: "))

    if x1 == x2:
        print("Error: x1 y x2 no pueden ser iguales (pendiente indefinida).")
        return

    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    print(f"\nLa ecuación de la recta es: y = {m:.4f}x + {b:.4f}")
