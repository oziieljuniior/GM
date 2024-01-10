from mayavi import mlab
import os

os.environ['ETS_TOOLKIT'] = 'wx'

# Carregando o arquivo STL
stl_file_path = '/data/Escuttos_Curvos_Speis_Marinis_Primiris_HeressyOfHorrus_6036682/files/shield1_concave.stl'
mesh = mlab.pipeline.open(stl_file_path)

# Visualizando o modelo STL
mlab.pipeline.surface(mesh)
mlab.show()
