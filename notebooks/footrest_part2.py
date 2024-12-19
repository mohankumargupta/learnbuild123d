# %%
from build123d import *
from math import atan2

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as footrest_builder:
    with BuildSketch(Plane.XZ) as side_sketch:
        # with BuildLine() as lines:
        #     pts = [
        #         (0,0),
        #         (0,50),
        #         (-220,50),
        #         (-170,0)
        #     ]
        #     Polyline(pts, close=True)
        #make_face()
        Rectangle(220,50, align=(Align.MAX, Align.MIN))
        with Locations((-170,0)):
            Triangle(a=50, b=50, C=90, rotation=180, align=(Align.MIN, Align.MAX), mode=Mode.SUBTRACT)
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
