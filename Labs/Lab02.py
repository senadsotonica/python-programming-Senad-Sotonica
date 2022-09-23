import matplotlib.pyplot as plt
import numpy as np
import math

pokList = []                                        # list of myPok
pchuX   = []                                        # list of pichu Xs
pchuY   = []                                        # list of pichu Ys
pkachX  = []                                        # list pikachu Xs
pkachY  = []                                        # list pikachu Ys


myPok ={                                            # dictionary of pokemon
    "wdth" :   0.0,                                 # width
    "lgth" :   0.0,                                 # length
    "clss" :   0,                                   # class
}                                                   



with open("datapoints.txt", 'r') as reader:                # Read and print the entire file line by line
    line = reader.readline()                        # The first line we read is not of interest
    line = reader.readline()                        # The second line is the first line of interest
                                                    # if that line is empty, the file is empty, 
                                                    # we don't go into the loop
    while line != '':                               # The EOF char is an empty string
        text = line.split(", ")                     # split upp string at and removing ', ' 
        myPok[ "wdth"  ] = float(text[0])            # and put the parts in a list of 3 strings
        myPok[ "lgth"  ] = float(text[1])            # putting each part in the corresponding 
        myPok[ "clss"  ] =   int(text[2])            # part of dictionary
        
        pokList.append(myPok.copy())                # put the pokemon into the pokeList
                                                    # and yeah, you have to use copy
        if myPok[ "clss" ] == 0:
            pchuX.append(myPok[ "wdth" ])
            pchuY.append(myPok[ "lgth" ])
        else:
            pkachX.append(myPok[ "wdth" ])
            pkachY.append(myPok[ "lgth" ])

        line = reader.readline()                    # # read in next line from file, before repeating 

vctrPok =  np.array(pokList)      
# print(vctrPok)                                          
# pokList = sorted(pokList, key=lambda k: (k["wdth"], k["lgth"]))                                                   

#for pok in pokList:                                 # work through pokemon list
#    if pok[ "clss" ] == 0:                          # if a pichu
#                                                    # plot pichu with blue at point width, length
#        plt.plot((pok["wdth"]), (pok["lgth"]), 'bo')
#    else:                                           # else it's a pikachu
#                                                    # plot pikachu with red at point width, length
#        plt.plot((pok["wdth"]), (pok["lgth"]), 'ro')
    #print(pok["wdth"], pok["lgth"], pok["clss"])

#plt.show()                                          # show graph

#with open("testpoints.txt", 'r') as reader:         # open testpoints
#    line = reader.readline()                        # first line is of no interest
#    line = reader.readline()                        # read in point

#    while line != '':
#        print(line)
#        text = line.split()                         # spliting the line, I only need 2nd and 3rd bit

        # I borrowed and modified this bit of magic, cleans the strings from non alphanumerical chars except '.'
 #       myPok["wdth"] = float(''.join(letter for letter in text[1] if (letter.isalnum() or letter == '.')))  # weight in float 
 #       myPok["lgth"] = float(''.join(letter for letter in text[2] if (letter.isalnum() or letter == '.')))  # length in float
        # https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/ 

        

# iterate pokList in search of closest point
#         remember the closest
# if closest pichu
#   then testpoint pichu
# else:
#   testpoint pikachu 
# print(min(points, key=lambda point: math.hypot(target[1]-point[1], target[0]-point[0])))
# 
                                                     



