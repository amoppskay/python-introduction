# examples for int data type
# print(10+20)
# print(100)

# quantity = 10
# price = 3
# print(quantity*price)

# item_quantity = 1018935
# item_price = 303456
# print(item_quantity*item_price)

# print(type(1))
# type(100)
# # no fxn value on lne 14 because you didnt ask it to print
# print(type(100))

# examples for string data type which must be in ("")
# print("Titi")
# student = "Titi"
# student = "Adetoun"

# print(student)
# print(type(student))

# print(student, " is now in JJTech")
# student is used a variable, hence it isnt in "" so student becomes a key and will return the value of whatever 
# name we put as student

# print(True) 
# print(False)
# print(type(True))
# print(type(False))

# is_paid = False
# print("Doors open", is_paid)

# is_paid = True
# print("Doors open", is_paid)

# blood_group = None
# dont add  "" so it doesnt look like string, python picks it as None data type
# print(blood_group)

# print(type(None))
# this will print type as <class 'NoneType'>

# a = 2
# b = 4
# print(a + b)

# logical comparison
# maths = 47
# science = 70
# pass_mark = 35
# if maths >= pass_mark and science >= pass_mark: 
#     print("test passed")
# else:
#     print("test failed") 
# this will return pass since both scores are greater than pass_mark

# maths = 25
# science = 34
# pass_mark = 35
# if maths >= pass_mark and science >= pass_mark: 
#     print("test passed")
# else:
#     print("test failed") 
# this will return failed since both scores are less than pass_mark

# maths = 25
# science = 34
# pass_mark = 35
# if maths >= pass_mark or science >= pass_mark: 
#     print("test passed")
# else:
#     print("test failed") 
# this will return failed since both scores are less than pass_mark

"""
maths = 47
science = 70
pass_mark = 35
if maths >= pass_mark or science >= pass_mark: 
    print("test passed")
else:
    print("test failed") 
# this will return pass since both scores are greater than pass_mark
"""

chocolate = 18
coffee = 30.50
print(coffee+chocolate)
# python automatically does implicit conversion here, since one is int data type and the other is float type
# implicit is automatic conversion during operation

age = 35.5
print(age)
# above will return the age as it is written on line 97 which is float
print(int(age))
# above will convert the result from float to int as we asked it to convert the result to int not float