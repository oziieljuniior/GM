import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh
import numpy as np
from scipy.interpolate import griddata

def interpolate_vertices(mesh_data, factor=2):
    new_vertices = []
    for face in mesh_data.vectors:
        for i in range(3):
            v1 = face[i]
            v2 = face[(i + 1) % 3]
            for j in range(1, factor):
                alpha = j / factor
                new_vertex = (1 - alpha) * v1 + alpha * v2
                new_vertices.append(new_vertex)
    return np.vstack([mesh_data.vectors.reshape(-1, 3), np.array(new_vertices)])

stl_file_path = '/home/oziel/Documentos/Mestrado/UFAM/Verao/Modelagem_2023/GM/python_project3/data/2/low-poly-moai20180403-9092-1jsjdxy/RubixDesign/low-poly-moai/moai.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

# Interpolar vértices
interpolated_vertices = interpolate_vertices(mesh_data, factor=2)

# Calcular as normais das faces
normals = np.cross(interpolated_vertices[::3] - interpolated_vertices[1::3], interpolated_vertices[2::3] - interpolated_vertices[1::3])
normals /= np.linalg.norm(normals, axis=1)[:, None]

# Organizar os vértices e normais antes de criar Poly3DCollection
verts = interpolated_vertices.reshape(-1, 3)
normals = normals.flatten()

# Criar a figura 3D com a malha interpolada
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces da malha interpolada com iluminação
mesh_faces = Poly3DCollection([verts[i:i+3] for i in range(0, len(verts), 3)], facecolors=plt.cm.viridis(normals))
ax.add_collection3d(mesh_faces)

# Ajustar os limites do eixo
ax.set_xlim([verts[:, 0].min(), verts[:, 0].max()])
ax.set_ylim([verts[:, 1].min(), verts[:, 1].max()])
ax.set_zlim([verts[:, 2].min(), verts[:, 2].max()])

# Mostrar a figura
plt.show()
