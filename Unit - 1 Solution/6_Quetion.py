# Write a Python program to check if a certain value exists in a list using membership operators.

# Demonstrating membership operators
my_list = [1, 3, 5, 7, 9]
value = 5

# Using 'in' operator
if value in my_list:
    print(f"{value} is in the list.")
else:
    print(f"{value} is not in the list.")

# Using 'not in' operator
if value not in my_list:
    print(f"{value} is not in the list.")
else:
    print(f"{value} is in the list.")
