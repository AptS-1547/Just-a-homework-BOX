#!/usr/bin/python3

# © 2022-2024 The ESAP Project. 使用 MIT 许可证

"""
任务:
编写一个程序，询问用户的姓名和年龄，然后计算他们的出生年份并将此信息返回给用户。
"""

import datetime  # 导入 datetime 模块，用于处理日期和时间

# 询问用户的姓名
name = input("请告诉我你的名字: ")

# 询问用户的年龄
age = input("还有你的年龄: ")

# 计算用户的出生年份
# datetime.datetime.today().year 获取当前年份
# int(age) 将用户输入的年龄转换为整数
birthday = datetime.datetime.today().year - int(age)

# 输出用户的姓名和出生年份
print(f"你好！{name}, 你的出生年份是 {birthday}.")