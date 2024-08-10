# Write a Python program to evaluate an expression and explain the role of operator precedence in the result.

# Demonstrating operator precedence
expression = 10 + 2 * 3 ** 2 / 4 - 5

# Calculating the expression
result = expression

print("Result of the expression:", result)


# In the expression 10 + 2 * 3 ** 2 / 4 - 5, the operators are applied based on their precedence:

# Exponentiation (**) is performed first: 3 ** 2 = 9.
# Multiplication (*) and Division (/) are performed next (from left to right): 2 * 9 / 4 = 18 / 4 = 4.5.
# Addition (+) and Subtraction (-) are performed last: 10 + 4.5 - 5 = 9.5.