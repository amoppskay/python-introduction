import util
# print("hiii")
# print("bye")
# print("amoppskay")

# def greetings ():
#     print("welcome to the team") #other lines got printed but this line; you need to call the fxn def to print; see next line
# greetings()

# # to make it dynamic by adding other values to "welcome to the team", you need to add the parameter eg "name" which keeps changing
# def greetings (name):
#     print("welcome to the team", name)
# greetings("titi") # adds titi to the greeting msg
# greetings("osh") adds osh to the greeting msg
# greetings("mercy") adds mercy to the greeting msg

def check_balance(account_number):
    util.get_db_credentials_param("db-secret")
    print("connecting to user account in the DB", account_number)
    print("checking balance for account number", account_number)
    print("current balance is 1000")
    return 1000 # it must end with return to return the balance
#  checkbal fxn is only declared once but can be used for other fxns that requires it as in the
#  examples below

check_balance(1200333) # uses this acct# in each of the print fxn above 
# check_balance(1903456) # uses this acct# in each of the print fxn above
# check_balance(2319374) # uses this acct# in each of the print fxn above

def send_money(senders_acct_no, receivers_acct_no, amount): #to send money we need to check bal
# so we call another fxn but it will need the check_bal fxn so it will grab it from checkbal above
     check_balance(senders_acct_no)
     current_bal = check_balance(senders_acct_no)
     print(current_bal)

def send_money(senders_acct_no, receivers_acct_no, amount):
    current_bal = check_balance(senders_acct_no)
    if current_bal >= amount:
        print("sending the amount", amount, "to bank account", receivers_acct_no)
    else:
        print("insufficient funds")

# send_money(12345, 23456, 300)
# returns sending 300 from acct# 12345 to acct# 23456, but it will checkbal using acct# to 
#  carry out the fxn

def calculate_interest(account_number):
    current_bal = check_balance(account_number)
    current_bal = current_bal + 10
    print("final bal after interest", current_bal)

calculate_interest(12345)
#  it will add the interest to the currentbal after using the info in the checkbal which reqiures
# acct#

# we can fxns that is in other files, we can import the file... refer to line 1