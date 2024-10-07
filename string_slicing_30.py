#             1
#         43210987654321 negative index
#                   1
#         012345678901234 positive index
parrot = "Norwegian Blue"

print(parrot[0:6]) # Norweg
print(parrot[:6])  # Norweg

# by default all slicing starts from 0, its not necessary to mention it
# ends on second number, but not including 012345=Norweg

print(parrot[3:5]) # we

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])
print(parrot[:])

# Negative slicing
print()
print(parrot[0:6])
print(parrot[-14:-8])

print(parrot[-4:-2])
print(parrot[-4:12])
