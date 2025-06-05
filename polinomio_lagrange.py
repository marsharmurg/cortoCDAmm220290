# polinomio_lagrange.py

def polinomio_de_lagrange():
    print("\n--- Polinomio de LaGrange ---")
    n = int(input("Ingrese el número de puntos: "))
    x_vals = []
    y_vals = []
    for i in range(n):
        x = float(input(f"Ingrese x[{i}]: "))
        y = float(input(f"Ingrese y[{i}]: "))
        x_vals.append(x)
        y_vals.append(y)

    print("\nPolinomio de Lagrange construido:")
    print("P(x) = ", end="")

    partes = []
    for i in range(n):
        numerador = []
        denominador = 1
        for j in range(n):
            if j != i:
                numerador.append(f"(x - {x_vals[j]})")
                denominador *= (x_vals[i] - x_vals[j])
        termino = f"{y_vals[i]:.3f} * " + " * ".join(numerador)
        partes.append(f"({termino}) / {denominador:.3f}")

    print(" +\n      ".join(partes))
