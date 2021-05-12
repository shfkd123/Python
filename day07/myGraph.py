from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.array([2,3,2,3,5,2,3,2,3,5])
x = np.array([1,1,1,1,1,1,1,1,1,1])
y = np.array([0,1,2,3,4,5,6,7,8,9])

print(z) 

ax.plot3D(x, y, z, 'maroon')
ax.set_title('3D line plot')
plt.show()