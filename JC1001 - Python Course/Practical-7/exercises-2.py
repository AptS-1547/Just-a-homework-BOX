#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Modify the Vehicle class from exercise 1 to include a name attribute. Create a 
Bus class which does not contain any attributes or methods. Remember, the 
pass statement can be used to populate the body of a conditional, iterative 
statement or function. That is, when Python expects some code to be present, 
but we have none, we can use the pass keyword. Create an instance of the Bus 
class and print its attributes.
"""

class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = ""

class Bus(Vehicle):
    pass

if __name__ == "__main__":
    vehicle = Bus(250, 114514, "Bus")
    print(vehicle.max_speed)
