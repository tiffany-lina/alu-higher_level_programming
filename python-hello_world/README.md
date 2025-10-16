# 0-run Script

This script runs a Python file whose name is stored in the $PYFILE environment variable.
It automatically appends ".py" to the filename.
# 1-run_inline.py Script

This script runs Python code stored in the environment variable $PYCODE.
Example usage:
export PYCODE='print(f"Best School: {88+10}")'
./1-run_inline.py
# Output: Best School: 98
