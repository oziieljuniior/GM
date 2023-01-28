import matplotlib.pyplot as plt
fig = plt.figure()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

points = []
lines = []

def on_click(event):
    point = Point(event.xdata, event.ydata)
    points.append(point)
    if len(points) > 1:
        line = Line(points[-2], points[-1])
        lines.append(line)
    plt.cla()
    for line in lines:
        plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
    plt.scatter([point.x for point in points], [point.y for point in points])
    plt.show()

plt.connect("button_press_event", on_click)
plt.show()


