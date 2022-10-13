# So this was an exercise where
# a while statetment would add upp 
# all numbers, 1 to 100
# and
# all odd numbers 1 to 99
# I added an option where user decides range and increment 
# just fo fun of it

#[      --- menu ---        ]#                                                                # in int format
def menu():
    print("\n         ...:::'[ Menu ]':::...\n")
    print("1  - add up all numbers, 1 to 100")
    print("2  - add up all odd numbers, 1 to 99")  
    print("3  - quit")
    print("\nWhat will it be? ")


#[      --- getNum ---        ]# 
def getNum():                                           # same function as in 02
                                                                
    isnum = False                                       # a boolean trigger set to false
    while not isnum:                                    # as long as isnum is false
        inmat = input("Please, enter a number : ")      # it will keep asking for a numeric input
        if int(inmat):                                  # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True

    return int(inmat)                                   # when the function is done it returns users numerical input 


#[      --- count ---        ]#
def count(start, end, incr):
    sum = 0
    list = []
    while start <= end:                                 # less or equal, so we count the last round too
        sum = sum + start
        start = start + incr
        
    
    print("\nCounting ...")
    print(sum)



#[      --- main ---        ]#

start   =  int                              
end     =  int                              
incr    =  int                              

quit = False
while not quit:                                         # as long as user doesn't choose to quit 
    
    option = False
    while not option:                                   # while user doesn't choose a valid option 
        
        menu()
        choice = getNum()
        if  (0 < choice < 4) :                          # if user chose 1, 2, 3 or 4
            option = True                               # choice is valid
            if choice == 1:                             # user wants preset values
                start   =   1                           # start at -10
                end     = 100                           # count to 10
                incr    =   1                           # increment 1

            if choice == 2:                             # preset values 
                start   =   1                           # start at -10
                end     =  99                           # count to 10
                incr    =   2                           # incerement 2

            if choice == 3:                             # user quits
                quit = True
                


    if not quit:
        count(start, end, incr)                         # count with the parameters start, end, increment