#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Below you have the algorithm of a program that asks the user for a set of positive 
numbers and identifies the highest among them. The user enters the number 0 to 
finish the sequence. Implement the algorithm below and test it. 

EP留言：开始要你根据伪代码来写代码了

Set number with number entered by user  
Set highest with number 
while number is not 0 
    if number is greater than highest 
        Set highest with number 

    Set number with number entered by user 
print highest
"""

highest = 0

while True:
    num = float(input("Please enter a positive number (press 0 to end the input): "))
    if num and highest < num:
        highest = num
    elif num:
        continue
    else:
        break

print("The highest number is", highest)
