# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# For example, assume the bill has the following prices: bill = [2, 4, 6]. Anna declines to eat item bill[2] which costs 6. If Brian calculates the bill correctly, Anna will pay (2 + 4) / 2 = 3. If he includes the cost of bill[2], he will calculate (2 + 4 + 6) / 2 = 6. In the second case, he should refund 3 to Anna.
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    anna_copy = [value for index, value in enumerate(bill) if index != k]
    total_paid = sum(bill) / 2
    anna_paid = sum(anna_copy) / 2

    message = "Bon Appetit" if (anna_paid == b) else (
        int(total_paid - anna_paid))
    print(message)


if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
