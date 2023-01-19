import matplotlib.pyplot as plt

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
selected_point = None

def on_press(event):
    global selected_point
    for point in points:
        if abs(event.xdata-point.x)<0.1 and abs(event.ydata-point.y)<0.1:
            selected_point = point
            break

def on_release(event):
    global selected_point
    selected_point = None

def on_move(event):
    global selected_point
    if selected_point:
        selected_point.x = event.xdata
        selected_point.y = event.ydata
        plt.cla()
        for line in lines:
            plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
        plt.scatter([point.x for point in points], [point.y for point in points])
        plt.draw()

plt.connect("button_press_event", on_press)
plt.connect("button_release_event", on_release)
plt.connect("motion_notify_event", on_move)
plt.show()
