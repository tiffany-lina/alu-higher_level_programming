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
### 7-rectangle.py
Implements the Rectangle class with width, height, area, perimeter,
instance tracking, customizable print symbols, and full documentation.
### 8-rectangle.py
Adds a static method `bigger_or_equal` to compare two Rectangle objects
based on their area and return the bigger one.
### 9-rectangle.py
Extends the Rectangle class with a `square` class method
that returns a new Rectangle instance with width == height == size.
Demonstrates area, perimeter, and string representation of a square.
### 6-rectangle.py
Defines a Rectangle class with private width and height,
tracks number of instances, and supports area, perimeter,
string representation, and deletion message.

