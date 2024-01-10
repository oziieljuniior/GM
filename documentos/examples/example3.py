import matplotlib.pyplot as plt

# Create a figure
fig = plt.figure()

# Create an empty Cartesian plane
ax = fig.add_subplot(111)

# Set the limits of the plane
ax.set_xlim([-10, 10])
ax.set_ylim([-10, 10])

# Plot the plane
ax.plot()

# Function that creates a point when a mouse click is detected
def onclick(event):
    print('click', event)
    plt.scatter(event.xdata, event.ydata, color = 'red', s = 20)
    plt.show()

# Connect the function to the plot
cid = fig.canvas.mpl_connect('button_press_event', onclick)

# Show the plot
plt.show()