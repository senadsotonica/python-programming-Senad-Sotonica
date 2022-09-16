vi1 = float
vi2 = float
vi3 = float
istri = False


def get_num():                                                                                              # same function as in 02
                                                                                                            # 
    i = 1                                                                                                   # 
    isnum = False                                                                                           # a boolean trigger set to false
    while not isnum:                                                                                        # as long as isnum is false
        inmat = input("Please, enter an angle :")                                                           # it will keep asking for a numeric input
        if inmat.isnumeric():                                                                               # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True
        else:                                                                                               # else the user is made aware of the mistake, and the loop runs again
            print("That's not a number")  
    return float(inmat)                                                                                     # when the function is done it returns users numerical input 
                                                                                                            # in float format

while not istri:
    vi1 = get_num()                                                                                         # getting input by calling get_num()
    vi2 = get_num()                                                                                         
    vi3 = get_num()
    if (vi1+vi2+vi3) == 180:                                                                                # if a valid triangle
        istri = True                                                                                        # the loop will stop
    else:                                                                                                   # else it will repeat
        print("Something is wrong.\nThe angles of a triangle should add up to 180 degrees.\n")

if vi1 == 90:                                                                                               # checking wich angle is a right angle
    print("The first angle is a right angle")
elif vi2 == 90:                                                                                            
    print("The second angle is a right angle")
elif vi3 == 90:                                                                                             
    print("The third angle is a right angle")
else:
    print("There are no right angles in the triangle.")                                                     # if none there are no right angles in this triangle

