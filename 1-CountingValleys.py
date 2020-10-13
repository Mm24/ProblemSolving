#!/bin/python3

import math
import os
import random
import re
import sys


"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly steps, 
for every step it was noted if it was an uphill, U , or a downhill, D step. 
Hikes always start and end at sea level, and each step up or down represents a 1
unit change in altitude. We define the following terms:

    - A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
    - A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through. 

countingValleys has the following parameter(s):

    int steps: the number of steps on the hike
    string path: a string describing the path
    returns int: the number of valleys traversed
"""



# Complete the 'countingValleys' function below.

# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    assert(2<=steps<=10**6)
    # assert(bool(re.compile('DU').search(path)))

    level = 0
    valleys = 0
    for s in path:
        if level == 0 and s == 'D':
            valleys += 1
        if s == 'U':
            level += 1
        elif s == 'D':
            level -= 1

    return valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
