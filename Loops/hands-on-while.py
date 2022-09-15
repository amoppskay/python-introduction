#  while is used when you dont have sequence of items but you have a condition

i = 1

while i<5:
    print(i) #infinite loop cos 1 is always < than 5, it will keep on printing
    i = i + 1 #stops printing on 4 cos on 5 it becomes false, will only keep looping when true

cars_coming = True

while cars_coming == True:
    print("keep the gate opened") #keeps on looping, infinite loop
    cars_coming = False #use this to break/stop the infinite loop

