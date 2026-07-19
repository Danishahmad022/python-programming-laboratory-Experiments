# Swap two variables

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print("Before swapping:")
print("a =", a)
print("b =", b)

# Swapping
a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)