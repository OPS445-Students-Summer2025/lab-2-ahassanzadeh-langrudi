#!/usr/bin/env python3

# Author: Arshan Hassanzadeh-Langrudi
# Author ID: ahassanzadeh-langrud
# Date Created: 2025/05/21
import sys

# Check if an argument was provided
if len(sys.argv) == 2:
    timer = int(sys.argv[1])
else:
    timer = 3

while timer > 0:
    print(timer)
    timer -= 1

print("blast off!")
