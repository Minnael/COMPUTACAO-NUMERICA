import matplotlib.pyplot as plt
import numpy as np 

def f(x):
	return np.log((x**2)+1) #Colocar a função da questao

def df(x):
	return (2*x)/((x**2)+1) #Colocar a primeira derivada
	
def d2f(x):
	return (-2*(x**2)+2)/(((x**2)+1)**2) #Colocar a segunda derivada
	
def P2(x):
	x0 = -0.81
	return f(x0) + df(x0)*(x-x0) + (d2f(x0)/2)*((x-x0)**2) #Colocar a formula do polinomio de taylor

print(P2(-1.35))
