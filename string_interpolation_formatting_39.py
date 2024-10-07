age = 24
print("My age is %d years" % age)
# %d is an integer value, which is provided by value age, mentioned with % '%age'
print("My age is {0} years".format(age))
print("My age" f" is {age} years")

major = "years"
minor = "months"
print("My age is %d %s, %d %s" % (age, major, 6, minor))
# %s is a string placeholder with int values under %d
print("PI is approximately %f" % (22 / 7))
# %f is a placeholder for float value which is provided by % and calculated 22 / 7
print("PI is approximately %60.50f" % (22 / 7))
# width of column 60 and 50 values after decimal

# %d - decimal - int
# %s - string
# %f - float
