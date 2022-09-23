import matplotlib.pyplot as plt
import math


poke ={                                             # dictionary  pokemon
    "width"     :   0.0,                            # width
    "length"    :   0.0,                            # length
    "class"     :   0,                              # class
    "distance"  :   0.0                             # distance
}                                                   

def get_num():                                      # function for getting a numerical input                                      
                                                                
    isnum = False                                   # a boolean trigger set to false
    while not isnum:                                # as long as isnum is false
        inmat = input("Please, enter a number : ")  # it will keep asking for a numeric input
        if float(inmat):                       # if the input is numeric, isnum is set to true, stopping the loop
            isnum = True
        else:                                       # else the user is made aware of the mistake, and the loop runs again
            print("That's not a number")  
    return float(inmat)                             # when the function is done it returns users numerical input 
                                                    # in float format
                                                    

def visa(x1, y1, x2, y2, txt1, txt2):               # plotting x1,y1 and x2,y2 with labels txt1 and txt2
    
    plt.plot(x1, y1, 'ro')                          # plot all pichu X,Ys with red dots
    plt.plot(x2, y2, 'bo')                          # plot all pikachu X,Ys with blue dots
    plt.xlabel(txt1)
    plt.ylabel(txt2)
    plt.show() 
    

def sortByDist(list, x, y):
    
    for p in list:                                  # for each element in list
                                                    # calculate distance from point x,y to current elements x,y that is width and length
        p["distance"] = math.dist([x, y], [p["width"], p["length"]])
                                                       
    newlist = sorted(pokList, key=lambda d: d["distance"])
    return newlist                                  # return the a list with the elements sorted by distance


def whichIsIt(list):
    pichuVote = 0
    pikachuVote = 0
    for i in range(10):                             # for 0 to 10
        if list[i]["class"] == 0:                   # check each elements class
            pichuVote = pichuVote + 1
        else:                                       # and count votes
            pikachuVote = pikachuVote + 1

    if pichuVote > pikachuVote:                     # if pichu is in majority return true
        return True
    else:                                           # else return false
        return False
        

def listFromFile(filename):
    list = []
    with open(filename, 'r') as reader:                 # Read and print the entire file line by line "datapoints.txt"
        line = reader.readline()                        # The first line we read is not of interest
        line = reader.readline()                        # The second line is the first pokemon
                                                        # if that line is empty, the file is empty, 
                                                        # we don't go into the loop
        while line != '':                               # The EOF char is an empty string
            text = line.split(", ")                     # split upp string at and removing ', ' 
            poke[ "width"  ] = float(text[0])           # and put the parts in a list of 3 strings
            poke[ "length" ] = float(text[1])           # putting each part in the corresponding 
            poke[ "class"  ] =   int(text[2])           # part of dictionary
            
            list.append(poke.copy())                    # put the pokemon into the pokeList
                                                        # and yeah, you have to use copy
                
            line = reader.readline()

    return list



# Main -------------------------------------------------------------------------------------------

pokList = listFromFile("datapoints.txt")
                                                                                          

print("Enter weight and length of your pokemon.")
print("width please:")
width = get_num()                                   # get width from user
print("Length please:")
length = get_num()                                  # get length from user

distList = sortByDist(pokList, width, length)       # sort pokemons by distance from the users pokemon width,length point 


if whichIsIt(distList):                             # check the 10 closest, to decide by majority wich class the pokemon is
    print("It's a pichu!")                          # if equal vote the function will return false value
else:
    print("It's a pikachu!")                        # so it's slightly biased towards pikachu

