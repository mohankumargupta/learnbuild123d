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
"""
# 2. Plate with Hole

   - Box and Cylinder are 3d objects
   - The box and cylinder are "centered" by default along all three axes. 
"""
# %%
from build123d import *

length, width, thickness = 80.0, 60.0, 10.0
center_hole_dia = 22.0


with BuildPart() as ex2:
    Box(length, width, thickness)
    Cylinder(radius=center_hole_dia / 2, height=thickness, mode=Mode.SUBTRACT)

ex2.part
