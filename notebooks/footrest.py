# %%
from build123d import *
from math import atan2

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as footrest_builder:
    with BuildSketch(Plane.YZ) as side_sketch:
        with BuildLine() as side_lines:
            l1 = Line((0,50),(70,50))
            l2 = Line(l1@0, (0,0))
            l3 = PolarLine(l1@1, length=7, direction=Vector(-70,-50).normalized())
            l4 = PolarLine(l2@1, length=7, direction=Vector(70,50).normalized())
            l5 = RadiusArc(l3@1, l4@1,radius=-120.)
        face = make_face()
    extrude(amount=LENGTH)
footrest = footrest_builder.part
footrest

# %%
print(footrest.volume)
#export_stl(footrest, "footrest.stl")
export_step(footrest, "footrest.step")
print(face.area)
print(f"center: x: {l5.arc_center.X} y: {l5.arc_center.Y}")
l3vertices = l3.vertices()
print(l3vertices)

# %%
normalizedvector = Vector(-70,-50).normalized()
print(normalizedvector)
