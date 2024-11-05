#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
A weather station records the average temperature every day for 7 days. Write a 
program that allows the user to input the temperature each day for 7 days and then 
displays the average temperature for that week. 
"""

sum = 0

for i in range(1,8):
    temperature_day = float(input(f"Please enter the weather for the day {i}: "))
    sum += temperature_day

print(f"The average temperature for that week is {sum/7}.")
