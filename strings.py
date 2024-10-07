name = 'Lilit'
age = 34

print(age)
print(type(age))
print(type(name))

agestr = '34 years'
print(age)
print(type(age))

# We cannot concatenate different data types in one print
print(name + age + agestr)

# TypeError: can only concatenate str (not "int") to str
