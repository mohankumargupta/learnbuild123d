from typing import Any, Dict, List
from IPython.display import HTML

from json import dumps
import os
from string import Template
from typing import Any, Dict, List
from IPython.display import HTML
from vtkmodules.vtkIOXML import vtkXMLPolyDataWriter

DEFAULT_COLOR = [1, 0.8, 0, 1]

def to_vtkpoly_string(
    shape: Any, tolerance: float = 1e-3, angular_tolerance: float = 0.1
) -> str:
    """to_vtkpoly_string

    Args:
        shape (Shape): object to convert
        tolerance (float, optional): Defaults to 1e-3.
        angular_tolerance (float, optional): Defaults to 0.1.

    Raises:
        ValueError: not a valid Shape

    Returns:
        str: vtkpoly str
    """
    if not hasattr(shape, "wrapped"):
        raise ValueError(f"Type {type(shape)} is not supported")

    writer = vtkXMLPolyDataWriter()
    writer.SetWriteToOutputString(True)
    writer.SetInputData(shape.to_vtk_poly_data(tolerance, angular_tolerance, True))
    writer.Write()

    return writer.GetOutputString()


def shape_to_html(shape: Any) -> HTML:
    """shape_to_html

    Args:
        shape (Shape): object to display

    Raises:
        ValueError: not a valid Shape

    Returns:
        HTML: html code
    """
    payload: List[Dict[str, Any]] = []

    if not hasattr(shape, "wrapped"):  # Is a "Shape"
        raise ValueError(f"Type {type(shape)} is not supported")

    payload.append(
        {
            "shape": to_vtkpoly_string(shape),
            "color": DEFAULT_COLOR,
            "position": [0, 0, 0],
            "orientation": [0, 0, 0],
        }
    )

    # A new div with a unique id, plus the JS code templated with the id
    div_id = "shape-" + str(id(shape))
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path, "template_render.js"), encoding="utf-8") as f:
        TEMPLATE_JS = f.read()
    code = Template(TEMPLATE_JS).substitute(data=dumps(payload), div_id=div_id, ratio=0.5)
    html = HTML(f"<div id={div_id}></div><script>{code}</script>")

    return html