import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh
import numpy as np
import tripy

# Carregar o novo arquivo STL
stl_file_path = '/home/darkcover/Documentos/GitHub/GM/python_project3/data/2/low-poly-cat20180403-346-1hoou15/RubixDesign/low-poly-cat/cat2.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

# Obter as coordenadas dos vértices
vertices = np.vstack(mesh_data.vectors)

# Aplicar a triangularização de Delaunay usando o tripy
triangles = tripy.earclip(vertices[:, :2])  # Somente coordenadas x e y

# Criar a figura 3D com a malha simplificada
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces da malha simplificada
mesh_faces = Poly3DCollection(triangles, facecolors='cyan', linewidths=0, alpha=0.7, edgecolors='none')
ax.add_collection3d(mesh_faces)

# Ajustar os limites do eixo
ax.set_xlim([vertices[:, 0].min(), vertices[:, 0].max()])
ax.set_ylim([vertices[:, 1].min(), vertices[:, 1].max()])
ax.set_zlim([vertices[:, 2].min(), vertices[:, 2].max()])

# Mostrar a figura
plt.show()

