"""The Decomposer translates a Border instance into a geometric primitive."""
from maze_solver.models.border import Border
from maze_solver.views.primitives import (
    Line,
    Point,
    Polygon,
    Polyline,
    DisjointLines,
    NullPrimitive,
    Primitive,
)

def decompose(border: Border, top_left: Point, square_size: int) -> Primitive:
    """ Turns a border into a relevant geometric primitive. 

    Uses the coordinates of the top_left point (a Point Type), and square_size:
        top_left -> •-------• top_right
                    │       │
                    │       │
        bottom_left •-------• bottom_right
    to generate the other points, using the translate method. 
    """
    top_right: Point = top_left.translate(x=square_size)
    bottom_right: Point = top_left.translate(x=square_size, y=square_size)
    bottom_left: Point = top_left.translate(y=square_size)

    top = Line(top_left, top_right)
    bottom = Line(bottom_left, bottom_right)
    left = Line(top_left, bottom_left)
    right = Line(top_right,bottom_right)

    # Polygon for a complete box; note the ordering of the points when instantiating.
    # □
    if border is Border.LEFT | Border.TOP | Border.RIGHT | Border.BOTTOM:
        return Polygon(
            [top_left,
             top_right,
             bottom_right,
             bottom_left]
        )
    
    # Polylines for a three-sided shape; note the ordering of the points when instantiating.
    # ⊏
    if border is Border.BOTTOM | Border.LEFT | Border.TOP:
        return Polyline(
            [
                bottom_right,
                bottom_left,
                top_left,
                top_right,
            ]
        )
    
    # ⊓
    if border is Border.LEFT | Border.TOP | Border.RIGHT:
        return Polyline(
            [
                bottom_left,
                top_left,
                top_right,
                bottom_right,
            ]
        )
    
    # ⊐
    if border is Border.TOP | Border.RIGHT | Border.BOTTOM:
        return Polyline(
            [
                top_left,
                top_right,
                bottom_right,
                bottom_left,
            ]
        )
    
    # ⊔
    if border is Border.RIGHT | Border.BOTTOM | Border.LEFT:
        return Polyline(
            [
                top_right,
                bottom_right,
                bottom_left,
                top_left,
            ]
        )
    
    # Polylines for a two-sided shape; note the ordering of the points when instantiating.
    if border is Border.LEFT | Border.TOP:
        return Polyline(
            [
                bottom_left,
                top_left,
                top_right,
            ]
        )
    
    if border is Border.TOP | Border.RIGHT:
        return Polyline(
            [
                top_left,
                top_right,
                bottom_right,
            ]
        )
    
    if border is Border.BOTTOM | Border.LEFT:
        return Polyline(
            [
                bottom_right,
                bottom_left,
                top_left,
            ]
        )
    
    if border is Border.RIGHT | Border.BOTTOM:
        return Polyline(
            [
                top_right,
                bottom_right,
                bottom_left,
            ]
        )
    
    # Polylines for a two-sided shape, where the lines are parallel (NS or WE).
    if border is Border.LEFT | Border.RIGHT:
        return DisjointLines([left, right])
    
    if border is Border.TOP | Border.BOTTOM:
        return DisjointLines([top, bottom])
    
    #Lines for a one-sided box. 
    if border is Border.LEFT:
        return left
    
    if border is Border.RIGHT:
        return right
    
    if border is Border.TOP:
        return top
    
    if border is Border.BOTTOM:
        return bottom
    
    return NullPrimitive()