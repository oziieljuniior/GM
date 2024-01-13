import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
from scipy.spatial import KDTree
from stl import mesh

def geodesic_centroid(vertices):
    center = np.mean(vertices, axis=0)
    normalized_vertices = vertices - center
    angles = np.arctan2(normalized_vertices[:, 1], normalized_vertices[:, 0])
    sorted_indices = np.argsort(angles)
    sorted_vertices = normalized_vertices[sorted_indices]
    centroid = np.mean(sorted_vertices, axis=0) + center
    return centroid

# Carregar a malha STL
#/home/darkcover/Documentos/GitHub/GM/python_project3/data/2/low-poly-moai20180403-9092-1jsjdxy/RubixDesign/low-poly-moai/moai.stl
stl_file_path = '/home/oziel/Documentos/Mestrado/UFAM/Verao/Modelagem_2023/GM/python_project3/data/2/low-poly-moai20180403-9092-1jsjdxy/RubixDesign/low-poly-moai/moai.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

# Calcular as normais das faces
normals = np.cross(mesh_data.vectors[:, 1, :] - mesh_data.vectors[:, 0, :], mesh_data.vectors[:, 2, :] - mesh_data.vectors[:, 0, :])
normals /= np.linalg.norm(normals, axis=1)[:, None]

# Criar um KDTree a partir dos vértices da malha
tree = KDTree(mesh_data.vectors.reshape(-1, 3))

# Segmentar a malha
# Definir um raio de vizinhança
radius = 10

# Criar um array para armazenar as normais das faces segmentadas
segmented_vertices = np.copy(mesh_data.vectors)

# Percorrer todos os vértices da malha:
for i, vertex in enumerate(mesh_data.vectors):
    # Encontrar os vizinhos do vértice
    neighbors = tree.query_ball_point(vertex, radius)
    
    # Filtrar os vizinhos para garantir que estejam dentro dos limites da matriz de vértices
    valid_neighbors = [n for n in neighbors if isinstance(n, int) and n < len(mesh_data.vectors)]
    
    # Se o vértice tiver mais de um vizinho, atualizá-lo para a média dos vértices vizinhos
    if len(valid_neighbors) > 1:
        segmented_vertices[i] = np.mean(mesh_data.vectors[valid_neighbors], axis=0)

# Salvar a malha segmentada
mesh_data.vectors = segmented_vertices
mesh_data.save("moai_segmented.stl")

# Salvar a malha segmentada
mesh_data.vectors = segmented_vertices
mesh_data.save("moai_segmented.stl")


# Visualizar a malha segmentada
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces da malha com iluminação
mesh_faces = Poly3DCollection(mesh_data.vectors, facecolors=plt.cm.viridis(normals[:, 2]))
ax.add_collection3d(mesh_faces)

# Ajustar os limites do eixo
ax.set_xlim([mesh_data.x.min(), mesh_data.x.max()])
ax.set_ylim([mesh_data.y.min(), mesh_data.y.max()])
ax.set_zlim([mesh_data.z.min(), mesh_data.z.max()])

# Mostrar a figura
plt.show()
