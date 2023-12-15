### Roles are defined as having an IntNum (integer) value. 

Refer to maze_solver.models.role
Each square can have a role 
    NONE, ENEMY, ENTRANCE, EXIT, EXTERIOR, REWARD, WALL
    however, a role is optional.
A null (or None) value indicates the lack of a role;
but empty values force conditional branches in code, which could 
lead to errors. Therefore, implement a Null Object Pattern.
**Null Object Pattern** helps to avoid this issue:
* stop using 'None'
* instead use a dedicated Null Object.

### Static duck typing

> "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

**Static duck typing** refers to a type-checking approach in programming languages that combines elements of **static typing** and **duck typing**. 

**Static typing** - the type of a variable is known at compile time. This means that the data types of variables are explicitly declared or inferred by the compiler before the program runs.

**Duck typing** - the type or the class of an object is **determined by its behavior** (methods and properties) rather than its explicit inheritance or interfaces. 

**Static duck typing** introduces static analysis to check if the expected behavior (methods and properties) is present in the code before runtime, even though the actual types may not be explicitly declared.