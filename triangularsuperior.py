def triangularSuperior(u, y):
	n = len(u)
	x = np.zeros((n,1))
	for i in range(n-1, -1, -1):
		x[i, 0] = (y[i,0] - u[i, i:n]@x[i:n,0])/u[i,i]
	return x
