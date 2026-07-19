# Program to find the area of a triangle using Heron's Formula

import math

# Input the three sides of the triangle
a = float(input("Enter first side (a): "))
b = float(input("Enter second side (b): "))
c = float(input("Enter third side (c): "))

# Calculate the semi-perimeter
s = (a + b + c) / 2

# Calculate the area
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Display the result
print("Area of the triangle =", area)