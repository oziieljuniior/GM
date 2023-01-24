import numpy as np
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import matplotlib.path as mpath

t = float(input("Valor de t: "))
control_point = np.array(eval(input("Pontos: ")))

print(control_point)
print(t)
print(type(control_point))
print(len(control_point))


a = np.ones(len(control_point), dtype = int)
for i in range(1, len(control_point)):
    a[i] = 2
path = mpath.Path(control_point, codes= a)

print(a)


fig, ax = plt.subplots()
patch = mpatches.PathPatch(path, facecolor = 'None', lw = 1)

ax.add_patch(patch)

plt.scatter(control_point[:,0], control_point[:,1])
plt.xlim(0,5)
plt.ylim(0,5)
plt.show()