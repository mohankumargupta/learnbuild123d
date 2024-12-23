# %%

from build123d import *

# The demo is interactive!

DENSITY = 7800 / 1e6

# Parameters
LENGTH = 165
WIDTH = 85
HEIGHT = 25

BASE_HEIGHT = 12
SLOT_INNER_WIDTH = 15
LIP_OFFSET = 5
SLOT_OUTER_WIDTH = SLOT_INNER_WIDTH+2*LIP_OFFSET
LIP_HEIGHT = 3

RAMP_LENGTH = 90
RAMP_WIDTH = 65
RAMP_HEIGHT = HEIGHT - BASE_HEIGHT

# Calculated values from parameters
HALF_LENGTH = LENGTH / 2
HALF_WIDTH = WIDTH / 2
HALF_RAMP_LENGTH = RAMP_LENGTH / 2
HALF_RAMP_WIDTH = RAMP_WIDTH / 2
HALF_RAMP_HEIGHT = RAMP_HEIGHT / 2

with BuildPart() as base_part:
    # base body
    with BuildSketch() as base_sketch:
        RectangleRounded(LENGTH, WIDTH, radius=10)
    extrude(amount=-BASE_HEIGHT)
    
    # lip extrude
    with BuildSketch(mode=Mode.PRIVATE) as half_slot_sketch:
        CENTER_TO_CENTER_DISTANCE = LENGTH - 108
        
        s1 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=SLOT_OUTER_WIDTH)
        s2 = offset(amount=-LIP_OFFSET, mode=Mode.SUBTRACT)
        s3 = split(bisect_by=Plane.YZ, keep=Keep.BOTTOM)
    with BuildSketch() as lip_sketch:
        with Locations((HALF_LENGTH, 0)):
            add(half_slot_sketch)
    extrude(amount=LIP_HEIGHT)
    
    # slot hole
    with BuildSketch() as slot_hole:
        s4 = SlotCenterToCenter(center_separation=CENTER_TO_CENTER_DISTANCE, height=SLOT_INNER_WIDTH, mode=Mode.PRIVATE)
        s5 = split(s4, bisect_by=Plane.YZ, keep=Keep.BOTTOM, mode=Mode.PRIVATE)
        with Locations((HALF_LENGTH, 0)):
            add(s5)
    extrude(amount=-BASE_HEIGHT, mode=Mode.SUBTRACT)
    
    #mirror lip extrude and slot hole
    split(bisect_by=Plane.YZ, keep=Keep.TOP)
    # Add fillets around lip
    bottom_lip = base_part.faces().group_by(Axis.Z)[-3].edges().filter_by_position(Axis.Y, -20, 20)
    fillet(bottom_lip, radius=2)
    mirror(about=Plane.YZ)

with BuildPart() as ramp_part:
    with BuildSketch(Plane.XZ) as ramp_sketch:
        RAMP_RADIUS = 50
        #ARC_OFFSET = 5
        ARC_ENDPOINT = 28.61817604250837
        with BuildLine() as ramp_profile:
            ramp_l1 = Line((-HALF_RAMP_WIDTH, 0), (HALF_RAMP_WIDTH, 0))
            ramp_l2 = Line(ramp_l1@1, ramp_l1@1 + (0, RAMP_HEIGHT))
            ramp_l3 = Line(ramp_l2@1, (ARC_ENDPOINT, (ramp_l2@1).Y))
            ramp_l4 = Line(ramp_l1@0, ramp_l1@0 + (0, RAMP_HEIGHT))
            ramp_l5 = Line(ramp_l4@1, (-ARC_ENDPOINT, (ramp_l4@1).Y))
            ramp_l6 = RadiusArc(ramp_l5@1, ramp_l3@1, radius=-RAMP_RADIUS)
        make_face()        
    extrude(amount=HALF_RAMP_LENGTH, both=True)
    with Locations(Plane.XZ.shift_origin((-55/2,0,6)), Plane.XZ.shift_origin((55/2,0,6))):
        HOLE_RADIUS = 5 / 2
        Hole(radius=HOLE_RADIUS)

with BuildPart() as final_part:
    add(base_part)
    add(ramp_part)

final_part.part
print(f"\npart mass = {final_part.part.volume*DENSITY:0.2f}")   
