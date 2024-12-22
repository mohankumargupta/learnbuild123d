# %%

# %%
import OCP
import pyvista as pv
from build123d import *

# %%
box = Box(10,10,10)
b = Compound.make_compound(box)


# %%
vs = OCP.IVtkOCC.IVtkOCC_Shape(b.wrapped)
sd = OCP.IVtkVTK.IVtkVTK_ShapeData()
sm = OCP.IVtkOCC.IVtkOCC_ShapeMesher()
sm.Build(vs,sd)

# %%
res = sd.getVtkPolyData()

# %%
mesh = pv.PolyData(res)
pv.plot(mesh, smooth_shading=True)
