import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**2 - 17

def secante(x0, x1, erro, itmax):
    er = 1
    it = 0
    xa1 = x0
    x = x1
    
    while (er >= erro and it < itmax):
        xa2 = xa1
        xa1 = x
        x = xa1 - (f(xa1)*(xa2-xa1)/(f(xa2) - f(xa1)))
        er = np.abs((x-xa1)/x)
        it = it + 1
    return (x, er, it)
        
x0 = 2.5
x1 = 5
erro = 10**-5
itmax = 5
res = secante(x0, x1, erro, itmax)
print(f'{res[0]:.4f}')

