#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a function that receives a list of integers and returns a list that only contains 
odd numbers from the original list.
"""

def only_odd_number(list_num: list) -> list:
    list_odd = []
    for num in list_num:
        if num % 2 == 1:
            list_odd.append(num)

    return list_odd

print(only_odd_number(range(1,1000)))
