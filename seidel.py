import numpy as np

def gaussSeidel(a,b,t,n):
  g=len(a)
  cont=0
  xa=np.ones(g)
  xn=np.zeros(g)
  while np.max(np.fabs(xn-xa))>10**(-t):
    xa[:]=xn[:]
    for i in range(g):
      soma=0
      for j in range(g):
        if i!=j:
          soma+=a[i,j]*xn[j]
      xn[i]=(b[i]-soma)/a[i,i]
    cont=cont+1
  return( xn, cont, np.max(np.fabs(xn-xa))/np.max(np.fabs(xn)))#errorelativo

A = np.array([[14, 2, -4],
              [1, 12, 2],
            [4, 1, -16]])

b = np.array([4, 14, -4])

res = gaussSeidel(A, b, 2, 3)

print("Solução: ", res[0])
print("Iter: ", res[2])
print("erro: ", res[1])
