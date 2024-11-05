#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
An online retailer offers discounts on the total number of items purchased based 
on the following criteria: 
• No discount for less than 10 items 
• 20% discount for purchases with between 10 and 19 items 
• 30% discount for purchases with between 20 and 30 items 
• 50% discount for purchases with more than 30 items 
Write a program that asks the user to enter the total number of items purchased, 
followed by the price of the sum of all items and then displays the final amount to 
pay, considering any discounts that are applicable.
"""

items = int(input("Enter the total number of items purchased: "))
price = float(input("Enter the price of the sum of all items: "))

if items < 10:
    total = price
elif 10 <= items <= 19:
    total = price * 0.8
elif 20 <= items <= 30:
    total = price * 0.7
else:
    total = price * 0.5

print(f"The final amount to pay is: {total}")