import bpy
import bmesh
from math import radians, sqrt, atan2
import mathutils

# Delete default cube if it exists
if 'Cube' in bpy.data.objects:
    bpy.data.objects['Cube'].select_set(True)
    bpy.ops.object.delete()

# Create a new mesh and bmesh
mesh = bpy.data.meshes.new('footrest')
bm = bmesh.new()

# Create vertices for the profile (in YZ plane)
verts = [
    (0, 0, 0),       # v0 - bottom left
    (0, 70, 50),     # v1 - top right
    (0, 0, 50),      # v2 - top left
]

# Calculate points for angled lines
vec1 = mathutils.Vector((-70, -50)).normalized() * 7
angled_point1 = mathutils.Vector((0, 70, 50)) + mathutils.Vector((0, vec1.x, vec1.y))

vec2 = mathutils.Vector((70, 50)).normalized() * 7
angled_point2 = mathutils.Vector((0, 0, 0)) + mathutils.Vector((0, vec2.x, vec2.y))

# Add vertices for angled lines
verts.extend([
    (0, angled_point1.y, angled_point1.z),  # v3
    (0, angled_point2.y, angled_point2.z),  # v4
])

# Create vertices
bm_verts = []
for v in verts:
    bm_verts.append(bm.verts.new(v))

# Create edges
edges = [
    (bm_verts[2], bm_verts[1]),  # Top horizontal line
    (bm_verts[2], bm_verts[0]),  # Vertical line
    (bm_verts[1], bm_verts[3]),  # First angled line
    (bm_verts[0], bm_verts[4]),  # Second angled line
]

for e in edges:
    bm.edges.new(e)

# Create the arc
# Calculate arc center and radius for -120 radius arc
mid_point = (angled_point1 + angled_point2) / 2
direction = (angled_point2 - angled_point1).normalized()
perpendicular = mathutils.Vector((-direction.y, direction.x, 0))
center = mid_point + perpendicular * 120

# Create arc vertices
num_segments = 12
arc_verts = []
start_angle = atan2(angled_point1.z - center.z, angled_point1.y - center.y)
end_angle = atan2(angled_point2.z - center.z, angled_point2.y - center.y)

if end_angle < start_angle:
    end_angle += 2 * 3.14159

prev_vert = bm_verts[3]
for i in range(1, num_segments):
    t = i / num_segments
    angle = start_angle * (1 - t) + end_angle * t
    x = 0
    y = center.y + 120 * cos(angle)
    z = center.z + 120 * sin(angle)
    new_vert = bm.verts.new((x, y, z))
    bm.edges.new((prev_vert, new_vert))
    prev_vert = new_vert
    arc_verts.append(new_vert)

# Connect last arc vertex to endpoint
bm.edges.new((prev_vert, bm_verts[4]))

# Create face
bmesh.ops.triangle_fill(bm, edges=bm.edges[:], use_beauty=True)

# Extrude the profile
geom = bm.faces[:]
bmesh.ops.extrude_face_region(bm, geom=geom)
bmesh.ops.translate(bm,
                   vec=(220, 0, 0),
                   verts=[v for v in bm.verts if v.select])

# Update mesh
bm.to_mesh(mesh)
bm.free()

# Create object and link to scene
obj = bpy.data.objects.new('Footrest', mesh)
bpy.context.collection.objects.link(obj)

# Select the new object
bpy.context.view_layer.objects.active = obj
obj.select_set(True)

# Add smooth shading
bpy.ops.object.shade_smooth()

# Add edge split modifier to maintain sharp edges
edge_split = obj.modifiers.new(name="Edge Split", type='EDGE_SPLIT')
edge_split.split_angle = radians(30)

"""
Here's a concise step-by-step guide using only keyboard shortcuts to create the footrest in Blender:

New scene setup:


X to delete default cube
Numpad 1 for front view
Numpad 5 to toggle orthographic view


Create base shape:


Shift + A, M for mesh, P for plane
Tab to enter edit mode
A to select all vertices
X to delete only vertices


Create profile:


Ctrl + Left Click to place vertices for:

Bottom point (0,0)
Top left point (straight up)
Top right point


E to extrude top right vertex at angle
E to extrude bottom vertex at angle


Create arc:


Select two end vertices
Shift + Right Click between them
F3, type "arc" and select "Make Arc"
Adjust radius to -120 in operator panel (F9)


Create face:


A to select all
F to create face


Extrude:


Numpad 3 for side view
E, X to extrude along X axis
Type "220" for exact length


View navigation during work:


Middle Mouse Button to orbit
Shift + Middle Mouse to pan
Mouse Wheel to zoom
Numpad . to focus on selection


Final touches:


Tab to exit edit mode
Shift + N to recalculate normals
Right Click, shade smooth
Add Edge Split modifier if needed (Ctrl + 3, search for "Edge Split")
"""