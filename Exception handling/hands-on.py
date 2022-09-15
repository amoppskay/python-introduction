# print("vamsi")
# marks = 85
# result = marks/0
# print(result) # mark cant be divided by 0
# print("hello")
# the exception in line 3 that has an error is causing other lines to be executed, hence line 5 couldnt be executed

# print("vamsi \n")
# marks = 85
# try: # used to handle exceptions
#     result = marks/0
#     print(result) # mark cant be divided by 0
# except:
#     print("unknown error \n")
# print("hello \n")

# print("vamsi \n")
# marks = 85
# try:
#     result = marks/5
#     print(result ) # mark cant be divided by 0
# except:
#     print("unknown error \n")
# print("hello \n")

# print("vamsi")
# marks = 85
# try:
#     result = marks/0
#     print(result) # mark cant be divided by 0
# except: ZeroDivisionError
# print("you cant divide by 0")
# print("hello")

# age = "86"

# try:
#     print(age+10)
# except Exception as e:
#     print(e)

# print("hellloooooo \n")

# try:
#     if type(age) is not int: # change str "" to int. 
#         age = int(age) 
#     print(age+10)
# except Exception as e:
#     print(e)

# print("hellloooooo")

try:
    file_data = open("movies_data.csv", "r")
    print(file_data.read())
except Exception as e:
    print(e)
    print("you should provide proper file path as existing path isnt found \n") 
# use try and except to handle possible exception errors

print("hellloooooo \n")