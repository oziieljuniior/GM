import numpy as np
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

t = float(input("Insira o valor de t: "))

# Define the control points for the Bezier curve
control_points = np.array([[0, 0], [3, 4], [6, 0], [9,4]])
print(control_points)
print(type(control_points))

# Create a Bezier path with the control points
path = mpath.Path(control_points, codes=[1, 2, 2, 2])
print(path)
print(type(path))

#np = []
list = []
for i in range(0,len(control_points) - 1):
    #print(control_points[i])
    simple_array = control_points[i] + (t*(control_points[i + 1] - control_points[i]))
    list.append(simple_array)
#print(np.array(list))       

#calculus
#t = 0.5
control_points1 = np.array(list)
print(control_points1)
print(type(control_points1))

path1 = mpath.Path(control_points1, codes=[1, 2, 2])
print(path1)
print(type(path1))

list = []
for i in range(0,len(control_points1) - 1):
    #print(control_points[i])
    simple_array = control_points1[i] + (t*(control_points1[i + 1] - control_points1[i]))
    list.append(simple_array)
#print(np.array(list))

control_points2 = np.array(list)
print(control_points2)
print(type(control_points2))

path2 = mpath.Path(control_points2, codes=[1, 2])
print(path2)
print(type(path2))


fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor='none', lw=2)
patch1 = mpatches.PathPatch(path1, facecolor='blue', lw=2)
patch2 = mpatches.PathPatch(path2, facecolor='red', lw=2)
ax.add_patch(patch)
ax.add_patch(patch1)
ax.add_patch(patch2)

# Plot the control points
plt.scatter(control_points[:,0], control_points[:,1])
plt.scatter(control_points1[:,0], control_points1[:,1])
plt.scatter(control_points2[:,0], control_points2[:,1])

plt.xlim(-3,12)
plt.ylim(-3,12)
plt.show()
