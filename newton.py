import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 23

def df(x):
    return 2*x

def newton(a, b, erro, itmax):
    it = 0
    x = a
    er = 1
    
    while (er >= erro and it < itmax):
        xold = x
        x = xold - ((f(xold))/(df(xold)))
        er = np.abs((x-xold)/x)
        it = it + 1
        
    return (x, er, it)

a = 4.5
b = 5.5
itmax = 100
erro = 10**-5
res = newton(a, b, erro, itmax)
print(f'{res[0]:.4f}')
