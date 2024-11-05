#!/usr/bin/python3

#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks: Write a program that asks the user for the following information, first name, last 
name, age, and location. The program should ask for this information and then 
return it to the user"""

"""
python的注释分为单行和多行
注释是给开发人员维护代码和编写注解用的

多行注释由3组引号组成
建议在菜鸟教程自学
"""
# 单行注释从#号开始

print("Hello there! This is The ESAP Project!\nWe will ask some personal information, please follow the instruction and answer it. Thanks!")
# print()函数用于向终端（文本流）输出数据。

# 下方分别定义了4个变量
# 变量名为first_name，last_name，age，location
# 在这里的 = 号是赋值的意思，将右边的参数赋值给左边的变量
# input函数用于向终端获取用户输入信息

first_name = input("What is your first name: ")
last_name = input("What is your last name: ")
age = input("How old are you: ")
location = input("Where do you live now: ")

# 打印我们获取到的信息

print(f"So your name is {last_name} {first_name}, {age} years old and live in {location} now.")
print(f"Goodbye {last_name} {first_name}, have a nice day!")


