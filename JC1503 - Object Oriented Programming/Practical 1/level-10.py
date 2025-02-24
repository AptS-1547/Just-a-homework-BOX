#!/usr/bin/env python3

"""
Write a Python program that takes no input and produces a copy of its own source code as its only 
output (this is like a computer virus that can replicate itself). 
"""

from pathlib import Path

with open(Path(__file__), "r") as file:
    print(file.read())
