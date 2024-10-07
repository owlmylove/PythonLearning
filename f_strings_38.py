name = 'Lilit'
age = 34

print(age)
print(type(age))
print(type(name))

age_in_words = '34 years'
print(age)
print(type(age))

print(name + f" is {age} years old")

#reference lesson 37
print(f"Pi is approximately {22 / 7:12.50f}")
# print("Pi is approximately {0:12}".format(22 / 7))
# so f = .format, f used in python 3.6 and higher
# so we put f before a string brackets value ""
# OR
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")
