"""
Python Functions is a block of related statements designed to perform a computational, logical, or evaluative task.
The idea is to put some commonly or repeatedly done tasks together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.
"""

"""
Syntax:
def function_name(parameters):
    statement
    return expression
"""

# dependencies
import util


print("\n#Simple Python function")


def hello():
    print("Hello, welcome to JJtech Python class!")
#calling the hello fxn with def as the keyword. Anytime  we call hello, it will be a fxn with () once it is called, it can be called multiple times
hello()
hello()



# # Calling the existing function
print("\n# Calling the existing function")
hello()


# # Function with arguments
# # A simple Python function to check whether x is even or odd
# # Here the x --> the data that is being passed to the 
# function is called arguments
print("\n# Function with arguments")
def check_number(number): #fxn is check_number with a variable (number), just call check_number anywhere and it will 
# print based on the conditions passed
    if number > 0:
        print("positive number")
    elif number < 0:
        print("negative number")
    else:
        print("neither positive nor negative number")

check_number(10)
check_number(-2)
check_number(0)
check_number(4)

# # # Code to call the function
def check_all_numbers():
    check_number(-2)
    check_number(3)
    check_number(0)


# check_all_numbers()


# # when you dont have functions
height=160
weight=56
bmi = ((weight/height)/height)*1000
print(bmi)

def calculate_bmi (height, weight):
    bmi = ((weight/height)/ height)*1000
    print(bmi)

calculate_bmi(157,53)
calculate_bmi(160,56)

print(calculate_bmi(172, 65))


print("\n# Function calculate BMI with height and weight")
def calculate_bmi(height, weight):
    bmi = ((weight/height)/height)*1000
    print(bmi)

calculate_bmi(157, 53)
calculate_bmi(160, 56)

# # # return statement
print("\n# return statement")
def sum_of_numbers(a,b):
    c = a + b
    print(c)
    return c
final_result = sum_of_numbers(10,15) #when you add a=10 b=15 return c=25 
print(final_result*4) # final_result = c = 25 multiply by 4
print(sum_of_numbers(10,15)*4) #here fxn sum_of_numbers which is 10+15 multiply by 4



# # # call the functions even from other files
# # # https://www.w3schools.com/python/ref_string_format.asp
print("\n# call the functions even from other files")
def store_invoice_details(name, price, invoice_id):
    print("Storing invoice details of the customer; {}, price: {}, invoice_id: {}".format(name, price, invoice_id))
    db_credentials = util.get_db_credentials_param(name='abcd') #calling db_credentials from util.py
    print("Got DB credentials secret {}".format(db_credentials))
    print("Establising db connection....")
    print("Storing the details into DB...")
    print("Successfully stored invoice details in the DB!")
    return True

result = store_invoice_details(name="Vamsi", price="$150", invoice_id="invoice-12345")
if result == True:
    print("You invoice details are stored successfully")
else:
    print("there was some error while we are trying to store your invoice details")