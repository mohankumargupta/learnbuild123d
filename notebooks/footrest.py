# %%
from build123d import *

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildSketch() as sketch:
    with BuildLine() as line:
        l1 = Line((0,50),(70,50))
        l2 = Line(l1@0, (0,0))
        l3 = PolarLine(l1@1, length=7, direction=(-1.0,-50./70), length_mode=LengthMode.DIAGONAL)
        l4 = PolarLine(l2@1, length=7, direction=(1.0,50./70), length_mode=LengthMode.DIAGONAL)
        l5 = SagittaArc(l3@1, l4@1, sagitta=-5.531)
    face = make_face()

with BuildPart() as footrest_builder:
    with BuildSketch(Plane.YZ) as side_sketch:
        with BuildLine() as side_lines:
            l1 = Line((0,50),(70,50))
            l2 = Line(l1@0, (0,0))
            l3 = PolarLine(l1@1, length=7, direction=(-1.0,-50./70), length_mode=LengthMode.DIAGONAL)
            l4 = PolarLine(l2@1, length=7, direction=(1.0,50./70), length_mode=LengthMode.DIAGONAL)
            l5 = SagittaArc(l3@1, l4@1, sagitta=-5.531)
        face = make_face()
    extrude(amount=LENGTH)
footrest = footrest_builder.part
footrest

# %%
print(footrest.volume)
export_stl(footrest, "footrest.stl")
#print(face.area)
