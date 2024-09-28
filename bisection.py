def bisection(f, a, b, tol=1e-6, max_iter=1000):    
    if f(a) * f(b) >= 0:
        return None
    
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        f_c = f(c)
        if f_c == 0 or (b - a) / 2 < tol:
            return c
        if f(a) * f_c < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return (a + b) / 2
