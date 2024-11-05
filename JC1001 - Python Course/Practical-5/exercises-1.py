#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function that receives a string as a parameter and returns the text in the 
string without vowels. 
"""

import re

def without_vowels(input_str: str) -> str:
    return re.sub(r"[aeiou]", " ", input_str)

print(without_vowels("No Vowels Please!"))