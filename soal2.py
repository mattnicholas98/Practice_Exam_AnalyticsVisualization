# Soal 2 - SPLTV (Sistem Persamaan Linear Tiga Variabel)
#---------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# x - 2y + z = 6
# 3x + y - 2z = 4
# 7x - 6y - z = 10

# calculating the equations
a = np.array([[1, -2, 1], [3, 1, -2], [7, -6, -1]])

b = np.array([6, 4, 10])
c = np.linalg.solve(a, b)

x = round(c[0])
y = round(c[1])
z = round(c[2])

print(f'Nilai x = {x}')
print(f'Nilai y = {y}')
print(f'Nilai z = {z}')


# equation for the graph

# 1st equation - subtitute values to 0 to find each intercept points
x1 = np.array([[6/a[0][0], 0, 0]])
y1 = np.array([[0, 6/a[0][1], 0]])
z1 = np.array([[0, 0, 6/a[0][2]]])

# 2nd equation
x2 = np.array([[4/a[1][0], 0, 0]])
y2 = np.array([[0, 4/a[1][1], 0]])
z2 = np.array([[0, 0, 4/a[1][2]]])

# 3rd equation
x3 = np.array([[10/a[2][0], 0, 0]])
y3 = np.array([[0, 10/a[2][1], 0]])
z3 = np.array([[0, 0, 10/a[2][2]]])


# plotting the graph based on the equations above
plt.figure('Graphs')

# 1st graph based on the 1st equation
graph1 = plt.subplot(131, projection = '3d')
graph1.scatter(x1, y1, z1, color='g')
graph1.plot_wireframe(x1, y1, z1, facecolors='g', alpha=0.5)
graph1.set_xlabel('Nilai X')
graph1.set_ylabel('Nilai Y')
graph1.set_zlabel('Nilai Z')
graph1.set_title('x - 2y + z = 6')

# 2nd graph based on the 2nd equation
graph2 = plt.subplot(132, projection = '3d')
graph2.scatter(x2, y2, z2, color='r')
graph2.plot_wireframe(x2, y2, z2, facecolors='r', alpha=0.5)
graph2.set_xlabel('Nilai X')
graph2.set_ylabel('Nilai Y')
graph2.set_zlabel('Nilai Z')
graph2.set_title('3x + y - 2z = 4')

# 3rd graph based on the 3rd equation
graph3 = plt.subplot(133, projection = '3d')
graph3.scatter(x3, y3, z3, color='b')
graph3.plot_wireframe(x3, y3, z3, facecolors='b', alpha=0.5)
graph3.set_xlabel('Nilai X')
graph3.set_ylabel('Nilai Y')
graph3.set_zlabel('Nilai Z')
graph3.set_title('7x - 6y - z = 10')

plt.show()