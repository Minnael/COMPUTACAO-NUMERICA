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
	y = np.linalg.solve(L, b)
	x = np.linalg.solve(U, y)
	
	return (L, U, x, y)
	
(L, U, x, y) = decomposicaoLU(A, b)
print(L)
print(U)
print(x)
print(y)
	

			
			
			
			
			
			
			
			
			
