from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2        
   
class pontos_array:
    def __init__(self, points):
        self.points = points
    
    ponto_array = []
    
    def curvab(self):
        self.ponto_array.clear()
        for point in self.points:
            self.ponto_array.append([point.x, point.y])
        return self.ponto_array

class cpoligonos:
    def __init__(self, pontos):
        self.pontos = pontos
    
    geral = []   
    
    def cpoligono(self, t):
        control_points = np.array(self.pontos)
        #print(t)
        tam = len(control_points)
        #print(control_points)
        n = 1
        while tam > n:
            if tam > n:
                name = "control_points" + str(n)
                name = control_points
                print(name)
                lista = []
                for i in range(0, len(name) - 1):
                    print(name[i], name[i + 1])
                    simple_array = name[i] + (t*(name[i + 1] - name[i]))
                    lista.append(simple_array)
                control_points = np.array(lista)
                print("new")
                print(control_points)
                plt.scatter(name[:,0], name[:,1])
                plt.plot(name[:,0], name[:,1])
                n += 1
        plt.scatter(control_points[:,0], control_points[:,1])
        
   
class bezier:
    def __init__(self, pontos = None):
        self.pontos = pontos
    final = []
    
            
    def curve(self):
        control_points = np.array(self.pontos)
        controle = np.array(self.pontos)
        tam = len(control_points)
        t1 = np.linspace(0,1, 100)
        self.final.clear()
        for t in t1:
            control_points = controle
            n = 1
            while tam > n:
                if tam > n:
                    name = "control_points"+str(n)
                    name = control_points
                    lista = []
                    for i in range(0, len(name) - 1):
                        simple_array = name[i] + (t*(name[i + 1] - name[i]))
                        lista.append(simple_array)
                    control_points = np.array(lista)
                    n += 1
            self.final.append(control_points)
        final1 = []
        for j in range(0, len(self.final)):
            for k in range(0, len(self.final[j])):
                final1.append(self.final[j][k])
        self.final = np.array(final1)
        line, = plt.plot(self.final[:,0], self.final[:,1]) 
        return line
        
    
            

        
class Canva:
    def __init__(self, t = 0.15):
        self.t = t
        
        self.fig = plt.figure()
        self.ax_slider = plt.axes([0.15, 0.02, 0.65, 0.03])
        self.slider = Slider(self.ax_slider, 't', 0.01, 1, valinit = self.t)
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim([-10,10])
        self.ax.set_ylim([-10,10])
        self.ax.plot()
        
        self.cidpress1 = self.fig.canvas.mpl_connect('button_press_event', self.create)
        self.cidpress2 = self.fig.canvas.mpl_connect("button_release_event", self.on_release)
        self.cidpress3 = self.fig.canvas.mpl_connect("motion_notify_event", self.on_move)
        self.slider.on_changed(self.update)
        plt.show()
            
         
    points = []
    lines = []
    selected_point = None
    def update(self, val):
        print("Valor atualizado")
        only = pontos_array(self.points).curvab()
        print(len(only))
        if len(only) > 2:
            plt.cla()
            self.ax.set_xlim([-10,10])
            self.ax.set_ylim([-10,10])
            cpoligonos(only).cpoligono(val)
            bezier(only).curve()
        self.t = val
            
        
        
    def create(self, event):
        print(event.button)
        trap = str(event.button)
        if trap == 'MouseButton.RIGHT':
            print(event.button)
            print('click x', event.xdata)
            print('click y', event.ydata)
            point = Point(event.xdata, event.ydata)
            self.points.append(point)
            if len(self.points) > 1:
                line = Line(self.points[-2], self.points[-1])
                self.lines.append(line)
            for line in self.lines:
                plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
            plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'blue', s = 25)
            plt.show()
            print([point.x for point in self.points], [point.y for point in self.points])
            if len(self.points) > 2:
                print("Criar curva")
                only = pontos_array(self.points).curvab()
                if (len(only)) >= 3:
                    print(len(only))
                    bezier(only).curve().remove()
                    plt.cla()
                    self.ax.set_xlim([-10,10])
                    self.ax.set_ylim([-10,10])
                cpoligonos(only).cpoligono(self.t)
                bezier(only).curve()
        elif trap == 'MouseButton.LEFT':
            print("Hello")
            for point in self.points:
                if abs(event.xdata-point.x)<0.1 and abs(event.ydata-point.y)<0.1:
                    self.selected_point = point
                    break
    
    def on_release(self, event):
        self.selected_point = None
    
    def on_move(self, event):
        if self.selected_point:
            self.selected_point.x = event.xdata
            self.selected_point.y = event.ydata
            plt.cla()
            for line in self.lines:
                self.ax.set_xlim([-10,10])
                self.ax.set_ylim([-10,10])
                plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
            plt.scatter([point.x for point in self.points], [point.y for point in self.points])
            plt.show()
            if len(self.points) > 2:
                print("Criar curva")
                only = pontos_array(self.points).curvab()
                if (len(only)) >= 3:
                    print(len(only))
                    bezier(only).curve().remove()
                    plt.cla()
                    self.ax.set_xlim([-10,10])
                    self.ax.set_ylim([-10,10])
                cpoligonos(only).cpoligono(self.t)
                bezier(only).curve()

                
            
    