import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from stl import mesh

# Carregar o novo arquivo STL
stl_file_path = '/home/darkcover/Documentos/GitHub/GM/python_project3/data/2/low-poly-cat20180403-346-1hoou15/RubixDesign/low-poly-cat/cat2.stl'
mesh_data = mesh.Mesh.from_file(stl_file_path)

# Criar a figura 3D com a malha completa
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adicionar as faces da malha
mesh_faces = Poly3DCollection(mesh_data.vectors)
ax.add_collection3d(mesh_faces)

# Ajustar os limites do eixo
ax.set_xlim([mesh_data.x.min(), mesh_data.x.max()])
ax.set_ylim([mesh_data.y.min(), mesh_data.y.max()])
ax.set_zlim([mesh_data.z.min(), mesh_data.z.max()])

# Mostrar a figura
plt.show()
