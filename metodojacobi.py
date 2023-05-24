import numpy as np

A = np.array([
	[12, 2, -1],
	[3, 12, 2],
	[4, 3, -10]
])

b = np.array([
	[4],
	[12],
	[-1]
])

def metodoJacobi(A, b, p, x0, nMax):
	n = len(A)
	inv = np.linalg.inv(A * np.eye(n))
	B = np.eye(n) - inv@A
	d = inv@b
	
	x0ld = np.copy(x0)
	it = 0
	er = 1
	
	while (er >= 10**(-p) and it < nMax):
		x = B@x0ld + d
		er = (np.max(np.abs(x - x0ld)))/np.max(np.abs(x))
		x0ld = np.copy(x)
		it = it + 1
	return (x, it, er)

n = len(A)
x0 = np.array([
	[0],
	[0],
	[0]
])
x, it, er = metodoJacobi(A, b, 3, x0, 30)
print(f'{x}\n{it}\n{er}')
