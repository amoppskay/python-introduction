
"""
To explain the None data type
"""
a = 1
b = 'hello'
c = False
d = None

# # d= "vamsi"

print(a)
print(b)
print(c)
print(d)
# print(len(d))
# it cant print length of d because it is None, empty, nothing to count

# # get the type of None, with type keyword
print(type(a))
print(type(b))
print(type(c))
print(type(d))
# prints the data type of each line <class 'int'> <class 'str'> <class 'bool'> <class 'NoneType'>

# # example usecase for None

blood_group = None
# here since we said None it will return the value stated on line 33 since None is True

blood_group = "0"
# since we put a value for blood_group, it will print the value 'Blood group: 0'

if blood_group is None:
    print('Blood group value is Not Available')
# blood_group output is True hence it will print 'Blood group value is Not Available'

else:
    print('Blood group:', blood_group)
# will give an override. the last overrides the 1st; hence using else will replace line 28 with 31 since we gave diff values for same key/var

