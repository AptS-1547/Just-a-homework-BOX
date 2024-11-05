#!/usr/bin/python3
# -*- coding: utf-8 -*-
#© 2022-2024 The ESAP Project. Using MIT License

"""Tasks:
Modify the Vehicle class from previous exercises to include the attribute 
capacity. The Vehicle class should have only one method, ticketPrice which 
returns an integer of the capacity multiplied by 100. Create a Bus class which 
inherits from Vehicle but overrides the ticketPrice method, to add an extra 10% 
to the ticketPrice to cover maintenance costs.
"""

class Vehicle:
    def __init__(self, max_speed, mileage, name, capacity):
        self.max_speed = max_speed
        self.mileage = mileage
        self.name = name
        self.capacity = capacity
    
    def ticketPrice(self):
        return self.capacity * 100

class Bus(Vehicle):
    def ticketPrice(self):
        return self.capacity * 110

if __name__ == "__main__":
    myBus = Bus(250, 114514, "Bus", 40)
    print(myBus.ticketPrice()) 
