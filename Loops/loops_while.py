# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied.

# For loops are used when you want to do operations on each member of a sequence, in order. While loops are used when you need to: operate on the elements out-of-order, access / operate on multiple elements simultaneously, or loop until some condition changes from True to False.
"""
Syntax:
while expression:
    statement(s)
"""

# Python program to illustrate
# while loop example -1
print('\n# while loop example -1')
wrong_pin_count = 0
while (wrong_pin_count < 6): #while wrong pin entry is btw 0-5, less than 6(number of attempts) until wrong pin is 5x then it is False
    pin_entered = False
    if pin_entered == False:
        wrong_pin_count = wrong_pin_count + 1 #pin count will now be 0+1 up to 5x
        if wrong_pin_count != 6:
            print("Please enter your pin", wrong_pin_count)
        else:
            print("Your pin got blocked", wrong_pin_count)
# while is used for a process that should continue as long as the condition is met  

# # while loop example -2
print('\n# while loop example -2')
count = 10
while (count > 1):
    count = count - 1 # if this line commented, it will return infinitely, infinite loop
    print("Hello JJTech, decreasing", count) #values start from 9 & decreases till 1 cos its index of 1

# # example of infinite while loop
# print('\n# example of infinite while loop')
# count = 0
# while (count < 5):
# 	print("Hello JJTech, infinite loop")
