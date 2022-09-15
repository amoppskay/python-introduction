# list is identified by [] comma separated
#print(["iphone", "nokia", "samsung", "LG", "alcartel", "motorola"])
#print(type(["iphone", "nokia", "samsung", "LG", "alcartel", "motorola"]))
# lists above has no variables, best to declare variables as done below

mobile_phones = ["iphone", "nokia", "samsung", "LG", "alcartel", "motorola"]
fruits = ["mango", "apple", "banana", "watermelon"]

# print(mobile_phones)
# print(type(mobile_phones))
# print(len(mobile_phones))
# print(mobile_phones [2]) # prints the item on index count of 2 = samsung

# mobile_phones[1] = "palasa" # replacing nokia with index 1 on the list with palasa
# print(mobile_phones)
# fruits[2] = "kiwi" # replacing banana with kiwi
# print(fruits)

# print(fruits)
# print(type(fruits))
# print(len(fruits))
# print(fruits [2])

# print(dir(fruits))
# print(dir(mobile_phones)) #only supported fxnalities are allowed eg append is a fxn used with list not string3

# mobile_phones.append("itel") #you can only append an item at a time, not more than 1
# print(mobile_phones)
# fruits.append("banana") #you can only append an item at a time, not more than 1
# print(fruits)

# mobile_phones.reverse() # starts the list in reverse order
# print(mobile_phones)

# # mobile_phones.extend(fruits) # etend fxn adds mobile_phone and fruits lists 2geda @ the end
# #print(mobile_phones)
# # mobile_phones.remove("palasa") # removes 'palasa' from the list
# # print(mobile_phones)

# list can be declared using empty [] or by typing the word 'list'
friends = list()
print(list) # prints the class of as list
print(friends) # prints empty list as there's no value in the variable 'friends'

# list is a for a sequence of values and accepts duplicates and additions, removal, reverse etc