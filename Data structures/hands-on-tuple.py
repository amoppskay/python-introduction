traffic_signals = ("red", "green","amber")

# print(traffic_signals)
# print(type(traffic_signals)) # prints data type of 'traffic_signals = tuple
# print(traffic_signals[0]) # prints the traffic_signal with index 0 on the tuple list = red
# print("yellow" in traffic_signals) # in = membership operator to check if yellow is in traffic_signals, false cos its not
# print(dir(traffic_signals)) # fxns suppported by tuple
# print(traffic_signals.count("red")) #count is to know how many times an item occur in a tuple
# tuple has only 2 dir fxns, count & index cos its immutable

traffic_signals[1] = "blue" # trying to change the value in index of 1 to blue
print(traffic_signals) # will return an error cos tuple doesn't allow a change/immutable

# fruits = ()
# print(fruits)
# # its an empty tuple that cant be modified with code after creation, can only be modified in the body of the variable not using a code
# fruits = ("apple", "banana")
# print(fruits)

#  tuple can only be created in 2 ways  - by calling 'tuple()' or by using ()comma separated
#  you can have diff data types in tuple - str, list, bool etc but the values can't be changed
#  at runtime only at the pt of creation/in the variable