# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# 2. Plate with Hole

# %%
from build123d import *

length, width, thickness = 80.0, 60.0, 10.0
center_hole_dia = 22.0

with BuildPart() as ex2:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)

ex2.part
# %% [markdown]
"""
# 2. Plate with Hole(Variation 1)
  Create a hole through the whole part without specifying the depth.
  Because Box is centered on all axes(including z-axis), the top of the box is depth/2 from origin.  
"""

# %%
with BuildPart() as ex2b:
    Box(length, width, thickness)
    with Locations(Plane.XY.offset(thickness/2)):
        Hole(radius=center_hole_dia / 2)

ex2b.part


# %%
from math import isclose
assert isclose(ex2.solid().volume, ex2b.solid().volume)
