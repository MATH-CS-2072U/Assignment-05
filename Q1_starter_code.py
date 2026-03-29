import numpy as np
import scipy.interpolate as int
import matplotlib.pyplot as plt
xs = np.array([-1.50, 0.500, 1.20, 3.10, 4.60])
ys = np.array([-0.400, 1.60, 6.60, 11.0, 12.03])
S = int.CubicSpline(...)
xPlot = np.linspace(...)
yPlot = S.__call__(...)
dSdx = ...
yPlot2 = dSdx(...)
dSdxdx = ...
yPlot3 = dSdxdx(...)
dSdxdxdx = ...
yPlot4 = dSdxdxdx(...)
plt.plot(xPlot,yPlot,...)
plt.plot(xPlot,yPlot2,...)
plt.plot(xPlot,yPlot3,...)
plt.plot(xPlot,yPlot4,...)
plt.plot(xs,ys,'.',...)
plt.legend()
plt.xlabel(...)
plt.ylabel(...)
plt.title('Cubic spline interpolant and its derivatives')
plt.show()
