#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that asks the user for 20 numbers. Once all the numbers have 
been entered, the sum of all the numbers should be displayed. 
"""

sum = 0

for _ in range(20):
    num = float(input("Enter a number: "))
    sum += num

print("The sum of the numbers is:", sum)
