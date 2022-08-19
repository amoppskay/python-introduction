# is and is not are the identity operators both are used to check if two values are located on the same part of the memory. Two variables that are equal do not imply that they are identical. 

a = 10
b = 20
# c = a
c = 10

print(a is not b)
print(a is b)
print(a is c)

m = "abcd"
print("abc" is m)
print("abcd" == m)
# line 14 is checking if it's equal to which will return true
# whwenever "is" is used, it is to check if it comopares or is identical to or not