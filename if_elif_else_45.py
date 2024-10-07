answer = 5

print("Please enter a value between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please try higher value")
elif guess > answer:
    print("Please try lower value")
else:
    print("You guess with first try. Good job!")

# this is just a print text
# once you start typing cursor goes to the next line,
# which means the input doesnt relates to print function
# ONCE the number is printed under guess THEN if statement starts
