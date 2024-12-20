# %%
from build123d import *
from math import atan2

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as footrest_builder:
    with BuildSketch(Plane.XZ) as side_sketch:
        Rectangle(220,70, align=(Align.MAX, Align.MIN))
        with Locations((70-220,70)):
            Triangle(a=70, b=70, C=90, rotation=-90, align=(Align.MIN, Align.MAX), mode=Mode.SUBTRACT)
    extrude(amount=100)

footrest = footrest_builder.part
footrest
# %%
print(f"Area of face: {side_sketch.face().area}")

# %%
with BuildSketch(Plane.XZ) as side_sketch2:
    with BuildLine() as lines2:
        pts = [
            (0,0),
            (0,50),
            (-220,50),
            (-170,0)
        ]
        Polyline(pts, close=True)
    face = make_face()

print(f"Area of face: {side_sketch2.face().area}")

