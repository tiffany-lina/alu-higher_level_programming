# Python - Data Structures: Lists, Tuples

## Task 0: Print a list of integers
**File:** `0-print_list_integer.py`

### Description
A function that prints all integers of a list, one per line, using `str.format()`.

### Example
```bash
$ ./0-main.py
1
2
3
4
5
## Task 1: Secure access to an element in a list
**File:** `1-element_at.py`

### Description
This function retrieves an element from a list like in C.  
- Returns `None` if the index is negative or out of range.

### Example
```bash
$ ./1-main.py
Element at index 3 is 4
## Task 2: Replace element
**File:** `2-replace_in_list.py`

### Description
This function replaces an element of a list at a specific position (like in C).  
- If the index is negative or out of range, it returns the original list.

### Example
```bash
$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
## Task 3: Print list in reverse
**File:** `3-print_reversed_list_integer.py`

### Description
This function prints all integers of a list in reverse order, one per line, using `str.format()`.

### Example
```bash
$ ./3-main.py
5
4
3
2
1
## Task 4: Replace element without modifying original list
**File:** `4-new_in_list.py`

### Description
This function replaces an element in a copy of a list at a specific position.  
- Returns a new list with the modification.
- Original list remains unchanged.
- If index is negative or out of range, returns a copy of the original list.

### Example
```bash
$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
## Task 5: Remove all 'c' and 'C' from a string
**File:** `5-no_c.py`

### Description
This function removes all occurrences of `c` and `C` from a string and returns the new string.

### Example
```bash
$ ./5-main.py
Best Shool
hiago
 is fun!
## Task 6: Print a matrix of integers
**File:** `6-print_matrix_integer.py`

### Description
This function prints a matrix of integers.  
- Each row is printed on a new line.  
- Integers are separated by a space using `str.format()`.  
- Works with empty matrices as well.

### Example
```bash
$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
## Task 7: Add 2 tuples
**File:** `7-add_tuple.py`

### Description
This function adds 2 tuples element-wise.  
- Returns a new tuple of 2 integers.  
- If a tuple has less than 2 elements, missing values are treated as 0.  
- If a tuple has more than 2 elements, only the first 2 are used.

### Example
```bash
$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
## Task 8: Tuple with string length and first character
**File:** `8-multiple_returns.py`

### Description
This function returns a tuple containing:  
1. The length of a string  
2. The first character of the string  

- If the string is empty, the first character is `None`.

### Example
```bash
$ ./8-main.py
Length: 22 - First character: A
## Task 9: Find the biggest integer in a list
**File:** `9-max_integer.py`

### Description
This function finds and returns the biggest integer in a list.  
- Returns `None` if the list is empty.  
- Does not use the built-in `max()`.

### Example
```bash
$ ./9-main.py
Max: 90
## Task 10: Find multiples of 2 in a list
**File:** `10-divisible_by_2.py`

### Description
This function returns a new list of booleans indicating whether each integer in the original list is divisible by 2.  
- The returned list has the same size as the original list.

### Example
```bash
$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2

