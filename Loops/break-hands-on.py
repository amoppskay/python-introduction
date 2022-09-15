items = ["eggs", "bread", "milk", "cheese", "mango"]

for each_item in items:
    if each_item == "cheese": # passes over cheese
        continue # continue will pass over the item cheese and continue with other item
    print(each_item, "put in my basket") # wont put cheese in the basket

# #if our loop searches for what it wants, we dont need it to go further, then we break
# for each_item in items:
#     if each_item == "milk":
#         print("found", each_item)
#         break # this will help it to stop on milk when it iterates over it, it wont continue iterating over cheese and mango
#     else:
#         print("still looking for milk", each_item)

# docs = ["passport",  "rtpcr-+ve", "visa", "boarding pass"]

# for doc in docs:
#     print(doc)
#     if "rtpcr" in doc and "+ve" in doc:
#         break
#     else:
#         print("collect document: ", doc)

# passengers = ["valid", "valid", "not valid", "valid"]

# for v in passengers:
#     if v == "not valid":
#         continue
#     print(v) #only when passengers doc is "not valid", continue so it wont print it but goes on to the next iterations

# for v in [1,2,3,4,5]:
#     if v == 3: #this will skip number 3 and still continue to the end
#         continue
#     print(v)

numbers = [1,2,3,4,5]

for n in numbers:
    pass #pass is just to move on and do nothing, place hold on, move on to the next line

print("hi") #prints on hi and nothing on the numbers list