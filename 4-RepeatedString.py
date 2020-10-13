#!/bin/python3

import math
import os
import random
import re
import sys

"""

Lilah has a string, s, of lowercase English letters that she repeated infinitely many times.

Given an integer, n, find and print the number of letter a's in the first letters of Lilah's infinite string.

For example, if the string  s = 'abcab' and n=10, the substring we consider is 'abcababcab', the first characters of her infinite string. There are 4
occurrences of a in the substring.

repeatedString has the following parameter(s):

    s: a string to repeat
    n: the number of characters to consider (an integer)
    Function Description: It should return an integer representing the number of occurrences of a in the prefix of length
    in the infinitely repeating string.

"""

# Complete the repeatedString function below.
def repeatedString(s, n):
    # Constraints
    assert(len(s)<100)
    assert(n>=1 and n<=10**12 )

    c = 'a'
    if n <= len(s):
        rep = s[:n].count(c)
    else:
        rep = s.count(c) * (n // len(s)) + s[:(n % len(s))].count(c)
    print(rep)
    return rep

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
