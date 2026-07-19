# Program to solve a quadratic equation

import math

# Input coefficients
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

# Calculate the discriminant
d = b**2 - 4*a*c

# Check the nature of roots
if d > 0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print("The roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif d == 0:
    root = -b / (2*a)
    print("The roots are real and equal.")
    print("Root =", root)

else:
    print("The roots are imaginary.")