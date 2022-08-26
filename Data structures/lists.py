#  List will be helpful to store multiple items in a single variable.

"""
– Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
"""


# list variables
fruits = ["banana", "apple", "watermelon", "kiwi", "grapes"]
prices = ["$100", "$150", "$10.50"]
# # put "" when you have $ or other signs beside numbers to return the value with the sign
numbers = [1, 2, 3, 4, 5]
my_list = [1, "car", 10.40, True]
# # line 12 has a mix of data types which is allowed in python

# # printing the list items
# print('\n# printing the list items')
# print(fruits, id(fruits))
# # id will return the memory location on my computer
# print(prices)
# print(numbers)
# print(my_list)

# # # check the data type
# print('\n# check the data type')
# print(type(fruits))
# print(type(numbers))
# # this will return the data structure type which is list

# # nested list
# print('\n# nested list')
# my_custom_list = [fruits, prices, [6, 10, 2]]
# print(my_custom_list)
# # nested list puts multiple lists together on one list (list inside a list)


# # length of list
# print('\n# length of the list')
# print(len(fruits))
# # return the numbers of item/fruits in a list rather than counting

# # access a specific element in list
# print('\n# access a specific element in list')
# print(fruits[2])
# # returns the 3rd fruit on the list since index starts from 0, in coding we count from 0
# print(fruits[0])
# # returns the 1st fruit on the list
# print(fruits[-1])
# # returns values in reverse order, from the last. for -1 the fruit is grape
# print(fruits[-2])
# # returns value of the 2nd to last fruit on list, since it's in reverse order

# # slicing lists
# print('\n# slicing lists')
# print(fruits[0:2])
# # returns list of fruits(item) btw 0 - 2 (range)
# print(fruits[1:4])
# # returns list of fruits(item) btw 1 - 4 (range)
# print(fruits[1:])
# # returns list of fruits from index 1 to the end regardless of the number of fruits(item) on the list

# # peform actions on list
# # return attributes and methods of an object
# print('\n# dir() method')
# print(dir(fruits))
# dir returns the no of fxns that can be performed on any data structrre eg list, int etc

# print(fruits.count("banana"))
# count is a fxn of the list data structure, hence it will return the number of 
# times banana appears on the list, if it's once it will return 1 if twice it will be 2

# modify particular index of list with new item
# print('\n # modify particular index of list with new item')
# print(prices)
# prices[1] = '$1000'
# = is assignment operator, hence it will replace index 1 with $1000 and take out 
# value on index 1 with the new one (used to change an existing value by calling with the index)
# print(prices)

# fruits.insert(3, "mango")
# insert fxn to insert mango to index 3
# print("fruits:", "mango")
# prints mango
# print("list:", fruits)
# prints list of fruits which now has mango added on index 3 on the fruit list
# print(fruits [0:])
# lists fruits from index 0 to the last fruit/item on the list

# append items to existing list
print('\n# append() method')
fruits.append("mango")
# adds mango to the list
print(fruits)

# sort the list
print('\n# sort() the list')
fruits.sort()
# gives the list in alphabetical order
print(fruits)

# insert item at a particular index
print('\n# insert item at a particular index')
fruits.insert(1,'grapes')
# inserts grape to index 1, changes the index q where grape was to 1 
print(fruits)

# remove an item from the list
print('\n# remove an item from the list')
fruits.remove('watermelon')
# removes watermelon from the list of fruits
print(fruits)

# iterate over all items in the list, one after another
print('\n# iterate over all items in the list, one after another')
for fruit in fruits:
    print(fruit)
# "for" is an  itirator used to call the values of each fruit variable 1 after the other. 

# iterate over each item in the list along with item index
print('\n# iterate over each item in the list along with item index')
for index, each_item in enumerate(fruits):
    print(index +1, each_item)
# using enumerate fxn to print along with index. This will give the value and its index
# add +1 for the 1st index to begin with 1 and not 0

# list with dictionaries inside
print('\n# list with dictionaries inside')
marks = [{"name": "vamsi", "marks": 50}, {"name": "avinash",
                                          "marks": 60}, {"name": "showmik", "marks": 70}, ]
print(marks)
# 


# clear a list
# print('\n # clear a list')
# fruits.clear()
# print(fruits)

 # delete the complete list

