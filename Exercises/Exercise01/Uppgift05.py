num = int                                                     
odd = False                                                     
div = False

def get_num():                                                  # same function as in 02
                                                                
    isnum = False                                               # a boolean trigger set to false
    while not isnum:                                            # as long as isnum is false
        inmat = input("Please, enter a number : ")              # it will keep asking for a numeric input
        if inmat.isnumeric():                                   # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True
        else:                                                   # else the user is made aware of the mistake, and the loop runs again
            print("That's not a number")  
    return int(inmat)                                           # when the function is done it returns users numerical input 
                                                                # in int format


num = get_num()                                                 # getting input by calling get_num() 
                                                                                                                                                        
if (num % 2)  == 0:                                             # is the number even
    print("The number", num, "is even")                         
else:                                                           # if not it is odd
    print("The number", num, "is odd")                          # set the odd flag to true
    odd = True

if (num % 5) == 0:                                              # is the number divisible by 5
    print("The number", num, "is divisible by 5 .")             # set the div flag to true
    div = True
else:                                                           # if not divisible by 5
    print("The number", num, "is not divisible by 5 .")

if odd and div:                                                 # activated only if both odd an div have been set to true
    print("The number", num, "is odd and divisible by 5 .")     # (they are set to false from start)
                                                                # if the number is both odd and divisible by 5