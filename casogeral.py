import numpy as np

def f0(x):
	return x
	
def f1(x):
	return 1
	
def casoGeral(x, h):	
	s1=0; s2=0; s3=0; s4=0; s5=0; s6=0
	n = len(x)
	for i in range(n):
		s1 = s1 + (f0(x[i])*f0(x[i]))
		s2 = s2 + (f0(x[i])*f1(x[i]))
		s3 = s3 + (f1(x[i])*f0(x[i]))
		s4 = s4 + (f1(x[i])*f1(x[i]))
		s5 = s5 + (f0(x[i])*h[i])
		s6 = s6 + (f1(x[i])*h[i])
	
	A = np.array([
		[s1, s2],
		[s3, s4]
	])
	
	b = np.array([
		[s5],
		[s6]
	])
	
	a0, a1 = np.linalg.solve(A, b)
	return a0, a1
	

	
x = [1.0, 1.9, 2.8, 3.7, 4.6]
y = [2.24, 4.48, 7.13, 10.08, 12.98]
h = []

n = len(x)
for i in range (n):
	h.append(np.exp(y[i]/x[i]))
	
a0, a1 = casoGeral(x, h)
print(a0)
print(a1)

	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
