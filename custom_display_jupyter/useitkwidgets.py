import vtk
from itkwidgets import view

sphere = vtk.vtkSphereSource()
sphere.SetRadius(1)
sphere.Update()

viewer = view(
    geometries=sphere.GetOutput(),
    ui_collapsed=True,
    axes=False,
    background=(255,255,255),
)