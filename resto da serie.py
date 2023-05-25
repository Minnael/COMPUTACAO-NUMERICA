import numpy as np
import math

def d3f(x):
	return np.cos(x)
	
def resto(tal, x, x0):
	return ((d3f(tal))/6)*(x-x0)**3
	
print(resto(math.pi/5, math.pi/7, math.pi/5))
