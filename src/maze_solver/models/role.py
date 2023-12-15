"""The role defines the role that each square of the maze has."""

from enum import IntEnum, auto

class Role(IntEnum):
    """ IntEnum based class to define the roles that each square can take.
    
    There is a benefit of using IntEnum rather than Enum. 
    """

    NONE = 0        #Serves as the Null Object
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()