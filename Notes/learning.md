### Roles are defined as having an IntNum (integer) value. 

The role is optional. 
A null (or None) value could indicate the lack of a role;
but empty values force conditional branches in code, which could 
lead to errors. 
**Null Object Pattern** helps to avoid this issue:
* stop using 'None'
* instead use a dedicated Null Object.
