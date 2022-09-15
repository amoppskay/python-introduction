# x = 1
# while x > 0:
#     print("darey")
# # prints till infinity cos the condition is met, x is always > 0

# x = 0
# while x < 0:
#     print("darey")
# # prints till infinity cos the condition is met, x is always < 0


# pin_code = int(input("What is your pin? "))
# wrong_pin = 0
# while pin_code != 2022 and wrong_pin < 5:
#     if pin_code != 2022 and wrong_pin <= 5:
#         print("Please enter your pin again")
#         pin_code = int(input("What is your pin? "))
#         wrong_pin = wrong_pin + 1
#         if pin_code== 2022 and wrong_pin < 5:
#             print("You have entered the right pin, pls proceed to the next step")
#         elif pin_code != 2022 and wrong_pin == 5:
#             print("Your card is now blocked")
    
# # another twick to the 
# pin_code = 0
# user_pin = 2022
# wrong_pin = 0
# while True:
#     pin_code = int(input("Enter your four digit pin "))
#     if pin_code != user_pin and wrong_pin < 2:
#         wrong_pin += 1
#         print("Please Try Again")
#     elif pin_code == user_pin and wrong_pin <= 2:
#         print("Pin is a match")
#         break
#     elif pin_code != user_pin and wrong_pin == 2:
#         print("Card has been blocked")
#         break   

i = 0

while i<=5:
    # print("Hello World")
# the value of i is less than 5, it will keep printing Hello World as it's always True, it will keep iterating cos its infinte loop
# while will iterate over a condition to see if its True and return the value 
    i = i+1
    print("Hello World", i) #this makes the loop false, so it will add index from 0-5 with "Hello World"

pin_count = 0

while pin_count <6:
    pin_entered = False
    if pin_entered == False:
        pin_count = pin_count + 1
        if pin_count <6:
            print("Wrong password, Try again:)")
        else:
            print("your pin got blocked, try agin in 5 mins")



