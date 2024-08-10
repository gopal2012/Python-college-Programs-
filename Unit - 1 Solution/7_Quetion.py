# Write a Python program to check if two variables reference the same object in memory using identity operators.

# Demonstrating identity operators
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print("a is b:", a is b)  # True, since b is assigned to a
print("a is c:", a is c)  # False, c is a new list with the same content
print("a == c:", a == c)  # True, content of a and c is the same
