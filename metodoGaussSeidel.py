import numpy as np

def metodoGaussSeidel(A, b, p, x0, nmax):
	n = len(A)
	inv = np.linalg.inv(A * np.eye(n))
	B = np.eye(n) - inv@A
	d = inv@b
	
	x0ld = np.copy(x0)
	x = np.copy(x0)
	it = 0
	er = 1
	while(er >= 10**(-p) and it < nmax):
		for i in range(n):
			x[i, 0] = B[i, :]@x + d[i, 0]
		er = (np.max(np.abs(x-x0ld)))/(np.max(np.abs(x)))
		x0ld = np.copy(x)
		it = it + 1
		
	return x, er, it
	
A = np.array([
	[12, 3, -4],
	[4, 12, 3],
	[0, 4, -12]
])

b = np.array([
	[-2],
	[12],
	[-4]
])

p = 2
x0 = np.array([
	[0.],
	[0.],
	[0.]
])
nmax = 30

x, er, it = metodoGaussSeidel(A, b, p, x0, nmax)
print(it)

		
		
		
		
		
		
		
		
		
		
		
		
