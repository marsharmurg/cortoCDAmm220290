# lagrange.py

def evaluacion_por_lagrange():
    print("\n--- Evaluación por LaGrange ---")
    n = int(input("Ingrese el número de puntos: "))
    x_vals = []
    y_vals = []
    for i in range(n):
        x = float(input(f"Ingrese x[{i}]: "))
        y = float(input(f"Ingrese y[{i}]: "))
        x_vals.append(x)
        y_vals.append(y)
    x_eval = float(input("Ingrese el valor de x para evaluar: "))

    resultado = 0
    for i in range(n):
        term = y_vals[i]
        for j in range(n):
            if j != i:
                term *= (x_eval - x_vals[j]) / (x_vals[i] - x_vals[j])
        resultado += term

    return resultado
