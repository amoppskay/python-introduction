# Dictionaries are used to store data values in key:value pairs.
"""
– When you need a logical association between a key:value pair.
"""

student = {"name": "vamsi", "age": "25 years", "college": "abc-college"}
fruits = {"apple": 5, "banana": 3.50, "watermelon": 2.75}
friends = {"class-1": ["david", "ricci"], "class-2": ["john", "matheus"]}

# print dictionary
print('\n # print dictionary')
print(student)
# students' dictionary list is returned
print(fruits)
# fruits dictionary is returned
print(friends)
# friends in dictionary list is returned

# # access dictionary items
print('\n # access dictionary items')
print(student["name"])
# returns names on the dictionary list of students
print(fruits.get("apple"))
# .get is a fxn attribute of dictionary that gives the value of apple = 5
print(friends["class-2"])
# class-2 on friends dictionary has 2 name, John n Matheus

# # check if key exists in a dictionary
print('\n # check if key exists in a dictionary')
if 'watermelon' in fruits: #in is membership operator; if is conditional statemenr
    print(fruits['watermelon'])
else: #otherwise or if not
    print('requested key not found')
# returns the value of watermelon on the fruits dictionary
# since watermelon exists, it returned the value 2.75 if not "requested key not found"

if 'class' in student: # in is membership operator; if is conditional statement
    print(student['college'])
else: # otherwise or if not
    print('requested key not found')
# conditional statement (if; else) since there's no class in student dictionary, it returned
# "requested key not found"


# # check the data structure type of these values
print('\n # check the data structure type of these values')
print(type(student))
print(type(fruits))
# both types (student and fruit) are dictionary (dict)

# # check the methods and attributes available for the dictionary variable
print('\n # check the methods and attributes available for the dictionary variable')
print(dir(student))
# returns all the attribute fxns that dictionary supports (.get, .update, .pop, .clear, .items) etc


# # check dictionary length
print('\n # check dictionary length')
print(len(student))
print(len(friends))
# returns the count of keys and values (after comma separated) in students = 3 and friends = 2

# # get the keys of dictionary with keys() method
print('\n # get the keys of dictionary with keys() method')
print(student.keys())
# result of keys only in the dictionary student ('name', 'age', 'college')

# # get the values of dictionary with values() method
print('\n # get the keys of dictionary with values() method')
print(student.values())
# result of values in the dictionary student ('vamsi', '25 years', abc-college')

# # copy all the dictionary data into another variable
print('\n # copy all the dictionary data into another variable')
duplicate_student = student.copy() # = is assignment operator to modify/change 1 to another
# another dictionary named duplicate_student is created which value is student.copy
print(student)
# returns results of student dictionary  {'name': 'vamsi', 'age': '25 years', 'college': 'abc-college'}
print(duplicate_student)
# returns result of duplicate_student {'name': 'vamsi', 'age': '25 years', 'college': 'abc-college'}

# # modify an existing key value in dictionary
print('\n # modify an existing key value in dictionary')
student['name'] = 'vamsi krishna chunduru' # = assignment operator to modify vamsi to vamsi krisna..
print(student)
# name changed/modified from 'vamsi' to 'vamsi krishna chunduru' using (=)

# # delete a key from the dictionary
print('\n # delete a key from the dictionary')
if 'college' in student: # if for conditional statement; in is membership operator
    student.pop('college') # .pop is used to remove the key&values 
    print(student)
else: # otherwise or if not
    print('key not found')
# since college was removed above using .pop, it returned 'key not found'

# # add a new key value to dictionary
print('\n # add a new key value to dictionary')
student['college'] = 'abc-college' # = assignment operator to modify/change 1 value to another
print(student)
# since we removed 'college' from the dictionary earlier, we added it back using its key&value


# # iterate over a dictionary keys

print('\n # iterate over a dictionary keys')
for key in student.keys(): # 'for' means 'looping' it is used for repetitive tasks
    print(key)
# iterates over the dictionary students & returns keys in order on separate lines

# # iterate over a dictionary values
print('\n # iterate over a dictionary values')
for val in student.values():
    print(val)
# iterates over the student dictionary & returns values in order on separate lines

# # iterate over a dictionary key,value pairs
print('\n # iterate over a dictionary key,value pairs')
for key,val in student.items():
    print(key, val)
#  iterates over student dictionary & returns keys&values in order on separate lines 

# # clear all key-value from dictionary
print('\n # clear all key-value from dictionary')
student.clear()
print(student)
# clears all the keys&values in student dictionary

# # delete the complete dictionary
# print('\n # delete the complete dictionary')
# del student
# print(student)