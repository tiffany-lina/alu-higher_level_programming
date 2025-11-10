# Python More Classes

This directory contains exercises for practicing Python classes.

## Files

### 0-rectangle.py
Defines an empty class `Rectangle` that can be instantiated:
```python
from 0-rectangle import Rectangle
my_rectangle = Rectangle()
### 1-rectangle.py
Defines a class `Rectangle` with private attributes `width` and `height`.
- Width and height must be integers >= 0.
- Properties `width` and `height` include getters and setters.

Usage example:

```python
from 1-rectangle import Rectangle
r = Rectangle(2, 4)
r.width = 10
r.height = 3
