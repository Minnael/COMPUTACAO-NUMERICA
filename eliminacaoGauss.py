import numpy as np

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
	return np.linalg.solve(u, y)
	
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

print(eliminacaoGauss(A, b))

