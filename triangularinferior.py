def triangularInferior(u, y):
    n = len(u)
    x = np.zeros((n,1))
    x[0, 0] = y[0, 0]/u[0, 0]
    for i in range(1, n):
        x[i, 0] = (y[i,0] - u[i, 0:i]@x[0:i, 0])/u[i,i]
    return x
