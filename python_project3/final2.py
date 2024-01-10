import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh
import numpy as np
from scipy.spatial import Delaunay

# Carregar o novo arquivo STL
stl_file_path = '/home/darkcover/Documentos/GitHub/GM/python_project3/data/2/low-poly-cat20180403-346-1hoou15/RubixDesign/low-poly-cat/cat2.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

# Obter os vértices da malha
vertices = mesh_data.vectors.reshape((-1, 3))

# Suavização da malha - Laplacian Smoothing
num_iterations = 2
for _ in range(num_iterations):
    # Calcular a média dos vértices vizinhos e atualizar as coordenadas
    vertices = (vertices + np.roll(vertices, shift=-1, axis=0) + np.roll(vertices, shift=1, axis=0)) / 3.0

# Triangulação de Delaunay dos vértices após a suavização
tri = Delaunay(vertices[:, :2])

# Obter as triângulos a partir da triangulação
triangles = vertices[tri.simplices]

# Criar a figura 3D com a malha completa
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces da malha
mesh_faces = Poly3DCollection(triangles, alpha=0.1, edgecolor='r')
ax.add_collection3d(mesh_faces)

# Ajustar os limites do eixo
ax.set_xlim([vertices[:, 0].min(), vertices[:, 0].max()])
ax.set_ylim([vertices[:, 1].min(), vertices[:, 1].max()])
ax.set_zlim([vertices[:, 2].min(), vertices[:, 2].max()])

# Mostrar a figura
plt.show()
