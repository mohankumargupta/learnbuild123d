# %%
from build123d import *

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as footrest_builder:
    with BuildSketch(Plane.YZ) as side_sketch:
        with BuildLine() as side_lines:
            '''
            pts = [
                (0,0),
                (70,0),
                (0,50),
                (0,0)
            ]
            Polyline(pts)
            '''
            l1 = Line((0,50),(70,50))
            l2 = Line(l1@1, (0,0))
            Line(l2@1, l1@0)
        make_face()
    extrude(amount=LENGTH)
footrest = footrest_builder.part
footrest

# %%
print(footrest.volume)
