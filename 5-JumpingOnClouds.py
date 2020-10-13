""""
This is a simulation problem. Because the problem guarantees that it is always possible to win,
we know that our input will never contain consecutive thunderclouds.
To reach the last cloud in a minimum number of steps, always try make a jump from i to i+2 .
If that is not possible, jump to i+1.



jumpingOnClouds has the following parameter(s):
    c: an array of binary integers
    - Function Description: Complete the jumpingOnClouds function in the editor below.
                            It should return the minimum number of jumps required, as an integer.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # Assuming there is always a posibility to jump
    n = len(c)
    i = 0
    jumps = 0

    while i < n - 1:
        if i + 2 >= n or c[i + 2] == 1:
            i += 1
            jumps += 1
        else:
            i += 2
            jumps += 1
    return jumps

def  jumpingOnClouds(c, n):
    jumps = [1] * n
    jumps[0] = 0
    if c[1] == 0: jumps[1] = 1
    for i in range(2, n):
        if c[i] == 0: jumps[i] = min(jumps[i - 1], jumps[i - 2]) + 1
    print(jumps[n - 1])

if __name__ == '__main__':
    # The first line contains an integer n, the total number of clouds
    n = int(input())
    # The second line contains space-separated binary integers describing clouds c[i] where 0<=i<=n
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c,n)

    print(result)
