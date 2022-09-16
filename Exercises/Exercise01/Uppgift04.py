wgt = float
age = float


def get_num():                                                                      # same function as in 02
                                                                                                                                                              # 
    isnum = False                                                                   # a boolean trigger set to false
    while not isnum:                                                                # as long as isnum is false
        inmat = input("Please, enter a number : ")                                  # it will keep asking for a numeric input
        if inmat.isnumeric():                                                       # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True
        else:                                                                       # else the user is made aware of the mistake, and the loop runs again
            print("That's not a number")  
    return float(inmat)                                                             # when the function is done it returns users numerical input 
                                                                                    # in float format

print("\nWhat is the patients age?")
age = get_num()
print("What is the patients weight?")
wgt = get_num()                                                                     # getting input by calling get_num()                                                                                         


 
print("The recommended number of pills for the patient is :")
if age > 12:                                                                        # checking wich category patient belongs to
    print(" 1 - 2 pills ")                                                          # children older than 12 years and adults
elif wgt >= 26 and wgt <= 40:                                                                                            
    print(" 1/2 - 1 pill ")                                                         # children 12 years and younger
elif wgt >= 15 and wgt <= 25:                                                       # weight 26 - 40 kg                                         
    print(" 1/2 pill ")                                                             # or weight 15 - 25 kg
else:
    print("hum... wait... this can't be right... something is very odd...\n")       # if none above, call the doctor
    print("May I suggest asking the doctor ?\n")
