import numpy as np
import matplotlib.pyplot as plt

t = float(input('Insira t: '))
control_points = eval(input("Insira os pontos: "))
control_points = np.array(control_points)
tam = len(control_points)
plt.scatter(control_points[:,0], control_points[:,1])
plt.plot(control_points[:,0], control_points[:,1])
n = 1

while tam > n:
    if tam > n:
        name = "control_points" + str(n)
        name = control_points
        print(n)
        print(name)
        list = []
        for i in range(0, len(name) - 1):
            simple_array = name[i] +(t*(name[i+1]-name[i]))
            list.append(simple_array)
        control_points = np.array(list)
        print("new")
        print(control_points)
        plt.scatter(name[:,0], name[:,1])
        plt.plot(name[:,0], name[:,1])
        n = n + 1
    plt.scatter(control_points[:,0], control_points[:,1])
plt.show()

