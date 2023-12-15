""" Defines the Maze class"""

from dataclasses import dataclass
from typing import Iterator
from functools import cached_property
from maze_solver.models.square import Square
from maze_solver.models.maze import Maze
from maze_solver.models.role import Role

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


    def __post_init__(self) -> None:
        validate_indices(self)
        validate_row_columns(self)
        validate_entrance(self)
        validate_exit(self)

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

    @cached_property
    def entrance(self) -> Square:
        return next(sq for sq in self if sq.role is Role.ENTRANCE)
    @cached_property
    def exit(self) -> Square:
        return next(sq for sq in self if sq.role is Role.EXIT)


def validate_indices(self, maze:Maze) -> None:
    """Validates each square in the maze.
    
    Checkes for the index property of each Square fits into 
    a continuous sequence of numbers that enumrates 
    all of the squares in the maze.
    """
    assert [square.index for square in maze] == list(range(len(maze.squares))), "Incorrect square.index."

def validate_row_columns(self, maze:Maze) -> None:
    """ Validates the row and column of the maze.

    Iterates over the rows and columns in the Maze,
    ensuring that the row and column attributes of the corresponding Square
    match up with the current row and column of the loops.
    """
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            assert square.row == y, "Incorrect square.row."
            assert square.column == x, "Incorrect square.column."

def validate_entrance(maze: Maze) -> None:
    assert 1 == sum(
        1 for square in maze if square.role is Role.ENTRANCE
    ), "Must include exactly one entrance."

def validate_exit(maze: Maze) -> None:
    assert 1 == sum(
        1 for square in maze if square.role is Role.EXIT
    ), "Must include exactly one exit."