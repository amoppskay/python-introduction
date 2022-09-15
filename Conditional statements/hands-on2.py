# raining = True

# if raining == True:
#     print("take umbrella or don't go out")

# print("Go to the mkt") # outside the condition so it is not related to it and will always be executed

# # the code below wont print because both conditions have to be True else, it wont print. this is for just 1 argument
# raining = False

# if raining == True:
#     print("go out")

# price = 1000
# budget = 800

# if budget >=price:
#     print("buy it")
# else:
#     print("check for what your money can buy")    

# bill_paid = True

# if bill_paid == True:
#     print("create the invoice and ship the item")
# else:
#     print("you cant but the item, work more")

light = "red"
if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "amber":
    print("GET READY")
#  will only print for red since that is our condition, others will not passed cos the condition isnt met

light = "green"
if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "amber":
    print("GET READY")
#  will only print for green since that is our condition, others will not passed cos the condition isnt met

light = "amber"
if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "amber":
    print("GET READY")
#  will only print for amber since that is our condition, others will not passed cos the condition isnt met

light = "blue"
if light == "red":
    print("STOP")
elif light == "green":
    print("GO")
elif light == "amber":
    print("GET READY")
else:
    print("you breached the traffic rule")
#  will only print for blue since all the conditions aren't met 