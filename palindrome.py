def Palindrome(x):
    string = x.lower()                  #Converts the string to lowercase
    arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']    
    new_list = list()
    for letter in string:               #This for loop is just to include alphabets and avoid any other character or spaces
        if letter in arr:
            new_list.append(letter)
            
    length = len(new_list)              
    findex = 0
    lindex = length-1
    while findex < length/2:            #While loops run till the middle of the string
        first = new_list[findex]        #Puts the first letter in the this variable
        last = new_list[lindex]         #Puts the last letter in the this variable
        if first == last:               #Checks if first and last letter matches
            findex+=1                   
            lindex-=1
        else:
            print('Not a palindrome')
            break
    else:
        print("Is a palindrome")    

    
Palindrome("aB-Cd c'ba")
Palindrome("level")
Palindrome("hello world")