import matplotlib.pyplot as plt

pokList = []                                        # list of myPok
pchuX   = []                                        # list of pichu Xs
pchuY   = []                                        # list of pichu Ys
pkachX  = []                                        # list pikachu Xs
pkachY  = []                                        # list pikachu Ys


myPok ={                                            # dictionary of pokemon
    "wdth":   21.95,                                # width
    "lgth":   31.23,                                # length
    "clss":    1                                    # class
}


with open("lek.txt", 'r') as reader:                # Read and print the entire file line by line
    line = reader.readline()                        # The first line we read is not of interest
    line = reader.readline()                        # The second line is the first line of interest
                                                    # if that line is empty, the file is empty, 
                                                    # we don't go into the loop
    while line != '':                               # The EOF char is an empty string
        text = line.split(", ")                     # split upp string at and removing ', ' 
        myPok[ "wdth" ] = float(text[0])            # and put the parts in a list of 3 strings
        myPok[ "lgth" ] = float(text[1])            # putting each part in the corresponding 
        myPok[ "clss" ] =   int(text[2])            # part of dictionary
        
        pokList.append(myPok.copy())                # put the pokemon into the pokeList
                                                    # and yeah, you have to use copy
        line = reader.readline()                    # # read in next line from file, before repeating 
                                                   
                                                    

for pok in pokList:                                 # work through pokemon list
    if pok[ "clss" ] == 0:                          # if a pichu
        pchuX.append(pok[ "wdth" ])                 # put width in pichuX list
        pchuY.append(pok[ "lgth" ])                 # put length in pichuY list
    else:                                           # else it's a pikachu
        pkachX.append(pok[ "wdth" ])                # put width in pikachuX list
        pkachY.append(pok[ "lgth" ])                # put length in pikachuY list


plt.xlabel("weight")
plt.ylabel("height")
plt.plot(pchuX, pchuY, 'bo')                              # plot pichu line default blue
plt.plot(pkachX, pkachY, 'ro')                       # plot pikachu line in red
plt.show()                                          # show
        




