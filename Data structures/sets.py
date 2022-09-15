# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set.
# The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set.
"""
– Use a set if you need uniqueness for the elements.
"""
numbers = {10, 20, 5, -3}
students = {"vamsi", "avinash", "showmik"}
fruits = {"apple", "banana", "orange"}
my_set = {10, 20, 'apple', 'car'}

# print set
print('\n # print set')
print(numbers)
print(students)
print(fruits)
print(my_set)


# # what will happen when we try to add duplicate element to the set
# # even though we try it wont let as add it as the same item already exists in the set
# # we can correlate with the playlist of songs
print('\n #test items duplication in the set')
duplicate_item_set = {10, 20, 30, 10} # =assignment operator to create duplicate_item_set
print(duplicate_item_set)
#last 10 will not be on the set cos set doesnt support duplication

# # Indexing --> set doesnt suppport indexing like lists & tuples
# # so hence You cannot access items in a set by referring to an index or a key.
# #  But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
print('\n #indexing check in the set')
# print(students[0])
# set doesnt support index cos it is unordered

# # check if an item exists in the set
print('\n # check if an item exists in the set')
print('vamsi' in students)
# in is membership operator to check if vamsi is present in students which is True
if 'apple' in fruits: #if is conditional statement; in is membership operator
    print('yes') # check if apple is present in the fruit set, if it is print yes
else: # otherwise/if not
    print('no')
# membership of apple in fruit is yes, if not "no"

# # check type of the set variables with type() method
print('\n # check type of the set variables with type() method')
print(type(numbers))
print(type(students))
# data type of student/number which is 'set'

# check the methods and attributes available for the set variable
print('\n # check the methods and attributes available for the set variable')
print(dir(students))
# attribute fxns that are supported by set (student. )

# check set length
print('\n # check dictionary length')
print(len(students))
print(len(my_set))
# count of students value in students & my_set

# # adding an a new item or modifying an item in set
# # wont happen because we have already seen that set doesnt support indexes so we cant assign values with index
# print('\n # adding an a new item or modifying an item in set')
# # students[0] = 'jenny'
# # print(students)

# # so the correct way to do it is via the set built-in method add()
students.add("jenny")
print(students)
# instead use the attribute fxn .add to include jenny on the set, index isnt considered in set
# it could add it anywhere on the set not in order

# # what will happen if we try to add the same value (remember set cant have a duplicate value)
print('\n # what will happen if we try to add the same value (remember set cant have a duplicate value)')
students.add('avinash')
print(students)
# avinash is on the set list, it wont add avinash cos its a duplicate

# # add multiple values to an existing set
print("\n # add multiple values to an existing set")
students.update(["jermy", "thomas", "kenny"])
print(students)

# # remove an existing item from the set
print("\n # remove an existing item from the set")
students.remove("jenny")
print(students)
# removes jenny from the set

# lets understand what will happen when we try to delete an item that doesnt exists in the set
# it will throw an error saying that the item key isnt found in the set
# students.remove("jenny") cos jenny has been removed earlier

# # lets understand how to easily delete if a key exists otherwise ignore instead of raising an error
print('\n # lets understand how to easily delete if a key exists otherwise ignore instead of raising an error')
if 'jenny' in numbers: # conditional statement
    numbers.remove('jenny') #if jenny is on the set, remove jenny
    print(students)
else: # otherwise/if not
    print('given item not found to delete') #if it's not on the set return 'given item not...'
    print(students)

# # other way to do the same step as above is using discard() method which is really simple
print('\n #trying deletion via discard')
students.discard('thomas')
students.discard(12345)
print(students)
# it removes straight unlike remove that throws an error that the item isn't in the set if not found
# discard is unlike remove that will throw an error if the value isnt in the set, 


# # iterate over all items in set and access individual items
print('\n # iterate over all items in set and access individual items')
for i in students: # iterate over th1e values in students and prints them in order in separate lines
    print(i) # i could be any temporary value, it could be each_student or any word

# # set union
# # reminder --> set wont have duplicates so even after union no duplicates
print("\n # set union")
u = numbers.union(my_set)
print(u)
# combines all the variables into a set, by performing a union, it takes out the dup value

# # set intersection --> to get common data between two sets
print("\n # set intersection --> to get common data between two sets")
i = numbers.intersection(my_set)
print(i)
# intersection is for common values in a set, 10, 20

# # clear all items from set
# print('\n # clear all items from set')
# students.clear()
# print(students)
# clears all the values in the set

# # delete the complete set
# print('\n # delete the complete set')
# del students
# print(students)
# no values students found cos it has been cleared early



