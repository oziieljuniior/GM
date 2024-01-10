import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, lambdify

# Criar a janela principal
root = tk.Tk()
root.title('Dashboard-original')

# Função para criar o gráfico 3D
def create_3d_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Dados de exemplo em terceira dimensão
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))

    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Gráfico 3D')

    # Criar uma nova janela para visualização gráfica
    graph_window = tk.Toplevel(root)
    graph_window.title('Visualização 3D')

    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.get_tk_widget().pack()

# Função para criar uma nova janela com a opção de adicionar uma função
def open_function_window():
    def plot_user_function():
        user_function = entry_function.get()
        if user_function:
            x, y = symbols('x y')
            z = eval(user_function)
            z_func = lambdify((x, y), z, 'numpy')

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
            Z = z_func(X, Y)
            ax.plot_surface(X, Y, Z, cmap='viridis')

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.set_title('Gráfico 3D com Função do Usuário')

            # Criar uma nova janela para visualização gráfica
            graph_window = tk.Toplevel(root)
            graph_window.title('Visualização 3D')

            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.get_tk_widget().pack()

    function_window = tk.Toplevel(root)
    function_window.title('Inserir Função')

    label_function = ttk.Label(function_window, text='Digite a função (ex: np.sin(np.sqrt(x**2 + y**2)))')
    label_function.pack(pady=10)

    entry_function = ttk.Entry(function_window)
    entry_function.pack(pady=10)

    plot_button = ttk.Button(function_window, text='Plotar Função', command=plot_user_function)
    plot_button.pack(pady=10)

# Função para fechar a aplicação
def quit_app():
    root.quit()

# Criar botão para criar o gráfico 3D
plot_button = ttk.Button(root, text='Criar Gráfico 3D', command=create_3d_plot)
plot_button.pack(pady=20)

# Adicionar botão para abrir uma nova janela com a opção de adicionar uma função
function_button = ttk.Button(root, text='Adicionar Função', command=open_function_window)
function_button.pack(pady=20)

# Adicionar botão para fechar a aplicação
quit_button = ttk.Button(root, text='Quit', command=quit_app)
quit_button.pack(pady=20)

# Iniciar a interface gráfica
root.mainloop()
