"""The border class defines the border of each maze square.

The name and value attributes of the resulting vorder are calculated
dynamically based on the combination of its sides. 

    >>> from maze_solver.models.border import Border
    >>> border=Border.TOP | Border.BOTTOM | Border.RIGHT | Border.LEFT
    >>> border
    <Border.TOP|BOTTOM|RIGHT|LEFT: 15>
    >>> border.value
    15
    >>> border is Border.TOP | Border.BOTTOM | Border.RIGHT | Border.LEFT
    True
    >>> border is Border.TOP | Border.RIGHT
    False
    >>> border == 15
    True
    >>> Border.TOP | Border.BOTTOM
    <Border.TOP|BOTTOM: 3>
    >>> Border.TOP in border         #membership test operator, 'in'
    True
    
"""
from enum import IntFlag, auto

class Border(IntFlag):
    """Border class defines the sides of a square. 
    
    A composite bit field is created by combining more than one enumerated constants.
    """
    
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        """Checks to see if the position is in a corner."""
        return self in (        # membership test operator, 'in'
            self.TOP | self.RIGHT,
            self.TOP | self.LEFT,
            self.BOTTOM | self.RIGHT,
            self.BOTTOM | self.LEFT
        )
    
    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3

    @property
    def deadend(self) -> bool:
        return self.bit_count() < 2