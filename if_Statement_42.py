name= input("Please enter your name: ")
age = input("How old are you, {0}? ".format(name))
# if we dont specify the age value type, as we want to mention user's name when ask age
# then input will accept a string type, but we need an int for age
print(age)

# Output
# Please enter your name: Lilit
# How old are you, Lilit? ten
# ten

name= input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
# age accepts only int input

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("Please come back in {0} years ".format(18 - age))
# if condition is this:
#   do this
# else:
#   do this
