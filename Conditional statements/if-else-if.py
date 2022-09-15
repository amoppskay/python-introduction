# if --> to handle single case
# if-else --> to handle two cases
# if-else-if --> to handle more than two cases

"""
syntax:

if (condition):
    statement
elif (condition):
    statement
elif (condition):
    statement
.
.
else:
    statement
"""
# if-else-if example
print('\n #if-else-if example')
marks = int(input("What is your exam score? ")) #input is for type conversion
print(marks, type(marks))
grade = None
# you have to fill in your grade manually, your grade determines your score below & what is printed
if marks >= 85 and marks <= 100:
    print('You got an A! Congrats!')
    grade = 'A'
elif marks >= 75 and marks < 85:
    print('You got a B! Well done!')
    grade = 'B'
elif marks >= 50 and marks < 75:
    print('You got a C. Not great, not terrible.')
    grade = 'C'
elif marks >= 40 and marks < 50:
    print('You got a D. But you can do better!')
    grade = 'D'
else:
    print("You did not pass the exam. Contact the teacher for more information.")
    grade = 'Fail'

print("Fill grade : {} in the sheet".format(grade))
print("Fill grade : ", grade, "in the sheet")
# this will print whatever the score is to replace the {}, returns values like "Fill grade A/B/C etc in the sheet"

print("Fill grade : {}, marks: {} in the sheet".format(grade, marks)) # adding marks to the code

