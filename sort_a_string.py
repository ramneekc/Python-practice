def sort_a_string(string):
    arr = string.split()                              
    new_arr = list()
    for x in arr:
        new_arr.append(x.lower() + x)               #Turns the string to lowercase and appends it to the front

    templist = sorted(new_arr)                      #Sorts the list with lower case letters being in the front
    newlist = list()
    for x in templist:
        y = x[len(x)//2:]                           #Keeps the second part(which is original) of the appended words
        newlist.append(y)
    print(newlist)

sort_a_string("Orange banana Apple Blueberries raspberries")