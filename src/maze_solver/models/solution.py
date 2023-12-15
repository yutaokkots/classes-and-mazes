"""Solution for a maze, originating and an entrance and ending at an exit.

A dataclass contains the following methods:
['__annotations__', '__class__', '__dataclass_fields__', '__dataclass_params__', 
'__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__match_args__', '__module__', '__ne__', 
'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
'__str__', '__subclasshook__', '__weakref__']

"""

from dataclasses import dataclass
from typing import Iterator
from functools import reduce

from maze_solver.models.role import Role
from maze_solver.models.square import Square


@dataclass(frozen=True)
class Solution:
    """ Solution class for obtaining a maze's solution. 
    
    two specialized methods allow for the squares to be iterable and subscriptable: 
        .__iter__()
        .__getitem__()
    a method for obtaining the length is also defined:
        .__len__()

    squares : tuple[Square, ...]
        Defines a tuple that comprises Type Square as defined by maze_solver.models.square. 
    """
    squares: tuple[Square, ...]

    def __post_init__(self) -> None:
        assert self.squares[0].role is Role.ENTRANCE
        assert self.squares[-1].role is Role.EXIT
        reduce(validate_corridor, self.squares)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)
    
    def __getitem__(self, index: int) -> Square:
        return self.squares[index]
    
    def __len__(self) -> int:
        return len(self.squares)

def validate_corridor(current:Square, following:Square) -> Square:
    """Validation for the maze path.
    
    The maze must have its
    - first square (self.squares[0] be the maze entrance (role.ENTRANCE)
    - last square (self.squares[-1] be the maze exit (role.EXIT)
    - two consecutive squares (current and following) share 
        a same row or same column (assert any()).
    """
    assert any([
        current.row == following.row,
        current.column == following.column
    ]), "Squares must lie in the same row or column."
    return following