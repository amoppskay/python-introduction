# To explain the python boolean data type

# observe the difference between string and boolean, string value will have '' or "" symbols surrounded
# where as here True, False are recognized by Python

print(True)
print(False)

a = True
b = False
# single = takes what is on the right side (True/False) and replaces it with what is on the left side (a/b) (assignment operator) key = value

print(a)
print(b)

print(10 > 9)
# 10 is greater > than 9 so it will print True

# print(10 == 9)
# # == is used in programming to check if 10 = 9 which is False (comparison operator) both values are diff 
# print(10 == 10)
# # this will print True

tutor = "Osh"
developer = "Osh"
print(tutor == developer)
# /it will return True since we set the variable/key=value on lines 23 & 24 

print(10 < 9)
# this will print/return False cos 10 is not less than (<) 9


# print the type of data, using python keyword called type
print(1 == 1, type(1 == 1))
# this will print 2 values, it will return True for 1 == 1, then print type of 1 == 1 which is bool (True <class 'bool')

x = 5 > 4
print(x, type(x))
# 5 > 4 is True in line 38, it will print the value of x as True and print the type which is bool (True <class 'bool')

y = 5 < 4
print(y, type(y))
# 5 < 4 is False in line 41, it will print the value of y as False and print the type which is bool (False <class 'bool')

print("True", type("True"))
# it will print True as string data type since it is in "", string takes "", boolean takes no "" hence it will return True <class 'Str'>

print("10", type("10"))
# this will print 10 <class 'str'> cos its in "" integer is number with no ""