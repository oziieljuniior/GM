import matplotlib.pyplot as plt

def on_press(event):
    print('you pressed', event.button, event.xdata, event.ydata)

cid = plt.figure().canvas.mpl_connect('button_press_event', on_press)

plt.show()