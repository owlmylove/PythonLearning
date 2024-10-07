# Truthy Values: A value is considered truthy if,
# when coerced to a boolean, it evaluates to true .
# Examples of truthy values include non-empty strings,
# numbers other than 0, arrays, objects, and functions.
# Falsy Values: Values that are not true are considered False values.

if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")
if name:
    print("Hello, {}". format(name))
else:
    print("Are you a man with no name?")

# we have value name and it should not be empty to have True, otherwise False
# we print text in input brackets and expecting an input for user
# after entering input we print if condition, {} we replace with input name
# we also could use
# if name != "":
# this if statement is more obvious to understand,
# as it says, if name is not an empty string
