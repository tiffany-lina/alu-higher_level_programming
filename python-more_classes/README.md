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
### 2-rectangle.py
Defines a class `Rectangle` with private attributes `width` and `height`.
- Properties `width` and `height` include getters and setters with validation.
- Public methods:
  - `area()` → returns the rectangle area.
  - `perimeter()` → returns the rectangle perimeter (0 if width or height is 0).

Usage example:

```python
from 2-rectangle import Rectangle
r = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(r.area(), r.perimeter()))
r.width = 10
r.height = 3
print("Area: {} - Perimeter: {}".format(r.area(), r.perimeter()))
### 3-rectangle.py
Defines a Rectangle class with width, height, area, perimeter, and printing via str() and repr().
