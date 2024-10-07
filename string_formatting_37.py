for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))
# mapping {0} {1} {2} values to i, i ** 2, i ** 3
# i = numbers between 1-13
# i ** 2 = i squared (число в квадрате)
# i ** 3 = i cubed (число в кубе)

# Output
# No. 1 squared is 1 and cubed is 1
# No. 2 squared is 4 and cubed is 8
# No. 3 squared is 9 and cubed is 27 etc till 13

print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))
# {0:2} second number after : means the width of value for particular column,
# so for 1 its 2 chars, for i**2 its 3 (as the longest value has 3 digits in it)
# and for i**3 its 4
# values aligned to the right by default

print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))
# adding < {2:<4} aligns values to the left

print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
# adding ^ {2:<4} aligns values to the center

print()
print("Pi is aproximately {0:12}".format(22 / 7))       # float number and 15 chars by default after decimal
print("Pi is aproximately {0:12f}".format(22 / 7))      # adding 'f' to :number2 fixes 6 chars after decimal
print("Pi is aproximately {0:12.50f}".format(22 / 7))   # adding '50f' to :number3 added 50 chars precision(точность) after decimal AND when we specify :number3 THEN python ignores :number2 value
print("Pi is aproximately {0:52.50f}".format(22 / 7))   # every value which is more than 12 for :number2 specifies column width for value
print("Pi is aproximately {0:62.50f}".format(22 / 7))   # so 62 is the width of value column, its aligned to right be default
print("Pi is aproximately {0:<72.50f}".format(22 / 7))  # aligning to the left
print("Pi is aproximately {0:72.54f}".format(22 / 7))  # adding more 4 chars to 50 chars after decimal, note there are 5000 at the end from which 000 means nothing as the are no sense chars after 51 chars

# Output
# Pi is aproximately 3.142857142857143
# Pi is aproximately     3.142857
# Pi is aproximately 3.14285714285714279370154144999105483293533325195312
# Pi is aproximately 3.14285714285714279370154144999105483293533325195312
# Pi is aproximately           3.14285714285714279370154144999105483293533325195312
# Pi is aproximately 3.14285714285714279370154144999105483293533325195312
# Pi is aproximately                 3.142857142857142793701541449991054832935333251953125000t
