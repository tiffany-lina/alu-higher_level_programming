#!/usr/bin/python3
import marshal
import types
import sys
import dis

if __name__ == "__main__":
    with open("hidden_4.pyc", "rb") as f:
        f.read(16)  # skip header (Python 3.8+)
        code = marshal.load(f)
    names = [name for name in code.co_names if not name.startswith("__")]
    for name in sorted(names):
        print(name)
