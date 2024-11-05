#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program that reverses the calculation performed in exercise 7, where the 
user enters a duration in seconds and the duration is returned to the user in days, 
hours, minutes, and seconds, with each unit of time printed on a separate line.  
"""

second = int(input("Please enter a duration in seconds: "))

day = second//86400
second -= day*86400
hour = second//3600
second -= hour*3600
minute = second//60
second -= minute*60

print(f"The duration is {day} days")
print(f"The duration is {hour} days")
print(f"The duration is {minute} days")
print(f"The duration is {second} days")
