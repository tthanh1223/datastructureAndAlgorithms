#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    a = float(first_multiple_input[0])

    b = float(first_multiple_input[1])

    c = float(first_multiple_input[2])

    # Write your code here
    if a == 0:
        if b == 0:
            if c == 0:
                print("Infinitely Many Solutions")
            else:
                print("No Solution")
        else:
            x = -c / b
            print("%.2f" % x)
delta = b ** 2 - 4 * a * c
if a != 0:
    if delta < 0:
        print('No Solution')
    elif delta == 0:
        x = -b / (2 * a)
        print("%.2f" % x)
    else:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)

        if x1 == 0 and x2 == 0:
            print("0")
        if x1 == 0:
            print("0 %.2f" % x2)
        if x2 == 0:
            print("0 %.2f" % x1)
        if x1 > x2:
            print("%.2f %.2f" % (x2, x1))
        else:
            print("%.2f %.2f" % (x1, x2))
