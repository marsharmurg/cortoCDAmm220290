import sympy as sp
import numpy as np

def muller_con_procedimiento(fx_expr_str, x0, x1, x2, tol=1e-6, max_iter=10):
    x = sp.Symbol('x')
    fx_expr = sp.sympify(fx_expr_str)
    f = sp.lambdify(x, fx_expr, modules=['numpy'])

    for i in range(max_iter):
        fx0 = f(x0)
        fx1 = f(x1)
        fx2 = f(x2)

        print(f"\nIteración {i+1}:")
        print(f"x0 = {x0}, f(x0) = {fx0}")
        print(f"x1 = {x1}, f(x1) = {fx1}")
        print(f"x2 = {x2}, f(x2) = {fx2}")

        if abs(fx2) < tol:
            print(f"Raíz encontrada con tolerancia {tol}. Valor: {x2}")
            return x2

        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (fx1 - fx0) / h0
        d1 = (fx2 - fx1) / h1
        a = (d1 - d0) / (h1 + h0)
        b = a * h1 + d1
        c = fx2

        disc = b**2 - 4*a*c
        sqrt_disc = np.sqrt(abs(disc)) * (1 if disc >= 0 else 1j)

        denom1 = b + sqrt_disc
        denom2 = b - sqrt_disc

        if abs(denom1) > abs(denom2) and abs(denom1) > 1e-14:
            denom = denom1
        elif abs(denom2) > 1e-14:
            denom = denom2
        else:
            print("Denominador muy pequeño. Terminando.")
            break

        dxr = -2*c / denom
        xr = x2 + dxr

        print(f"Delta xr = {dxr}")
        print(f"Nuevo xr = {xr}")

        x0, x1, x2 = x1, x2, xr

    print("Máximo número de iteraciones alcanzado.")
    return x2
