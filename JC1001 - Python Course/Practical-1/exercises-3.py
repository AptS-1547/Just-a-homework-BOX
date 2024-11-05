#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks: Write a program which asks the user to enter their name and age. The program 
should then output a message that returns this information and calculates the 
year the user will be 100 years old."""

import datetime

name = input("Please let me know your name: ")
age = input("Also your age: ")

print(f"Hello! {name}, You will be 100 years old in {datetime.datetime.today().year + 100 - int(age)}.")
