"""Defines the geometric primitive generic function to create an XML tag. 

The XML tag helps to generate an SVG element.
For example,
    rect_svg = tag("rect", x=10, y=10, width=50, height=50, fill="red")

>>> # Element name and attributes (including one with a hyphen)
>>> tag("svg", xmlns="http://www.w3.org/2000/svg", stroke_linejoin="round")
'<svg xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" />'
"""

from typing import Protocol, NamedTuple

class Primitive(Protocol):
    """ Primitive Class uses Protocol from the typing module. 
    
    Protocol defines an expected behavior: 
        any class that claims to implement the Primitive protocol 
        must have a draw method that takes keyword arguments (**attributes) 
        and returns a string.

    Protocol defines an interface without specifying the actual implementation 
        of the draw method. Instead, it includes the ellipsis (...) 
        in the method body, which is a way to indicate that the method 
        should be present but doesn't provide any implementation details.
    """
    def draw(self, **attributes) -> str:
        ...

class Point(NamedTuple):
    """Point class generates a point with (x,y) coordinates.
    
    Point class uses the 'NamedTuple' factory function (sublcass of a NamedTuple). 
    
    By using NamedTuple, it extends the 'tuple' class with named fields. 
    The name fields in this class are:

    x : int
        Represents the x-coordinate of a Euclidean point.
    y : int
        Represents the y-coordinate of a Euclidean point.

    The Point class contains a .draw() method. The Primitive Protocol also
    contains a .draw() method, but this Point class is not extended from the 
    Primitive Protocol. 
    """

    x: int
    y: int

    def draw(self, **attributes) -> str:
        return f"{self.x},{self.y}"
    
    def translate(self, x=0, y=0) -> "Point":
        return Point(self.x + x, self.y + y)
    
class Line(NamedTuple):
    """Line class generates a line segment delimited by the starting and ending points.
    
    Line class uses a 'NamedTuple' factory function. 
    The name fields in the class are:
    start : Point
        starting point of the line segment.
    end : Point
        ending point of the line segment.

    """
    start: Point
    end: Point

    def draw(self, **attributes) -> str:
        """Draw method returns an svg line. """
        return tag(
            "line",
            x1 = self.start.x,
            y1=self.start.y,
            x2=self.end.x,
            y2=self.end.y,
            **attributes,
        )

def tag(name:str, value:str | None = None, **attributes) -> str:
    """A 'tag' function that defines the creation of an XML tag.
    
    If the attributes contain any elements, it also replaces 
    any underscores to hyphens in the attribute name. 
    (stroke_width -> "stroke-width")

    name : str
        the name of the XML tag (e.g. "svg", "div", "circle", "rect")
    value : str | None 
        the content of the tag.
    **attributes
        kwargs for additional tag attributes. 
    """

    attrs = "" if not attributes else " " + " ".join(
        f'{key.replace("_", "-")}="{value}"'
        for key, value in attributes.items()
    )
    if value is None:
        return f"<{name}{attrs} />"
    return f"<{name}{attrs}>{value}</{name}>"

