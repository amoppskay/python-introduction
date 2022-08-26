# A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.
"""
– Use tuples when your data cannot change.
"""

numbers = (1, 2, 3)
names = ('vamsi', 'avinash', 'showmik')
fruits = ('apple', 'banana', 'orange')
my_tuple = (10, 20, 30, {"name": "vamsi", "age": 22},
            ['car', 'bike', 'bus'], 10)
# mixed tuple with list, dic, int, string

# print tuples
print('\n # print tuples')
print(numbers)
print(names)
print(fruits)
print(my_tuple)


# # verify the type of data structure
print('\n # verify the type of data structure')
print(type(numbers))
print(type(names))
# returns type as Tuple


# # access tuple items
# print('\n# access tuple items')
print(names[0])
print(numbers[1])
print(my_tuple[4])
# similar to list using index to call the values

# # check if item exists in the tuple
print('\n # check if item exists in the tuple')
print(10 in numbers)
# check if it belongs to the tuple, there's no 10 hence its false

if 'banana' in fruits:
    print("yes")
else:
    print("no")


# # check the methods and attributes available for the tuple variable
print('\n # check the methods and attributes available for the tuple variable')
print(dir(names))
# other fxns that can be used with tuple

# # check tuple length
print('\n # check tuple length')
print(len(names))
print(len(my_tuple))
# count the number of items in names and my_tuple

# # get number of times an items is present in the tuple
print('\n # get number of times an items is present in the tuple')
print(my_tuple.count(10))
print(names.count("avinash"))
# count is to know how many times a value got repeated or called. Avinash=1x, 10=2x

# # get the index of an item in the tuple
print('\n # get the index of an item in the tuple')
print(names.index("vamsi"))
print(fruits.index("orange"))
# get the index of vamsi in names tuple = 0; get the index of orange in fruits tuple = 2


# # iterate over items in the tuple
print('\n # iterate over items in the tuple')
for each_item in names:
    print(each_item)
# lists the names in order on the tuple; Vamsi, Avinash, Showmik

# # modify the tuple WE CANT MODIFY AN EXISTING TUPLE, with the below examples we can understand tuples are immutable
numbers[0] = 100
names[1] = 'captain america'
names.append('iron man')
names.clear()
# gives an error cos the fxns append, clear aren't supported in tuple; the name isn't in the tuple

# # delete the tuple completely
print('\n # delete the tuple completely')
del(names)
print(names)
# deletes the tuple
# you can only modify with iterator using "for loop"
# to modify or change, you have to go to the assigning value to either add or delete