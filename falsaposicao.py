import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x**2) - 35

def falsaposicao(a, b, erro, itmax):
    it = 0
    x = a
    er = 1
    
    while(er >= erro and it < itmax):
        xold = x
        x = (a-(((b-a)*f(a))/(f(b)-f(a))))
        er = np.abs((x - xold)/x)
        if (f(a)*f(x) < 0):
            b = x
        else:
            a = x
            
        it = it + 1
    return (x, er, it)

a = 4
b = 6
erro = 10**-5
itmax = 5
res = falsaposicao(a,b,erro,itmax)
print(f'{res[0]:.4f}')
