import matplotlib.pyplot as plt
import math

pokList = [] # list of pokemons    
pchuX   = [] # list of pichus X
pchuY   = [] # list of pichus Y
pkachX  = [] # list of pikachus X
pkachY  = [] # list of pikachus Y

poke ={                                             # dictionary  pokemon
    "width"  :   0.0,                               # width
    "length" :   0.0,                               # length
    "class"  :   0                                  # class
}                                                   


                                                    

def visa(x1, y1, x2, y2, txt1, txt2):               # plotting x1,y1 and x2,y2 with labels txt1 and txt2
    
    plt.plot(x1, y1, 'ro')                          # plot all pichu X,Ys with red dots
    plt.plot(x2, y2, 'bo')                          # plot all pikachu X,Ys with blue dots
    plt.xlabel(txt1)
    plt.ylabel(txt2)
    plt.show() 



def whichClass(list, poke):
    
    first = True                                    # first run in for loop set true
    for p in list:                                  # run through elements in list
                                                    # calculate distance from pokemon to current element p in list
            distance = math.dist([poke["width"], poke["length"]], [p["width"], p["length"]])
            
            if  first or distance < shortest:       # if first distance or distance is shorter than shortest
                shortest = distance                 # set shorter to distance
                if p["class"] == 0:                 # set text in pClass to appropriate class
                    text = "Pichu" 
                else: 
                    text = "Pikachu"
                first = False                       # set first to false when first element in list is checked
                
    return text                                     # return text with the appopriate class



# Main -------------------------------------------------------------------------------------------

with open("datapoints.txt", 'r') as reader:         # Read and print the entire file line by line
    line = reader.readline()                        # The first line we read is not of interest
    line = reader.readline()                        # The second line is the first pokemon
                                                    # if that line is empty, the file is empty, 
                                                    # we don't go into the loop
    while line != '':                               # The EOF char is an empty string
        text = line.split(", ")                     # split upp string at and removing ', ' 
        poke[ "width"  ] = float(text[0])           # and put the parts in a list of 3 strings
        poke[ "length" ] = float(text[1])           # putting each part in the corresponding 
        poke[ "class"  ] =   int(text[2])           # part of dictionary
        
        pokList.append(poke.copy())                 # put the pokemon into the pokeList
                                                    # and yeah, you have to use copy
        if poke["class"] == 0:                      # if pokemon class is 0 that is Pichu
            pchuX.append(poke["width"])             # put width in pchuX list
            pchuY.append(poke["length"])            # put length in pchuY list
        else:                                       # else it's a Pikachu
            pkachX.append(poke["width"])            # put width in pkachX list
            pkachY.append(poke["length"])           # put length in pkachY list
            
        line = reader.readline()                    # read in next line from file, before repeating 

visa(pchuX, pchuY, pkachX, pkachY, "width", "length")
                                                    # calling visa to plot all pokemons in their respective class
                                                                                          
with open("testpoints.txt", 'r') as reader:         # open testpoints file
    line = reader.readline()                        # first line is of no interest
    line = reader.readline()                        # read in first pokemon

    while line != '':
        
        text = line.split()                         # spliting the line, I only need 2nd and 3rd bit

        # I borrowed and modified this bit of magic, cleans the strings from non alphanumerical chars except '.'
        poke["width"] = float(''.join(letter for letter in text[1] if (letter.isalnum() or letter == '.')))  # weight in float 
        poke["length"] = float(''.join(letter for letter in text[2] if (letter.isalnum() or letter == '.')))  # length in float
        # https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/ 
        
        pokClass = whichClass(pokList, poke)
        
        print("Pokemon:", poke, " är en ", pokClass)# print current pokemon from testfile and which class it belongs to

        line = reader.readline()                    # read next line from file


