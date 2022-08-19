# to exlpain the variables concept

items_count = 100
# a variable called items_count was declared and assigned a value 100
# print(id (items_count)) 
# line 5 will print the location the variable is stored on our computer and the RAM 
customer_name = 'vamsi'
is_bill_paid = False
unit_price = 15.05
# declaring variables and assigning values on lines 3 - 6

# print('items_count: ', items_count, 'type of items_count: ',
#       type(items_count), 'memory loction: ', id(items_count))
# print('customer_name: ', customer_name, 'type of customer_name: ',
#       type(customer_name), 'memory loction: ', id(customer_name))
# print('is_bill_paid: ', is_bill_paid, 'type of is_bill_paid: ',
#       type(is_bill_paid), 'memory loction: ', id(is_bill_paid))
# print('unit_price: ', unit_price, 'type of price: ', type(
#     unit_price), 'memory loction: ', id(unit_price))

total = items_count * unit_price

discount = 50

total_after_discount = total - discount

total_before_discount = items_count * unit_price

print('total bill to be paid: ', items_count * unit_price)

# since total is used a variable on line 21, you dont need to call total as on line 23, replace (items_count * unit_price) with total instead
print('total bill to be paid: ', total)

# since you gave a discount variable on line 23, you can call the discount with total below
print('total bill to be paid: ', total-discount)

# since you declared a variable for total_after_discount on line 25, you can call it below
print('total_after_discount: ', total - discount)

print("total_before_discount: ", items_count * unit_price)

print("items_count:", items_count)
