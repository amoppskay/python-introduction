"""
To explain the type conversion concepts
"""

# Example for implicit type conversion
print("# Example for implicit type conversion")
x = 10

print("x is of type:",type(x))

y = 10.6
print("y is of type:",type(y))

z = x + y

print(z)
print("z is of type:",type(z))

# Example for explicit type conversion
print("\n# Example for explicit type conversion")
# initializing string \n will print on a new line, which means there'll be a line in btw the 1st line and 2nd line
s = "10010"

# printing string converting to int
c = int(s)
# print ("After converting to integer: {}, type: {}, name: {}".format(c, type(c), "vamsi"))
print ("\n# After converting to integer: ",c, "type: ",  type(c), "name: ", "vamsi")
print("After converting to integer: {}, type: {}, name: {} .format(c, type(c), osh)")


# printing string converting to float
e = float(s)
print ("After converting to float : {}, type: {}".format(e,type(e)))


# # # Example for explicit type conversion while using input
# input fxn is to take the value that you entered and fill it up where required, it will convert the input to str
print("\n# Example for explicit type conversion while using input")
age = input("\n# Enter your age? ")
print("\n# Age: {}, Type: {}".format(age, type(age)))
new_age = int(age)
print("\n# Age: {}, Type: {}".format(new_age, type(new_age)))
