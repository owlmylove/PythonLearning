
#                    1         2
#          012345678901234567890123456 positive index
letters = "abcdefghijklmnopqrstuvwxyz"
# in total there are 26 chars and 25 index starting from 0

backwards = letters[25:0:-1]
print(backwards)

# Output zyxwvutsrqponmlkjihgfedcb

print()
backwards = letters[25::-1]
print(backwards)

# from start to the last character including last
# Output zyxwvutsrqponmlkjihgfedcba

print()
backwards = letters[::-1]
print(backwards)
# Output zyxwvutsrqponmlkjihgfedcba
# if we dont mention bakckward last char it means it by default

# Exercises
# letters = "abcdefghijklmnopqrstuvwxyz"

# qpo
backwards = letters[16:13:-1]
print(backwards)

# edcba
backwards = letters[4::-1]
print(backwards)

# last 8 chars in reverse (backward order)
print(letters[:-9:-1])

print(letters[-4:])
# output - wxyz
# print last 4 letters, starting backwards numbers
# [number1:number2] number 1 start of the index and number2 end of the index,
# if number2 is the last index in a string we can leave it empty [number1:]

print(letters[-1:])
# output z
# if number1bindex is the last index in a string then it will be the only output
# the first index from the end is -1, if indexing is starting from -1,
# there will be nothing else as the end of a string

print(letters[:1])
# output a
# starting from the default first index(if its empty [:number2]) 0  and end with 1
# but not included 1

print(letters[0])
# output a
# first and the only index 
