#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks: Write a program that asks the user to enter a single word followed by a number 
which is the number of times the word should be repeated. The program should 
then display the word repeated the number of times specified by the user."""

# 接下来我不会写注释，请在菜鸟教程自学

number, word = input("Please enter a single word followed by a number, then I will repeat it: ").split()

for _ in range(0, int(number)):
    print(word)