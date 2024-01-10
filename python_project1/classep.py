from matplotlib.widgets import Slider
import matplotlib.pyplot as plt
import numpy as np


#Classe de pontos criada para salvar os pontos da janelas ao clicar
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#Classe salva os pontos onde o segmento deve ser criado, de maneira ordenada
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2        

#Clase organiza os pontos criados
class PontosArray:
    def __init__(self, points):
        self.points = points
    
    ponto_array = []
    
    def curvab(self):
        self.ponto_array.clear()
        for point in self.points:
            self.ponto_array.append([point.x, point.y])
        return self.ponto_array

#Classe cria uma curva de polígonos a partir de um segmento de pontos dados. 
class CPoligonos:
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
            name = "control_points" + str(n)
            name = control_points
            #print(name)
            lista = []
            lista = (1 - t)*name[:-1,:] + t*name[1:,:]
            control_points = np.array(lista)
            #print("new")
            #print(control_points)
            plt.scatter(name[:,0], name[:,1])
            plt.plot(name[:,0], name[:,1])
            n += 1    
        plt.scatter(control_points[:,0], control_points[:,1])
        
#Classe cria a curva de bézier
class Bezier:
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
                name = "control_points"+str(n)
                name = control_points
                lista = []
                lista = (1 - t)*name[:-1,:] + t*name[1:,:]
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

class CanvaBernstein:
    def __init__(self, n=None, control_points=None):
        self.n = n
        self.control_points = control_points
        self.bernstein_fig = plt.figure()
        self.bernstein_ax = self.bernstein_fig.add_subplot(111)
        self.bernstein_ax.set_xlim([0, 1])
        self.bernstein_ax.set_ylim([-10, 10])
        self.bernstein_ax.set_title("Polinômios de Bernstein")
        self.bernstein_fig.show() 
        
    def coef_binomial(self, n, k):
        return np.math.factorial(n) // (np.math.factorial(k) * np.math.factorial(n - k))

    def polinomio_bernstein(self, n, i, t):
        return self.coef_binomial(n, i) * t ** i * (1 - t) ** (n - i)
        
    def plot_bernstein(self):
        t = np.linspace(0, 1, 100)

        for i in range(self.n + 1):
            B = self.polinomio_bernstein(self.n, i, t)*self.control_points[i][1]
            self.bernstein_ax.plot(t, B, label=f'B_{i},{self.n}(t)')

        self.bernstein_ax.set_title(f'Polinômios de Bernstein de Grau {self.n}')
        self.bernstein_ax.set_xlabel('t')
        self.bernstein_ax.set_ylabel('B_i,n(t)')
        self.bernstein_ax.legend()
        self.bernstein_ax.grid()
        plt.show()
    
    def update_bernstein(self, control_points):
        self.control_points = control_points
        if self.bernstein_fig is not None and self.bernstein_ax is not None:
            self.bernstein_ax.clear()
            self.bernstein_ax.set_xlim([0, 1])
            self.bernstein_ax.set_ylim([-10, 10])

            t = np.linspace(0, 1, 100)

            for i in range(self.n + 1):
                B = self.polinomio_bernstein(self.n, i, t) * self.control_points[i][1]
                self.bernstein_ax.plot(t, B, label=f'B_{i},{self.n}(t)')

            self.bernstein_ax.set_title(f'Polinômios de Bernstein de Grau {self.n}')
            self.bernstein_ax.set_xlabel('t')
            self.bernstein_ax.set_ylabel('B_i,n(t)')
            self.bernstein_ax.legend()
            self.bernstein_ax.grid()
            self.bernstein_fig.canvas.draw_idle()

#Classe geral, cria a janela para criação e trabalho com a curva de bézier.  
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
        
        self.control_points_list = []

        self.cidpress1 = self.fig.canvas.mpl_connect('button_press_event', self.create)
        self.cidpress2 = self.fig.canvas.mpl_connect("button_release_event", self.on_release)
        self.cidpress3 = self.fig.canvas.mpl_connect("motion_notify_event", self.on_move)
        self.cidpress4 = self.fig.canvas.mpl_connect('key_press_event', self.menu)
        self.slider.on_changed(self.update)
        plt.show()
            
         
    points = []
    lines = []
    selected_point = None
    def update(self, val):
        #print("Valor atualizado")
        only = PontosArray(self.points).curvab()
        #print(len(only))
        if len(self.control_points_list) > 1:
            if len(only) > 2:
                #plt.cla()
                self.ax.set_xlim([-10,10])
                self.ax.set_ylim([-10,10])
                CPoligonos(only).cpoligono(val)
                Bezier(only).curve()
            self.t = val
        else:
            if len(only) > 2:
                plt.cla()
                self.ax.set_xlim([-10,10])
                self.ax.set_ylim([-10,10])
                CPoligonos(only).cpoligono(val)
                Bezier(only).curve()
            self.t = val
            
        if hasattr(self, 'bernstein_canva'):
            control_points = PontosArray(self.points).curvab()
            self.bernstein_canva.update_bernstein(control_points)
        
    def create(self, event):
        #print(event.button)
        trap = str(event.button)
        if trap == 'MouseButton.RIGHT':
            #print(event.button)
            #print('click x', event.xdata)
            #print('click y', event.ydata)
            point = Point(event.xdata, event.ydata)
            self.points.append(point)
            if len(self.points) > 1:
                line = Line(self.points[-2], self.points[-1])
                self.lines.append(line)
            for line in self.lines:
                plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
            plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'blue', s = 25)
            plt.show()
            #print([point.x for point in self.points], [point.y for point in self.points])
            if len(self.points) > 2:
                #print("Criar curva")
                only = PontosArray(self.points).curvab()
                if (len(only)) >= 3:
                    #print(len(only))
                    Bezier(only).curve().remove()
                    plt.cla()
                    self.ax.set_xlim([-10,10])
                    self.ax.set_ylim([-10,10])
                CPoligonos(only).cpoligono(self.t)
                Bezier(only).curve()
        elif trap == 'MouseButton.LEFT':
            #print("Hello")
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
            #print("point target")
            plt.cla()
            for line in self.lines:
                self.ax.set_xlim([-10,10])
                self.ax.set_ylim([-10,10])
                plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
            plt.scatter([point.x for point in self.points], [point.y for point in self.points])
            plt.show()
            if len(self.points) > 2:
                #print("Criar curva")
                only = PontosArray(self.points).curvab()
                if (len(only)) >= 3:
                    #print(len(only))
                    Bezier(only).curve().remove()
                    plt.cla()
                    self.ax.set_xlim([-10,10])
                    self.ax.set_ylim([-10,10])
                CPoligonos(only).cpoligono(self.t)
                Bezier(only).curve()
        
        if self.selected_point:
            # (Código existente)
            if hasattr(self, 'bernstein_canva'):
                control_points = PontosArray(self.points).curvab()
                self.bernstein_canva.update_bernstein(control_points)
        
    def menu(self, event):
        if event.key == 'd':
            print('Deletar todos os pontos e linhas da curva')
            plt.cla()
            self.ax.set_xlim([-10,10])
            self.ax.set_ylim([-10,10])
            self.points.clear()
            self.lines.clear()
            plt.show()
        
        elif event.key == 'm':
            print('Deletar último ponto')
            plt.cla()
            if len(self.points) <= 1:
                self.ax.set_xlim([-10,10])
                self.ax.set_ylim([-10,10])
                self.points.clear()
                plt.show()
                print("Sem pontos para remover")
                return
            self.points.pop()
            self.lines.pop()
            self.ax.set_xlim([-10,10])
            self.ax.set_ylim([-10,10])
            plt.show()
            
            if len(self.points) == 1:
                self.lines.clear()
            elif len(self.points) >= 2:
                self.lines.pop()
                line = Line(self.points[-2], self.points[-1])
                self.lines.append(line)
            for line in self.lines:
                plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
            plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'blue', s = 25)
            plt.show()
            #print([point.x for point in self.points], [point.y for point in self.points])
            if len(self.points) > 2:
                #print("Criar curva")
                only = PontosArray(self.points).curvab()
                if (len(only)) >= 3:
                    #print(len(only))
                    Bezier(only).curve().remove()
                    plt.cla()
                    self.ax.set_xlim([-10,10])
                    self.ax.set_ylim([-10,10])
                CPoligonos(only).cpoligono(self.t)
                Bezier(only).curve()
        
        elif event.key == 'b':
            print(event.key)
            self.openbernstein()
        
        elif event.key == 'n':
            print(event.key)
            self.split_curve(event)
    
    def openbernstein(self):
        n = len(self.points) - 1
        if n > 0:
            control_points = PontosArray(self.points).curvab()
            self.bernstein_canva = CanvaBernstein(n=n, control_points=control_points)
            self.bernstein_canva.plot_bernstein()
        else:
            print("Adicione pelo menos dois pontos de controle para visualizar os polinômios de Bernstein.")
            
    def split_curve(self, event):
        if len(self.points) < 4:
            print("Não há pontos suficientes para dividir a curva.")
            return
        #encontre o ponto de referência clicado pelo usuário
        selected_index = None
        for i, point in enumerate(self.points):
            if abs(event.xdata - point.x) < 0.5 and abs(event.ydata - point.y) < 0.5:
                selected_index = i
                print(selected_index)
                break

        if selected_index is None:
            print("Nenhum ponto selecionado")
            return
        
        #divide os pontos em duas listas com base no ponto de referencia
        left_points = self.points[:selected_index+1]
        right_points = self.points[selected_index:]
        self.control_points_list.append(self.points)
        self.control_points_list.append(left_points)
        self.control_points_list.append(right_points)
        print(self.control_points_list)
        plt.cla()
        #reinice o poligono de controle com os pontos da parte esquerda da divisão
        self.points = left_points
        #limpar as linhas existentes
        self.lines.clear()
        #desenhando as linhas com base nos novos pontos
        if len(self.points) > 1:
            line = Line(self.points[-2], self.points[-1])
            self.lines.append(line)
        print(len(self.lines))
        print(self.lines)
        for line in self.lines:
            plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
        plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'red', s=25)
        #plt.show
        if len(self.points) > 2:
            only = PontosArray(self.points).curvab()
            CPoligonos(only).cpoligono(self.t)
            Bezier(only).curve()
        
        #atualiza a exibição do gráfico
        plt.show()
        
        ##reinice o poligono de controle com os pontos da parte direita da divisão
        self.points = right_points
        #limpar as linhas existentes
        self.lines.clear()
        #desenhando as linhas com base nos novos pontos
        if len(self.points) > 1:
            line = Line(self.points[-2], self.points[-1])
            self.lines.append(line)
        print(len(self.lines))
        print(self.lines)
        for line in self.lines:
            plt.plot([line.point1.x, line.point2.x], [line.point1.y, line.point2.y])
        plt.scatter([point.x for point in self.points], [point.y for point in self.points], color = 'red', s=25)
        #plt.show
        if len(self.points) > 2:
            only = PontosArray(self.points).curvab()
            CPoligonos(only).cpoligono(self.t)
            Bezier(only).curve()
        
        #atualiza a exibição do gráfico
        plt.show()
        
