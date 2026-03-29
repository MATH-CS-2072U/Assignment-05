import numpy as np
import matplotlib.pyplot as plt
from LS import *

# Data from question 2:
xs = np.array([-1.00, 0.200, 2.40, 3.60, 4.70])
ys = np.array([-1.400, 0.60, 2.60, 4.1, 5.15])
P, a = LS( ... )
xPlot = np.linspace( ... )
yPlot = P( ... )
plt.plot(xs,ys, ... )
plt.plot(xPlot,yPlot, .. )
plt.xlabel('x')
plt.ylabel('y')
plt.show()
err = 0.0
for i in range(5):
    err += ...                               
print('Least squares error is %e.' % (err))
