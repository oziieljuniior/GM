# GM

Anotações e desenvolvimentos de códigos do curso de verão em modelagem geométrica. Aqui estão alguns exemplos de códigos que estudamos durante a aula.
Organização do projeto: 
- Examples: Contém os arquivos de construção do código principal. Nesta pasta, você deve encontrar exemplos de arquivos .py e .ipynb que foram elaborados a partir de exemplos e testes para a construção do código principal;
- Pictures: Contém imagens e vídeos mostrando teste realizados;
- Python_Project: Pasta principal, contém o arquivo principal do projeto - classep.py. O arquivo init.py é o arquivo de teste da classep.py
- Slider: Contém um arquivo chamado Apresentation(1), nele é possível visualizar uma apresentação elaborada com as informações da construção do trabalho.

## Interactive Bezier Curve Creator
Este projeto é uma implementação em Python para a criação e manipulação de curvas de Bézier interativas utilizando a biblioteca Matplotlib. Ele permite que o usuário insira pontos de controle com o botão direito do mouse e mova os pontos de controle com o botão esquerdo do mouse. Além disso, é possível usar teclas para apagar pontos de controle e limpar a tela.

# Classes e Métodos
Aqui está uma análise das classes e métodos presentes no código:

** Classe Point: Usada para armazenar as coordenadas x e y dos pontos de controle.
** Classe Line: Armazena dois pontos para representar um segmento de linha.
** Classe pontos_array: Organiza os pontos de controle e retorna uma lista de coordenadas.
** Classe cpoligonos: Desenha uma curva de polígonos com base nos pontos de controle.
** Classe bezier: Cria a curva de Bézier usando um conjunto de pontos de controle.
** Classe Canva: Responsável pela criação da interface gráfica e manipulação dos eventos.

#Como Usar
Clone este repositório ou baixe o arquivo .py.
Instale as dependências necessárias usando pip install matplotlib numpy.
Execute o arquivo init.py em seu ambiente Python.
Utilize o botão direito do mouse para criar pontos de controle.
Utilize o botão esquerdo do mouse para mover os pontos de controle.
Use as teclas 'd' para apagar todos os pontos de controle e 'm' para apagar o último ponto adicionado.

# Dependências
Python 3
Matplotlib
NumPy
