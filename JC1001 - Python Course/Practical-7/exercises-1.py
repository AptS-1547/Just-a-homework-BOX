#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Write a program to create a Vehicle class with max_speed and mileage 
attributes. Create an instance of this class and print its attributes. 
"""

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

if __name__ == "__main__":
    vehicle = Vehicle(250, 114514)
    print(vehicle.max_speed)
