import numpy as np 

A = np.array([
	[7, 5, -5, 3],
	[49, 36, -37, 16],
	[-7, -10, 20, 35],
	[42, 27, 11, 59]
])

b = np.array([
	[50],
	[393],
	[-308],
	[-160]
])

def triangularSuperior(u, y):
	n = len(u)
	x = np.zeros((n,1))
	for i in range(n-1, -1, -1):
		x[i, 0] = (y[i,0] - u[i, i:n]@x[i:n,0])/u[i,i]
	return x

def triangularInferior(l, b):
    n = len(l)
    x = np.zeros((n,1))
    x[0, 0] = b[0, 0]/l[0, 0]
    for i in range(1, n):
        x[i, 0] = (b[i,0] - l[i, 0:i]@x[0:i, 0])/l[i,i]
    return x

def decomposicaoLU(A, b):
	n = len(A)
	L = np.eye(n)
	soma = 0
	for j in range(n-1):
		pivo = A[j, j]
		for i in range(j+1, n):
			fator = A[i, j]/pivo
			L[i, j] = fator
			A[i, 0:] = A[i, 0:] - fator * A[j, 0:]
	U = A
	y = triangularInferior(L, b)
	x = triangularSuperior(U, y)
	for i in range(n):
		soma = soma + sum(U[i]) + sum(L[i])
	soma = soma + sum(x)
	return soma
	
print(decomposicaoLU(A, b))
	

			
			
			
			
			
			
			
			
			
