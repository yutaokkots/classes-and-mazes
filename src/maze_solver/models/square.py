"""Defines the Square class. """
from dataclasses import dataclass

from maze_solver.models.border import Border
from maze_solver.models.role import Role

@dataclass(frozen=True)
class Square:
    "Square class representing each square on the maze includes various properties."
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE