""" Defines specific SVG primitives. 

Functions
---------
tag : function
    Defines a geometric primitive generic function to create XML tags. 
Classes
-------
Primitive : class


The XML tag helps to generate an SVG element.
For example,
    rect_svg = tag("rect", x=10, y=10, width=50, height=50, fill="red")

>>> # Element name and attributes (including one with a hyphen)
>>> tag("svg", xmlns="http://www.w3.org/2000/svg", stroke_linejoin="round")
'<svg xmlns="http://www.w3.org/2000/svg" stroke-linejoin="round" />'
"""

from dataclasses import dataclass
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

    Allows for static duck typing of class instances that contain
    and use a 'draw()' method as a Primitive class. 
    """
    def draw(self, **attributes) -> str:
        ...

class Point(NamedTuple):
    """Point class generates a point with (x,y) coordinates.
    
    Point class uses the 'NamedTuple' factory function (sublcass of a NamedTuple). 
    By using NamedTuple, it extends the 'tuple' class with named field attributes. 
    
    Attributes
    ----------
    x : int
        Represents the x-coordinate of a Euclidean point.
    y : int
        Represents the y-coordinate of a Euclidean point.

    Methods
    -------
    draw(**attributes):
        Returns a point as an (x, y) coordinate.
        The Point class contains a .draw() method. The Primitive Protocol also
        contains a .draw() method, but this Point class is not extended from the 
        Primitive Protocol. 
    translate(x=0, y=0):
        returns a translated (shifted) point using input x and y values. 
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

class Polyline(tuple[Point,...]):
    """Polyline class to create a polyline (multiple lines but unconnected at first and last point)."""
    
    def draw(self, **attributes) -> str:
        """This draw method returns an xml for a <polyline> element.
        
        When instantiated, it uses the tuple of Point objects (between the parenthesis)
        to self-create and become the type, tuple of Points (i.e. Polyline Type). 
        Therefore, 'self' is the tuple of Points itself.
        """
        points = " ".join(point.draw() for point in self)
        return tag("polyline", points=points, **attributes)
    
class Polygon(tuple[Point,...]):
    """Polygon class to create a polygon (closed multi-line shape)."""

    def draw(self, **attributes) -> str:
        """The draw method returns an xml for a <polygon> element."""
        points = " ".join(point.draw() for point in self)
        return tag("polygon", points=points, **attributes)

class DisjointLines(tuple[Line,...]):
    """Disjoint class to combine existing lines. """

    def draw(self, **attributes) -> str:
        """'Draws' a connection between lines (no SVG equivalent)."""
        return "".join(line.draw(**attributes) for line in self)

@dataclass(frozen=True)
class Rect:
    """Rectangle class for generating a rectangle xml element.
    
    Because this is a dataclass with (frozen=True), instances 
    of the class are immutable. 

    Attributes
    ----------
    top_left : Point
        Optional coordinates as a Point object can be provided. If provided, 
        the point coordinates are combined with the other attributes in the 
        draw method in the line of code: 
            attrs = attributes | {"x": self.top_left.x, "y": self.top_left.y}
    """
    top_left: Point | None = None

    def draw(self, **attributes) -> str:
        """The draw method returns an xml for a <rect> element."""
        if self.top_left:
            attrs = attributes | {"x": self.top_left.x, "y": self.top_left.y}
        else:
            attrs = attributes
        return tag("rect", **attrs)
    
@dataclass(frozen=True)
class Text:
    """Rectangle class for generating a Text xml element."""
    content: str
    point: Point

    def draw(self, **attributes) -> str:
        """The draw method returns an xml for a <text> element."""
        return tag(
            "text",
            self.content,
            x=self.point.x,
            y=self.point.y,
            **attributes
        )

class NullPrimitive:
    """Defines a Null Primitive object to adhere to a null object pattern."""

    def draw(self, **attributes) -> str:
        return ""

def tag(name:str, value:str | None = None, **attributes) -> str:
    """Defines the creation of an XML tag.
    
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

