def secant_method(f, x0, x1, tol=1e-6, max_iter=1000):
    for n in range(max_iter):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if abs(f_x1) < tol:
            return x1
        if f_x0 == f_x1:
            return None
        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, x2
    return None
