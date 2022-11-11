import requests

API_HOST = "https://reqres.in"  # get the domain name from regres.in and amke the common name a variable = API_HOST


# user_id = str(input("Please enter user id "))

def get_user_id(user_id):  # defined a fxn = get_user_id
    print(f"Getting details of user {user_id}")
    response = requests.get(API_HOST + "/api/users/" + str(user_id))
    print(f"response code is {response}")
    # return response.json()
    print(response.json())

print(get_user_id())

def update_user_details(user_id, user_data):
    print(f"Performing update on user_id {user_id}")
    response = requests.put(API_HOST + "/api/users/" + str(user_id), user_data)
    print(f"response code is {response}")
    return response.json()

# users_id = 3
#
# users_data = {"name": "titi", "job": "developer"}
#
# print(update_user_details(users_id, users_data))




# {"name": "morpheus", "job": "zion resident"}
