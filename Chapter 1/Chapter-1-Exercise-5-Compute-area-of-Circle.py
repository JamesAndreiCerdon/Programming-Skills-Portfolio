"""Chapter 1 Exercise 5: Compute area of Circle
Write a Python program which accepts the radius of a circle from the user and compute the area."""

#import the file pi from python database and use float to calculate the radius
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))

