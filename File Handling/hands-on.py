# file_path = 'C:\\Users\\amopp\OneDrive\\Desktop\\python-introduction\\File Handling\\sample.txt'

# import os #imports os from python module

# data = open(file_path, "r")
# # print(data.read()) 
# # print(data.read(8)) # reads only 1st 8 xters
# # print(data.readline(3)) #reads onlly line 3

# for i in data:
#     print(i) # iterating over each line in order

# data = open(file_path, "w")
# data.write("vamsi is a good teacher \n")
# data.write("he teaches us python well \n")
# data.close()

# data = open(file_path, "a")
# data.write("sorry for the confusion \n")
# data.write("I promise this wont occur again ")
# data.close() # close is to save and close the file

# data = open(file_path, "x") # x is to create a file
# data.close()

# os.remove(file_path) # we imported os in line 3 above, we use this to remove the file we created. To use remove fxn we need to import os
# cos there's no direct fxn to remove an existing file so we need to import os

# file_data = open("movies.txt", "x")# 'x' is for create a file

# print(type(file_data))
# print(dir(file_data))

# file_data = open("movies.txt", "w") #write mode to write in the file movies.txt
# file_data = open("movies.txt", "a") # append more lines
file_data = open("movies.txt", "r")
# file_data.write("Today is Friday\n")
# file_data.write("People arent in class\n")
# file_data.write("Class is very scanty\n")
# file_data.write("Vamsi is doing a good job here\n")
# file_data.write("Tommorow is Saturday\n")
# file_data.write("There's no class tomorrow\n")

print(file_data.readline())
print(file_data.read(6))
print(file_data.readlines()) # puts all of the texts in a list with 'readlines'
file_data.close()


