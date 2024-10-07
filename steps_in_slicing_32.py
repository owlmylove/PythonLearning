#                   1
#         012345678901234 positive index
parrot = "Norwegian Blue"

print(parrot[0:6:2])   # Nre
print(parrot[0:6:3])   # Nw

# taking characters from index 0 to 6, but not including 6 - Ne
# and adding one more character as a step index 2 between start and end - Nre

number = "9,233;372:036 854,755;807"
separators = number[1::4]
print(separators)
# ,;: ,;

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])
# [9, 233, 372, 36, 854, 755, 807]

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
# MTWTFSS

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
#separators2 = data[::5]
#separators2 = data[0:-1:5]
separators2 = data[:-1:5]
print(separators2)
# 12345678
