name= input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age < 18:
    print("Please come back in {0} years ".format(18 - age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

# if age from (- ~) to 17 print under if statement applies
# if age >=18 else statement applies
# if age = 900 elif statement applies
