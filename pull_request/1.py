# %%


from build123d import *
from display_patch import shape_to_html

box = Box(10,10,10)
shape_to_html(box)


# %%
from build123d import *
cylinder = Cylinder(radius=10, height=50)
shape_to_html(cylinder)

