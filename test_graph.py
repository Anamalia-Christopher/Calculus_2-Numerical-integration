import numpy as np  
import matplotlib.pyplot as plt  
plt.figure() # Create a new figure window
xlist = np.linspace(-2.0, 2.0, 100) # Create 1-D arrays for x,y dimensions
ylist = np.linspace(-2.0, 2.0, 100) 
X,Y = np.meshgrid(xlist, ylist) # Create 2-D grid xlist,ylist values
F = X**2 + Y**2 - 1  #  'Circle Equation
plt.contour(X, Y, F, [0], colors = 'k', linestyles = 'solid')
plt.show()
