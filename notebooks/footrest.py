# %%


from build123d import *
from math import atan2


LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as side_builder:
    with BuildSketch(Plane.YZ) as side_sketch:
        with BuildLine() as side_lines:
            l1 = Line((0,50),(70,50))
            l2 = Line(l1@0, (0,0))
            l3 = PolarLine(l1@1, length=7, direction=Vector(-70,-50).normalized())
            l4 = PolarLine(l2@1, length=7, direction=Vector(70,50).normalized())
            l5 = RadiusArc(l3@1, l4@1,radius=-120.)
        face = make_face()
    extrude(amount=-LENGTH)
side_part = side_builder.part
#side_part

# %%
assert 1==1

# %%
from build123d import *
from math import atan2

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as front_builder:
    with BuildSketch(Plane.XZ.offset(-70)) as front_sketch:
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
    extrude(amount=70)

front_part = front_builder.part

# %%
assert 1==1

# %%
from build123d import *
from math import atan2

LENGTH = 220
WIDTH = 70
HEIGHT = 50

with BuildPart() as bottom_builder:
    with BuildSketch(Plane.XZ) as side_sketch:
        Rectangle(220,70, align=(Align.MIN, Align.MIN))
        with Locations((70-220,70)):
            Triangle(a=70, b=70, C=90, rotation=-90, align=(Align.MIN, Align.MAX), mode=Mode.SUBTRACT)
    extrude(amount=50)

bottom_part = bottom_builder.part

# %%
assert 1==1


# %%

# with BuildPart() as text_builder:
#     with BuildSketch() as text_sketch:
#         with Locations((300,0)):
#             Text("X-Axis_________>", font_size=30., align=(Align.CENTER, Align.CENTER))
#         with Locations((0,300)):
#             Text("Y-Axis", font_size=30., align=(Align.CENTER, Align.CENTER))
#     extrude(amount=10)    


with BuildPart() as footrest_builder:
    add(side_builder)
    add(front_builder, mode=Mode.INTERSECT)
    #add(bottom_builder)
    #Sphere(radius=20)
    #add(text_builder)

footrest = footrest_builder.part
footrest


