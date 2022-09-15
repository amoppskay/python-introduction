# A nested loop is a loop inside the body of the outer loop.
print("\n#nested loops --> exmple - 1")
# outer loop
for i in range(0, 6): #outer interation
    # nested loop
    # to iterate from 1 to 5
    for j in range(0, 5): #inside iteration; 
        # print multiplication
        # default end \n was replaced with a space here to stay at the same line
        print('*', end=' ') #sart with index of the outside multply by inside iteration will finish 1st b4 the outer index starts again
        # for every i iteration, j  will run its entire range
    print()  # use debugger to explain; it helps to begin with a new line

# print("\n#nested loops --> exmple - 2")
# # # outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        # default end \n was replaced with a space here to stay at the same line
        print(i*j, end=' ')
    print()  # use debugger to explain; it helps to begin a new line
    
