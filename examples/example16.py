import tkinter as tk 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

root = tk.Tk()
root.title('Exemplo de menu do Matplotlib')

fig = Figure(figsize=(5,4), dpi = 100)
ax = fig.add_subplot(111)
ax.plot([1,2,3],[2,4,3])

canvas = FigureCanvasTkAgg(fig, master = root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
toolbar.pack()

def on_button_click():
    print('Botão do menu clicado!')

for item in toolbar.winfo_children():
    if isinstance(item, tk.Menu):
        if item.index('end') == 1 and item.entrycget(0, 'label') == 'Pan':
            pan_menu = item
            pan_menu.add_command(label='Clique Aqui', command=on_button_click)

tk.mainloop()
