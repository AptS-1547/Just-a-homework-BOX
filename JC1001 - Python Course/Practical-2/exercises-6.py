#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
The speed of light c is approximately 3 × 108meters per second. Write a 
program that asks the user to input a time in seconds and returns the distance 
that light travels in this time. Your program should output the distance in meters, 
kilometres, and miles.
"""

time = int(input("Please a time in seconds: "))

meter = time*300000000

print(f"The distance that light travels in this time is {meter} meters, {meter/1000} kilometres, {meter/1000*0.6214} miles")
