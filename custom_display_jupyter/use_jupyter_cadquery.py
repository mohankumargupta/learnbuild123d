# %%
import jupyter_cadquery.cad_display as cd
from jupyter_cadquery import show_object

from build123d import *

cd.SIDECAR.close()
cd.SIDECAR = None

box = Box(10,10,10)
show_object(box)

