import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**2) - 14

def bissecao(a, b, erro, itmax):
    it = 0
    x = a
    er = 1
    
    while(er >= erro and it < itmax):
        xold = x
        x = (a+b)/2
        er = np.abs((x - xold)/x)
        if (f(a)*f(x) < 0):
            b = x
        else:
            a = x
            
        it = it + 1
    return (x, er, it)

a = 3
b = 4
erro = 10**-5
itmax = 5

res = bissecao(a, b, erro, itmax)
print(res[0])






    
    




