#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function that receives a list of strings containing duplicate values and 
returns a new list with all duplicates removed.
"""

test_arg = ["fuck", "hello", "help", "ESAP", "ESAP"]

def remove_duplicate_values(list_str: list) -> list:
    return list(set(list_str))

print(remove_duplicate_values(test_arg))
