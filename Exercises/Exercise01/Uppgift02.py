
                                                                                           

tal1 = float
tal2 = float

def get_num():                                                                                              # using the very same while loop from 01
                                                                                                            # but now it's inside a function that I can call
                                                                                                            # whenever I need it
    isnum = False                                                                                           # a boolean trigger set to false
    while not isnum:                                                                                        # as long as isnum is false
        inmat = input("Please, enter a number:")                                                            # it will keep asking for a numeric input
        if inmat.isnumeric():                                                                               # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True
        else:                                                                                               # else the user is made aware of the mistake, and the loop runs again
            print("That's not a number")  
    return float(inmat)                                                                                     # when the function is done it returns users numerical input 
                                                                                                            # in float format


tal1 = get_num()                                                                                            # getting input by calling get_num()
tal2 = get_num()                                                                                    

if tal1 > tal2:                                                                                             # checking if the first number is bigger
    print("The first number is bigger.")
elif tal2 > tal1:                                                                                           # checking if the second number is bigger
    print("The second number is bigger.")
else:
    print("The numbers are equal.")                                                                         # if it is neither they are equal

