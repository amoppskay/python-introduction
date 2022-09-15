# emails = ["vamsi@jjtech.com", "titi@amazon.com", "osh@tcs.com", "priye@acxiom.com"]
# comapnies = set()

# for email in emails:
#     print(email)

#     print(email.split("@"))

#     print(email.split("@")[1])

#     print(email.split("@")[1].split(".")[0])

emails = ["vamsi@jjtech.com", "titi@amazon.com", "osh@tcs.com", "priye@acxiom.com"]
comapnies = set()

for email in emails:
    # print(email)
    comapnies.add(email.split("@")[1].split(".")[0])
print(comapnies)