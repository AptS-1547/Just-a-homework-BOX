#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
In the Gregorian calendar, the length of a month varies from 28 to 31 days. Write 
a program that reads the name of a month from the user as a string. Then 
displays the number of days in that month. 

Hint: If the month is Feb, then it should display “28 or 29 days” to take leap years 
into account.
"""

month = input("Enter the name of the month: ")

if month in ("January", "March", "May", "July", "August", "October", "December"):
    print(f"{month} has 31 days")
elif month in ("April", "June", "September", "November"):
    print(f"{month} has 30 days")
elif month == "February":
    print(f"{month} has 28 or 29 days")
else:
    print("Please enter a valid month name")