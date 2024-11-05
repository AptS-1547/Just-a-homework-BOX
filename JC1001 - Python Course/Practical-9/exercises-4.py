#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a recursive function that calculates and returns the value of 𝑎𝑏 – that is, your 
function receives two integer arguments / parameters, a and b.
"""

import sys
sys.setrecursionlimit(1000000)

def power_recursive(a: int, b: int) -> int:
    if b == 0:
        return 1
    return a * power_recursive(a,b-1)

if __name__ == "__main__":
    print(power_recursive(400, 4))
