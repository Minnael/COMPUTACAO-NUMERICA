import numpy as np

def triangularSuperior(u, y):
	n = len(u)
	x = np.zeros((n, 1))
	for i in range(n-1, -1, -1):
		x[i, 0] = (y[i, 0] - u[i, i:n]@x[i:n, 0])/u[i, i]
	return x

def eliminacaoGauss(A, b):
	matrizA = np.concatenate((A, b),1)
	n = len(matrizA)
	for j in range(n - 1):
		pivo = matrizA[j, j]
		for i in range(j+1, n):
			fator = matrizA[i, j]/pivo
			print(fator)
			matrizA[i, 0:] = matrizA[i, 0:] - fator*matrizA[j, 0:]
	u = matrizA[0:, 0:n]
	y = matrizA[0:, n:n+1]
	print(triangularSuperior(u, y))
	
A = np.array([
	[5, 4, 6, -3],
	[30, 30, 39, -20],
	[-5, -46, -30, 14],
	[-35, 8, -33, -5]
]) 

b = np.array([
	[-21],
	[-166],
	[298],
	[-127]
])

eliminacaoGauss(A, b)

