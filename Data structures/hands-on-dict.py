# for data that need properties with key:value,
phone_type = {"name": "lg", "price": 1000, "storage": 256, "camera": 64} 

print(phone_type)
print(type(phone_type))

print(phone_type["price"]) #prints value of price
print(phone_type["camera"]) #prints value of camera

# phone_type["camera"] = 128 # changes the value of camera from 64 to 128
# print(phone_type)

phone_type["model"] = "s-2022" # adds model to the dict
print(phone_type)

print(dir(phone_type)) # fxns such as copy, get, items, keys, values etc

new_phone_type = phone_type.copy() #copies items from phone_type to a new variable "new_phone_type"
print(new_phone_type)

print(phone_type.keys()) # prints list of keys in the dict list
print(phone_type.values()) # prints list of values in the dict list
print(phone_type.items()) # prints keys and values on the dict list

mobile_phones = [{"name": "lg", "price": 900, "storage": 256, "camera": 32}, {"name": "samsung", "price": 1200, "storage": 256, "camera": 64},
{"name": "iphone", "price": 1100, "storage": 256, "camera": 64}, {"name": "itel", "price": 600, "storage": 256, "camera": 16}]
#  this will return the list of keys/values on the dict 
print(mobile_phones)