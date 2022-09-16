
isnum = False                                                                                           # a boolean trigger set to false
inmat = ""

while not isnum:                                                                                        # as long as isnum is false
    inmat = input("Please, enter a number:")                                                            # it will keep asking for a numeric input
    if inmat.isnumeric():                                                                               # if the input is numeric, isnum is set to true stopping the loop
        isnum = True
    else:
        print("That's not a number")                                                                    # else the user is made aware of the mistake, and the loop runs again

num = float(inmat)                                                                                      # since inmat is numeric it is safe to convert it to a float type

if num > 0:                                                                                             # if it is a positive number it is bigger than 0
    print("The number is positive.")
elif num < 0:                                                                                           # if it is a negative number it is lesser than 0
    print("The number is negative.")
else:
    print("The number is a neither.\nIt's nothing, and that is something.\nIt's a zero.")               # if it is neither it can only be zero

