# comma separated {} = set with no duplicates and unordered, order keeps changing @ 
# every diff runtime

play_list = {"asha", "lagbaja", "rihanna", "davido", "asha"} # will not print asha 2x 
# cos it accepts no duplicates and order

print(play_list)
print(type(play_list))
print(dir(play_list)) # possible fxns of tuple eg add, clear, copy, union, update, pop, intersection etc

play_list.pop() # randomly removes items from the set; takes out 1st item and unorder the values each time you run
print(play_list)

play_list.remove("asha") # removes/takes out specificied/named item in the set eg "asha"
print(play_list)

play_list1 = {"asha", "wizkid", "davido", "kizzdaniel", "kaygold"}
play_list2 = {"wizkid", "davido", "burna", "asha", "asake", "olamide"}
print(play_list1.union(play_list2)) # adds playlist2 to playlist1
print(play_list1.intersection(play_list2)) # returns only the common values in the set