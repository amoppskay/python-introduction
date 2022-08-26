# students = ["Osh",  "Adetoun", "Priye", "Frank"]
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
driving_rules = ("drive safe", "observe speed limit", "don't drink", "no phones while driving", "use seatbelts")

print(type(driving_rules))

print(driving_rules[2])

driving_rules[3] = "drink & drive"
# this can't be modified, will return error cos its Tuple type