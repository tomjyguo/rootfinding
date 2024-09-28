def newtons_method(f, df, x0, tol=1e-6, max_iter=1000):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        dfxn = df(xn)
        if abs(fxn) < tol:
            return xn
        if dfxn == 0:
            return None
        xn = xn - fxn / dfxn
    return None
