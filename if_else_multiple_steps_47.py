# reference 45 lesson
answer = 5

print("Please enter a value between 1 and 10: ")
guess = int(input())

# if guess < answer:
#     print("Please try higher value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have not guessed correctly")
# elif guess > answer:
#     print("Please try lower value")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You guess with first try. Good job!")

# added one more block of if else inside main blocks if/elif
# we can have a lot of elif, but only one else

# OPTIMISED CODE, the code below do the same thing as the above

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


if guess == answer:
    print("You got it first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done you guessed it")
    else:
        print("Sorry, you have not guessed correctly")
