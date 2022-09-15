name = "titi amps"

print(dir(name)) #all possible fxns
print(name.upper()) # prints in upper case letters
print(len(name.upper())) #length of name in upper case letters
print(name.strip()) #
print(len(name.strip()))
# print(name.replace("i", "@")) #replaces i with @ anywhere i is mentioned

mail = "titi.amps@lg.com"
print(mail.split(".")) # splits anywhere . is
print(name.split(" ")) # splits anywhere space is on the name
print(mail.split("@")) # splits anywhere @ is, so it splits into 2

temp = mail.split("@")
print(temp [1])

temp2 = temp[1].split(".")
print(temp2[0])
