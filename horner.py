def metodo_horner(coeficientes, x, verbose=False):
    """
    Aplica el método de Horner para evaluar un polinomio en x.
    coeficientes: lista de coeficientes (orden descendente)
    x: valor en el que se evalúa el polinomio
    verbose: si True imprime paso a paso
    """
    resultado = coeficientes[0]
    if verbose:
        print(f"Paso 0: b0 = {resultado}")
    
    for i in range(1, len(coeficientes)):
        resultado = resultado * x + coeficientes[i]
        if verbose:
            print(f"Paso {i}: b{i} = b{i-1} * {x} + {coeficientes[i]} = {resultado}")
    
    if verbose:
        print(f"Resultado final: F({x}) = {resultado}")
    return resultado
