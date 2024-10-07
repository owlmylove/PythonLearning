age = int(input("How old are you? "))

# if age >= 16 and age <= 65:
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# AND condition is True only if both conditions are True
# OR condition is True even if only one condition is True

# How old are you? 34
# Have a good day at work
# --------------------------------------------------------------------------------
# Have a good day at work
