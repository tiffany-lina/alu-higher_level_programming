#!/usr/bin/python3

def uppercase(str):
    """Print a string in uppercase using only one loop and no imports."""
    for c in str:
        print("{}".format(chr(ord(c) - 32)) if 'a' <= c <= 'z' else "{}".format(c),
              end='')
    print()

