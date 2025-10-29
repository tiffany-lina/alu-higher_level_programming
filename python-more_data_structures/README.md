## Task 0: Square all integers in a matrix
**File:** `0-square_matrix_simple.py`

### Description
This function computes the square of all integers in a 2D matrix.  
- Returns a new matrix.  
- Original matrix remains unchanged.

### Example
```bash
$ ./0-main.py
[[1, 4, 9], [16, 25, 36], [49, 64, 81]]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
## Task 1: Replace element in a list
**File:** `1-search_replace.py`

### Description
This function returns a new list where all occurrences of a given element are replaced with another element.  
- Original list remains unchanged.

### Example
```bash
$ ./1-main.py
[1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
[1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
## Task 2: Add all unique integers in a list
**File:** `2-uniq_add.py`

### Description
This function returns the sum of all unique integers in a list.  
- Each integer is counted only once.

### Example
```bash
$ ./2-main.py
Result: 15
## Task 3: Return common elements in two sets
**File:** `3-common_elements.py`

### Description
This function returns a set of elements common to two input sets.

### Example
```bash
$ ./3-main.py
['C']
## Task 4: Return elements present in only one set
**File:** `4-only_diff_elements.py`

### Description
This function returns a set of elements that are present in exactly one of the two input sets.

### Example
```bash
$ ./4-main.py
['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
## Task 5: Return number of keys in a dictionary
**File:** `5-number_keys.py`

### Description
This function returns the number of keys in a given dictionary.

### Example
```bash
$ ./5-main.py
Number of keys: 3
## Task 6: Print a dictionary by ordered keys
**File:** `6-print_sorted_dictionary.py`

### Description
This function prints all keys and values of a dictionary in alphabetical order of the keys.  
- Only the first level keys are sorted.  
- Values can be of any type.

### Example
```bash
$ ./6-main.py
Number: 89
ids: [1, 2, 3]
language: C
track: Low level
## Task 8: Delete a key in a dictionary
**File:** `8-simple_delete.py`

### Description
This function deletes a key from a dictionary if it exists.  
- If the key does not exist, the dictionary remains unchanged.

### Example
```bash
$ ./8-main.py
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
--
--
Number: 89
ids: [1, 2, 3]
language: C
--
Number: 89
ids: [1, 2, 3]
language: C
## Task 9: Return a new dictionary with all values multiplied by 2
**File:** `9-multiply_by_2.py`

### Description
This function returns a new dictionary with all values of the input dictionary multiplied by 2.  
- Original dictionary remains unchanged.

### Example
```bash
$ ./9-main.py
Alex: 8
Bob: 14
John: 12
Mike: 14
Molly: 16
--
Alex: 16
Bob: 28
John: 24
Mike: 28
Molly: 32
## Task 10: Return key with the biggest integer value
**File:** `10-best_score.py`

### Description
This function returns the key associated with the highest integer value in a dictionary.  
- If the dictionary is empty or `None`, it returns `None`.  
- Assumes all values are integers and unique.

### Example
```bash
$ ./10-main.py
Best score: Molly
Best score: None

