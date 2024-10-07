a = 12
b = 3

print(a + b)   # 15
print(a - b)   # 9
print(a * b)   # 36
print(a / b)   # 4.0 python divides int numbers to float result by default
print(a // b)  # 4 full integer division
print(a % b)   # 0 remainder after integer division

for i in range(1, a // b):
    print(i)

# Output
# 1
# 2
# 3


# or i in range(1, a / b):
#     print(i)
# will be float and function will not work (1, 4.0)
