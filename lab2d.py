#!/usr/bin/env python3

import sys

# Check for exactly 2 additional arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')