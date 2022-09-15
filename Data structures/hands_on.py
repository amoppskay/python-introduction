students = ["Osh",  "Adetoun", "Priye", "Frank"]
# print(students)

# print("Osh" in students)
# above line will check if Osh is on the list of studrnts and return True

# students.append("Vamsi")
# print(students)
# append will add what we have stated (vamsi) to the list
# to use list, just put . other operations will auto populate 

# students.remove("Osh")
# print(students)

# print(dir("students"))

# name = "Titi is good"
# print(name.endswith("good"))
# print(name.endswith("is"))
# endswwith is used with a string not a list, it will return True if the string 
# ends with the word stated or False if not

# tuple
# driving_rules = ("drive safe", "observe speed limit", "don't drink", "no phones while driving", "use seatbelts")

# print(type(driving_rules))

# print(driving_rules[2])

# driving_rules[3] = "drink & drive"
# this can't be modified, will return error cos its Tuple type

# sets
# wish_list = {"aws", "devops", "terraform", "cfn", "ansible", "aws"}
# print(wish_list)
# print(type(wish_list))

name = "Titi   "
email = "titi@jjtech,com"

# print(dir(name))
# print(name.strip().replace("T", "J"))
# print(len(name), len(name.strip()))
# print(name.upper())
# print(name.capitalize())
# print(name.join("Ogunsina"))
# print(name.join(["Ogunsina", "Monisola"]))


# for each_student in students: # # for is to loop 
#     print(each_student.upper()) # #upper is an attribute fxn used with list data type/structure
# loops are used to avoid repetition, it will iterate over each value 1 @ a time 
# and the return the value of each student on the list in Upper case on separate lines
