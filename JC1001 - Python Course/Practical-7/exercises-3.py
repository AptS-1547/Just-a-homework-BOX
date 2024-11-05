#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Modify the Vehicle class from exercise 1 and 2, to a method, seating_capacity. 
This method should return a string that reports the name of the vehicle and the 
seating capacity. Within the Bus class, override the seating_capacity method so 
that the default value of seating capacity is set to 40. Instantiate the Bus class 
as before, then print a call from the Bus object calling the seatingCapacity 
method i.e. print(myBus.seatingCapacity()) 
"""

class Vehicle:
    def __init__(self, max_speed, mileage, name):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.seating_capacity = 4
    
    def seatingCapacity(self):
        return f"The {self.name} has a seating capacity of {self.seating_capacity} passengers."

class Bus(Vehicle):
    def seatingCapacity(self):
        return f"The {self.name} has a seating capacity of 40 passengers."

if __name__ == "__main__":
    myBus = Bus(250, 114514, "Bus")
    print(myBus.seatingCapacity()) 
