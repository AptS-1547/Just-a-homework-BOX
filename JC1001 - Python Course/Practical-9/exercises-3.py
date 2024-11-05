#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a recursive function that calculates and returns the sum of a non-negative integer
 e.g. 912 = 9 + 1 + 2 = 12
"""

import sys
sys.setrecursionlimit(1000000)

def sum_recursive(number: int) -> int:
    if number == 0:
        return 0
    return number % 10 + sum_recursive(number // 10)

if __name__ == "__main__":
    print(sum_recursive(1145141919810))
