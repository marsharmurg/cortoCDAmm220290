from horner import metodo_horner
from muller import muller_con_procedimiento


def opcion_horner():
    entrada = input("Ingresa los coeficientes del polinomio separados por espacios (orden descendente): ")
    coef = list(map(float, entrada.strip().split()))
    x_valor = float(input("Ingresa el valor de x para evaluar el polinomio: "))
    print("\n--- Método de Horner ---")
    resultado = metodo_horner(coef, x_valor, verbose=True)
    print(f"\nResultado: {resultado}")


def opcion_muller():
    print("\n--- Método de Muller ---")
    fx_expr_str = input("Ingrese el polinomio (por ejemplo: x**3 - 2*x + 1): ")
    x0 = float(input("Ingrese x0: "))
    x1 = float(input("Ingrese x1: "))
    x2 = float(input("Ingrese x2: "))
    tol = float(input("Ingrese la tolerancia (por defecto 1e-6): ") or 1e-6)
    max_iter = int(input("Ingrese número máximo de iteraciones (por defecto 10): ") or 10)
    
    muller_con_procedimiento(fx_expr_str, x0, x1, x2, tol, max_iter)


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Evaluación polinomial por Horner")
    print("2. Método de Muller")
    print("3. Interpolación lineal")
    print("4. Evaluación por LaGrange")
    print("5. Polinomio de LaGrange")
    print("6. Regresión lineal por mínimos cuadrados")
    print("0. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            opcion_horner()
        elif opcion == "2":
            opcion_muller()
        elif opcion == "3":
            print(">> Aquí irá la interpolación lineal")
        elif opcion == "4":
            print(">> Aquí irá la evaluación por LaGrange")
        elif opcion == "5":
            print(">> Aquí irá el polinomio de LaGrange")
        elif opcion == "6":
            print(">> Aquí irá la regresión lineal")
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
