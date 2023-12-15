### **Roles are defined as having an IntNum (integer) value.**

Refer to maze_solver.models.role
Each square can have a role,

    NONE, ENEMY, ENTRANCE, EXIT, EXTERIOR, REWARD, WALL,

however, a role is optional.

A null (or None) value indicates the lack of a role;
but empty values force conditional branches in code, which could 
lead to errors. 

Therefore, implement a Null Object Pattern.

**Null Object Pattern** helps to avoid this issue:
* stop using 'None'
* instead use a dedicated Null Object.

### **Static duck typing**

> "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

**Static duck typing** refers to a type-checking approach in programming languages that combines elements of **static typing** and **duck typing**. 

**Static typing** - the type of a variable is known at compile time. This means that the data types of variables are explicitly declared or inferred by the compiler before the program runs.

**Duck typing** - the type or the class of an object is **determined by its behavior** (methods and properties) rather than its explicit inheritance or interfaces. 

**Static duck typing** introduces static analysis to check if the expected behavior (methods and properties) is present in the code before runtime, even though the actual types may not be explicitly declared.

### **Structural subtyping; Protocols in Python** 
A Protocol (structural subtyping, PEP 544) class, called Primitives, was defined. 

The draw() method is a **protocol member** and is defined as
having the following signature:

```
from typing import Protocol

class Primitive(Protocol):
    def draw(self, **attributes) -> str:
        ...
```

Any other classes that contain a 'draw()' method and with a 
compatible signature will be a *subtype of the Primitive class*,
due to 'structural subtyping' that occur with Protocol types. 

As an example, the Point class is a structural subtype of the 
Primitive (Point class is a type of Primitive) because the
Point class includes a draw() method with compatible signatures. 

```
class Point(NamedTuple):
    x: int
    y: int

    def draw(self, **attributes) -> str:
        return f"{self.x},{self.y}"
    
    def translate(self, x=0, y=0) -> "Point":
        return Point(self.x + x, self.y + y)
```
### **Difference between "..." and "pass" statements.**

Example usage in the maze_solver.views.primitives module. 

`pass` 'no-op'; 'no operation'; explicitly does nothing. Helps to ensure correct indentation syntax. 

`...` has a singleton value `ellipsis`, and is a placeholder. Can be used to indicated unwritten code. 

```
    % print(dir(...))
    ['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', 
    '__format__', '__ge__', '__getattribute__', '__getstate__', 
    '__gt__', '__hash__', '__init__', '__init_subclass__', 
    '__le__', '__lt__', '__ne__', '__new__', '__reduce__', 
    '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
    '__str__', '__subclasshook__']
    % print(type(...))
    <class 'ellipsis'>
    % print(....__sizeof__())
    16
```   

### **Ellipsis for Typing**

With the `typing` module, the `ellipsis` can be used to declare `tuple` types. 

Listing the elements of a `tuple` to declare a tuple type:
```
    Tuple[int, int, str]
```
Arbitrary-length homogenous tuples:
```
    Tuple[str, ...]
```