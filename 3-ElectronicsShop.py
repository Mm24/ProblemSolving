"""
getMoneySpent has the following parameter(s):

    int keyboards[n]: the keyboard prices
    int drives[m]: the drive prices
    int b: the budget

Returns

    int: the maximum that can be spent, or

if it is not possible to buy both items
"""
#!/bin/python3

import os
import sys


def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    money = [sum([x, y]) for x in keyboards for y in drives if sum([x, y]) <= b]
    # -1 if she can't purchase both items
    money = max(money + [-1])
    return money


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()