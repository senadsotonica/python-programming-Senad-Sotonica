wght = int                                                     
lgth = int                                                   
wdth = int
hght = int
ans = 'y'


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

# Yes this could have been solved with 
# if wght > 8 or length > 55 or width > 40 or height > 23: 
#   print("Not allowed")
# but where's the fun in that?


while ans == 'y':                                                                           # we enter the loop because the ans is set to 'y'
    ans = input("\nDo you want to check if your luggage is allowed? (y/n)")                 # we give the user to either initiate check the luggage or terminate
    if ans == 'n':                                                                          # if the user types n
        break                                                                               # it jumps out of whole loop and that's it
    else:
        while ans == 'y':                                                                   # if user types y another loop is initiated
            print("\nLet us see.")
            print("\nWhat is the weight of the luggage?")
            wght = get_num()                                                                # Getting input for weight
            if wght > 8:                                                                    # Checking weight
                print("I am so sorry, but it is a bit on the heavy side.")                  # If overweight print message                             
                break                                                                       # Exit inner loop
            print("What is the length of the luggage?")  
            lgth = get_num()                                                                # Getting input for length
            if lgth > 55:                                                                   # Checking length
                print("I am so sorry, it is too long . ")                                   # If oversized break inner loop
                break
            print("What is the width of the luggage?")
            wdth = get_num()                                                                # Getting input for width 
            if wdth > 40:                                                                   # Checking width
                print("I am so sorry, we have restrictions on width.")                      # If oversized break inner loop
                break
            print("What is the height of the luggage?")
            hght = get_num()                                                                # Getting input for height
            if hght > 23:                                                                   # Checking height
                print("I am so sorry, you almost made it, but no, not with that height.")   # If oversized break inner loop
                break
            print("\nWell done! The luggage is allowed.")                                   # If no breaks were activated
            print("\nNext please!")                                                         # The luggage is allowed, repeat the inner loop
    
    if ans != 'y' and ans != 'n':                                                           # if the user types something else than y or n
        print("\nSorry, what was that? Type y or n . Let's try it once more, sha'll we?")   # Ask wtf?
        ans = 'y'                                                                           # Reset ans to 'y' so the loop repeats
 