#Function to find prime factors of a number

def prime_factors(x):
    number =2
    arr = list()
    while (number <= x):
        if (x % number) == 0:      #Checks if remainder is 0
            arr.append(number)     #if remainder is 0, appends the number in the list 
            x = x/number           #Then keep dividing 
        else:
            number+=1              #else increment the number to see next number 

    return print(arr)               

prime_factors(630)