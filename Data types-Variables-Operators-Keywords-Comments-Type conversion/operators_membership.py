# in and not in are the membership operators; used to test whether a value or variable is in a sequence.

# Python program to illustrate
# not 'in' operator
x = 'J'
y = '@'
name = 'JJ Tech'
fruits = ["banana", "apple", "watermelon"]


print('J' in name)
# "J " is in name so its True
print('vamsi' in name)
# "vamsi" is not on the name list on line 7 False
print("kiwi" not in fruits)
# kiwi is not on list, hence its True
print("n" in name)
# "n" is not on the name in line 7, hence its False
print(x in name)
# line 14 will be true cos x is a variable with J as value, hence there's J in the name JJTech so its True
print("apple" in fruits)
# apple is in fruit list on line 8 so its True
print("kiwi" not in fruits)
# kiwi is not on the list on line 8, hence it's True