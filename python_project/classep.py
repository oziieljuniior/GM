import matplotlib.pyplot as plt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2        
   
   
class Canva:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)
        self.ax.set_xlim([-10,10])
        self.ax.set_ylim([-10,10])
        self.ax.plot()
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        plt.show()
    
    points = []
    lines = []
    
                    
    def onclick(self, event):
        print('click', event)
        point = Point(event.xdata, event.ydata)
        self.points.append(point)
        if len(self.points) > 1:
            line = Line(self.points[-2], self.points[-1])
            self.lines.append(line)
        for line in self.lines:
            plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
        plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'blue', s = 25)
        plt.show()
    

