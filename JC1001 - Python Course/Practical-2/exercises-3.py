#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program which converts temperature in degrees Fahrenheit to degrees 
Celsius. Your program should include in the output, the original value in 
Fahrenheit that has been converted into degrees Celsius. (a simple way to 
perform this calculation is to deduct 32 from the Fahrenheit temperature, multiply 
by 5 and then divide by 9).
"""

num = int(input("Please enter a temperature in degrees Fahrenheit: "))

print(f"The temperature in degrees Fahrenheit is {num} and in degrees Celsius is {(num-32)*5/9}")
