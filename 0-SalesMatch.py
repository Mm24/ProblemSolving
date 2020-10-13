"""
Function Description

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):
    n: the number of socks in the pile
    ar: the colors of each sock

input format:
- The first line contains an integer n, the number of socks represented in ar
- The second line contains n space-separated integers describing the colors ar[i] of the socks in the pile

"""

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # Checks the number of pairs is 1<=n<=100
    assert(n > 0 and n <= 100  )
    # Checks the pairs are 1<=ar<=100
    assert( all(ele >= 1 and ele <=100  for ele in ar) )

    count = lambda element, seq: sum(1 for i in seq if i == element)
    pairs = 0
    socks = ar
    for s in set(socks):
        pairs += count( s, socks ) // 2
    return pairs


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Number of pairs
    n = int(9)  #int(input())
    # Socks
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]   #list(map(int, input().rstrip().split()))


    result = sockMerchant(n, ar)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()