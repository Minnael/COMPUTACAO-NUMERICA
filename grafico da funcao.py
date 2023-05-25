import matplotlib.pyplot as plt
import numpy as np

def f(x):
	return x
	
xg = np.linspace(-1, 4, 100)
yf = f(xg)

plt.plot(xg, yf)
plt.plot()
