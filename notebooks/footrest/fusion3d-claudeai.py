import adsk.core
import adsk.fusion
import math
import traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        rootComp = design.rootComponent
        
        # Create a new sketch on the YZ plane
        yzPlane = rootComp.yZConstructionPlane
        sketches = rootComp.sketches
        sketch = sketches.add(yzPlane)
        
        # Get sketch curves
        lines = sketch.sketchCurves.sketchLines
        arcs = sketch.sketchCurves.sketchArcs
        
        # Create the outline
        point1 = adsk.core.Point3D.create(0, 50, 0)
        point2 = adsk.core.Point3D.create(70, 50, 0)
        point3 = adsk.core.Point3D.create(0, 0, 0)
        
        # Draw main lines
        line1 = lines.addByTwoPoints(point1, point2)  # Top horizontal line
        line2 = lines.addByTwoPoints(point1, point3)  # Vertical line
        
        # Calculate points for angled lines
        vec = adsk.core.Vector3D.create(-70, -50, 0)
        vec.normalize()
        vec.scaleBy(7)
        point4 = adsk.core.Point3D.create(point2.x + vec.x, point2.y + vec.y, 0)
        
        vec2 = adsk.core.Vector3D.create(70, 50, 0)
        vec2.normalize()
        vec2.scaleBy(7)
        point5 = adsk.core.Point3D.create(point3.x + vec2.x, point3.y + vec2.y, 0)
        
        # Draw angled lines
        line3 = lines.addByTwoPoints(point2, point4)
        line4 = lines.addByTwoPoints(point3, point5)
        
        # Create arc
        arc = arcs.addByThreePoints(
            point4,  # Start point
            adsk.core.Point3D.create((point4.x + point5.x)/2, 
                                   ((point4.y + point5.y)/2) - 5.531,  # Approximate middle point
                                   0),
            point5  # End point
        )
        
        # Create profile from curves
        profile = sketch.profiles.item(0)
        
        # Create extrusion
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(profile, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)
        distance = adsk.core.ValueInput.createByReal(220)  # LENGTH parameter
        extInput.setDistanceExtent(False, distance)
        extrudes.add(extInput)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

