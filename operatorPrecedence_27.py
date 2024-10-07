# Operator Precedence - Order of operators
a = 12
b = 3

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a + b) / 3) -4) * 12)
print(((a + b) / 3 - 4) * 12)

c = a + b
d = c / 3
e = d - 4
print(e * 12)

# Order for operations
# Brackets
# Order
# Multiplication/Division - has equal order, left to right
# Addition/Subtraction - has equal order, left to right

print(a / (b * a) / b)
