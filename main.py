from horner import metodo_horner
from muller import muller_con_procedimiento
from interpolacionlineal import interpolacion_lineal
from lagrange import evaluacion_por_lagrange
from polinomio_lagrange import polinomio_de_lagrange
from regresion_lineal import regresion_lineal





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

def opcion_interpolacion_lineal():
    print("\n--- Método de Interpolación Lineal ---")
    interpolacion_lineal()

def opcion_lagrange():
    resultado = evaluacion_por_lagrange()
    print(f"\nResultado: {resultado}")

def opcion_polinomio_lagrange():
    polinomio_de_lagrange()

def opcion_regresion_lineal():
    regresion_lineal()

  


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Evaluación polinomial por el metodo de  Horner")
    print("2. Determonacion de raices por el Método de Muller")
    print("3. Determinación de polinomios por interpolación lineal")
    print("4. Evaluación polinomial por el método de LaGrange")
    print("5. Determinación de polinomios de LaGrange")
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
            opcion_interpolacion_lineal()
        elif opcion == "4":
            opcion_lagrange()
        elif opcion == "5":
            opcion_polinomio_lagrange()
        elif opcion == "6":
            opcion_regresion_lineal()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
