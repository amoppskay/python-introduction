# for is used when you have a sequence of items to iterate eg list, tupple, dict, set
fruits = ["kiwi", "grapes", "apples", "watermelon"] #iterating in a list [,,,]

for f in fruits: # 'f' is a temp variable, for each and every iteration, return the item in order
    print(f) # 'f' value keeps changing in each iteration from kiwi, grapes, apple, h20melon

fruits = ("kiwi", "grapes", "apples", "watermelon") # iterating in a tuple (,,,)

for i in fruits:
    print(i)

# iteration in set is not ordered, the order of fruits will keep changing each time we print
fruits = {"kiwi", "grapes", "apples"} # iterating in a set {,,,}

for g in fruits:
    print(g)

mobile_phones = [
    {"name": "lg", "price": "120", "color": "white"},
    {"name": "nokia", "price": "130", "color": "yellow"},
    {"name": "iphone", "price": "140", "color": "black"},
    {"name": "samsung", "price": "150", "color": "pink"}
]

for mobile in mobile_phones:
    print(mobile)
    print(mobile["name"]) # only values of name of name will be printed
    print(mobile["name"], mobile["price"]) # values of name & keys will be printed