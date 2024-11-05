#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that first asks the user to enter a duration in days, hours, 
minutes, and seconds. Use a similar approach to exercise 6, where first the 
program will ask for the duration in days, followed by hours, minutes etc. Your 
program should then return the total number of seconds of the full duration 
entered. 
"""

day, hour, minute, second = input("Please enter a duration in days, hours, minutes, and seconds, using space spacing: ").split()

print(f"The total number of seconds of the full duration is {int(day)*86400 + int(hour)*3600 + int(minute)*60 + int(second)}")
