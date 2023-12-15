""" Defines the Maze class"""

from dataclasses import dataclass
from typing import Iterator
from functools import cached_property
from maze_solver.models.square import Square

@dataclass(frozen=True) # immutable dataclass to ensure underlying tuple of square objects are unchanged.
class Maze:
    """Maze class defines the Maze. 

    There might be an inclination to use a list to store the Square object.
    But that would prevent caching partial results of computations later.
    Python's cache requires memoized function arguments to be hashable and
    therefore, immutable. 
    To avoid 
    (1) extra work when iterating over squares; and
    (2) accessing a Square by index, 
    two specialized methods allow for the Squares to be iterable and subscriptable: 
       __iter__()
       __getitem__()
    """
    squares: tuple[Square, ...]

    def __iter__(self) -> Iterator[Square]:
        """Allows maze instances to cooperate with a for-loop."""
        return iter(self.squares)
    
    def __getitem__(self, index:int) -> Square:
        """Enables square-bracket notation for getting squares by index."""
        return self.squares[index]
    
    @cached_property
    def width(self):
        """Obtains the width of the maze.
        
        Because looping through the square is an expensive operation, 
        use the functools' cached_property to cache the information.
        Computed only once
        """
        return max(square.column for square in self) + 1
    
    @cached_property
    def height(self):
        """Obtains the width of the maze.
        
        Both the width and height is calculated (rather than supplied).
        This allows for data consistency, where supplied values may not be correct.
        """
        return max(square.row for square in self) + 1
    
