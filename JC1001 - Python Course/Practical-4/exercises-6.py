#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Running on a treadmill at a constant speed burns 9.7 calories per minute. Write a 
program that uses an iterative statement to display the number of calories burned 
after 10, 15, 20, 25 and 30 minutes.
"""

for minutes in range(10, 31, 5):
    calories_burned = minutes * 9.7
    print(f'Calories burned after {minutes} minutes: {calories_burned:.1f}')
