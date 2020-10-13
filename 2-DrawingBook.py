#!/bin/python3

import os
import sys

"""
Function Description: 
Given and n ,p find and print the minimum number of pages that must be turned in order to arrive at page p


pageCount has the following parameter(s):

    int n: the number of pages in the book
    int p: the page number to turn to

Returns

    int: the minimum number of pages to turn to page p

"""


def pageCount(n, p):
    # assert (n > 0 and n <= 10**5)
    # assert (p > 0 and p <= n)
    page =  min(p//2, n//2-(p//2))
    return page

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
