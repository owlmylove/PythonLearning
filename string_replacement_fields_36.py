age = 24
print("My age is " + str(age) + " years")
# replacing int type to str

print("My age is {0} years".format(age))
# {0} placeholder for age and then formatting data type

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
# mapping of values
# There are 31 days in Jan, Mar, May, Jul, Aug, Oct, Dec

print("There are {0} days in JAN, MAR, MAY, JUL, AUG, OCT AND DEC".format(31))
# mapping of value 31 to {0} days

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}".format(28, 30, 31))
# mapping of days 28, 30, 31 as 0, 1, 2

print()
print("""Jan: {2} 
Feb: {0} 
Mar: {2}
Apr: {1}
May: {2} 
Jun: {1}
Jul: {2}""".format(28, 30, 31))
