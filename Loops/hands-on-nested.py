# nested lists of students, the list of students are 3 and put 2geda in a list [[,,,]]
students = [ [1,2,3,4], [5,6,7,8], [9,10,11,12,13] ]

for i in students:
    # print(i) # iterates over each index of list
    for j in i:
        print(j)
        print('*', end=' ')
