"""
    The factorial of the integer n, written n!, is defined as:
    
        n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1

    Calculate and print the factorial of a given integer.
    
    Complete the extraLongFactorials function in the editor below. It should print the result and return.

    extraLongFactorials has the following parameter(s):

    n: an integer

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.

# Memoization here isn't strictly necessary, but I wanted to practice writing out a memoization feature.


def memo(f):
    table = {}

    def helper(x):
        if x not in table:
            table[x] = f(x)
        return table[x]
    return helper


@memo
def extraLongFactorials(n):
    product = 1
    for i in range(1, n+1):
        product *= i

    print(product)


if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
