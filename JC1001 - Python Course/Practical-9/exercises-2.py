#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Fibbonacci numbers also referred to as 𝐹_𝑛 is a sequence such that each 
number is the sum of the two proceeding numbers when either number is 
greater than 1:
 𝐹𝑛 = 𝐹𝑛−1 +𝐹𝑛−2 
Write a recursive function that calculates and returns a Fibbonaci number for a given 
positive integer. 
"""

import sys
sys.setrecursionlimit(1000000)

def fibbonacci_recursive(number: int, memo={}) -> int:
    if number in memo:
        return memo[number]
    if number in (1, 2):
        return 1
    memo[number] = fibbonacci_recursive(number - 1, memo) + fibbonacci_recursive(number - 2, memo)
    return memo[number]

if __name__ == "__main__":
    print(fibbonacci_recursive(114))
