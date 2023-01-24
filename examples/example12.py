import numpy as np
import matplotlib.pyplot as plt

t = float(input("Insira t: "))
control_points = np.array([[0, 0], [3, 4], [6, 0], [9,4]])
print(control_points)

plt.scatter(control_points[:,0], control_points[:,1])
plt.plot(control_points[:,0], control_points[:,1])

list = []
for i in range(0,len(control_points) - 1):
    #print(control_points[i])
    simple_array = control_points[i] + (t*(control_points[i + 1] - control_points[i]))
    list.append(simple_array)
control_points1 = np.array(list)
plt.scatter(control_points1[:,0], control_points1[:,1])
plt.plot(control_points1[:,0], control_points1[:,1])

list = []
for i in range(0,len(control_points1) - 1):
    #print(control_points[i])
    simple_array = control_points1[i] + (t*(control_points1[i + 1] - control_points1[i]))
    list.append(simple_array)
control_points2 = np.array(list)
plt.scatter(control_points2[:,0], control_points2[:,1])
plt.plot(control_points2[:,0], control_points2[:,1])

list = []
for i in range(0,len(control_points2) - 1):
    #print(control_points[i])
    simple_array = control_points2[i] + (t*(control_points2[i + 1] - control_points2[i]))
    list.append(simple_array)
control_points3 = np.array(list)
plt.scatter(control_points3[:,0], control_points3[:,1])
plt.plot(control_points3[:,0], control_points3[:,1])


plt.show()