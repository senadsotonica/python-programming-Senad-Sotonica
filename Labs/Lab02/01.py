#from tarfile import PAX_FIELDS
import matplotlib.pyplot as plt
import random
import math


poke ={                                                     # dictionary  pokemon
    "width"     :   0.0,                                    # width
    "length"    :   0.0,                                    # length
    "class"     :   0,                                      # class
    "distance"  :   0.0                                     # distance
}                                                   

                                                    
#----- fromFile         -----   -----                   -----                  -----   -----                   
def fromFile(fname):                                        # creating a list of pokemons from file                                    
    list = []
    with open(fname, 'r') as reader:                        # read and print the entire file line by line      
        line = reader.readline()                            # the first line we read is not of interest
        line = reader.readline()                            # the second line is the first pokemon
                                                            # if that line is empty, the file is empty, 
                                                            # we don't go into the loop
        while line != '':                                   # the EOF char is an empty string
            if fname == "datapoints.txt":                   # if reading datapoints file   
                text = line.split(", ")                         # split upp string at and removing ', ' 
                poke[ "width"  ] = float(text[0])               # and put the parts in a list of 3 strings
                poke[ "length" ] = float(text[1])               # putting each part in the corresponding 
                poke[ "class"  ] =   int(text[2])               # part of dictionary
            
            if fname == "testpoints.txt":                   # if reading testpoints file
                text = line.split()                             # spliting the line, I only need 2nd and 3rd bit

                # I borrowed and modified this bit of magic, cleans the strings from non alphanumerical chars except '.'
                poke["width"] = float(''.join(letter for letter in text[1] if (letter.isalnum() or letter == '.')))  # weight in float 
                poke["length"] = float(''.join(letter for letter in text[2] if (letter.isalnum() or letter == '.'))) # length in float
                # https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/ 

            list.append(poke.copy())                        # put the pokemon into the pokeList
                                                            # and yeah, you have to use copy                         
            line = reader.readline()                        # read the next line before repeating the loop

    return list                                             # return list when finished


#----- shwPok           -----   -----                   -----                  -----   -----                   -----                  -----   -----                   
def shwPok(x1, y1, x2, y2, txt1, txt2):                     # plotting x1,y1 and x2,y2 with labels txt1 and txt2
    
    plt.plot(x1, y1, 'ro')                                  # plot all pichu X,Ys with red dots
    plt.plot(x2, y2, 'bo')                                  # plot all pikachu X,Ys with blue dots
    plt.xlabel(txt1)
    plt.ylabel(txt2)
    plt.show()                                              # show the graph


#----- getXY            -----   -----                   -----                  -----   -----                   -----                  -----   -----                   
def getXY(list):                                            # separete the X and Y by type
    paX = []                                                # list of pichus width      as X
    paY = []                                                # list of pichus length     as Y
    pbX = []                                                # list of pikachus width    as X
    pbY = []                                                # list of pikachus length   as Y

    for p in list:                                          # for every pokemon in list
        if p["class"] == 0:                                 # if pokemon class is 0 it is a Pichu
            paX.append(p["width"])                              # put width in paX list
            paY.append(p["length"])                             # put length in paY list
        else:                                               # else it's a Pikachu
            pbX.append(p["width"])                              # put width in pbX list
            pbY.append(p["length"])                             # put length in pbY list

    return paX, paY, pbX, pbY                               # return all lists of width and length


#----- whichClass       -----   -----                   -----                  -----   -----                   -----                  -----   -----                   
def whichClass(p, list):                                    # check which class p is compared to the list
    
    first = True                                            # first run in for loop set to true
    for i in list:                                          # run through elements i in list
                                                            # calculate distance from pokemon p to current element i in list
            distance = math.dist([p["width"], p["length"]], [i["width"], i["length"]])
            
            if  first or distance < shortest:               # if it is the first distance or the distance is shorter than shortest distance
                shortest = distance                         # set shortest to distance and
                if i["class"] == 0:                         # set value in pokemon p["class"] to appropriate class
                    p["class"] = 0 
                else: 
                    p["class"] = 1
                first = False                               # set first to false when first element in list is checked

    

#----- desideClass      -----   -----                   -----                  -----   -----                   -----                  -----   -----                   
def decideClass(testList, dataList):                        # decide class of every pokemon in testList compared to pokemons in dataList
    for p in testList:                                      # for every pokemon in testList
        whichClass(p, dataList)                             # which class is the current pokemon from testList compared to pokemons in dataList


#----- printPok         -----   -----                   -----                  -----   -----                   -----                  -----   -----                   
def printPok(list):

    for p in list:                                      
        print("Pokemon :", p)                               # print the pokemon
        if p["class"] == 0:                                 # and which type
            print(" is a Pichu !")
        else:
            print(" is a Pikachu !")


#----- getNum           -----   -----                   -----                  -----   -----                   -----                  -----   -----
def getNum():                                               # function for getting a numerical input                                      
                                                                
    isnum = False                                           # a boolean trigger set to false
    while not isnum:                                        # as long as isnum is false
        inmat = input("Please, enter a positive number : ") # it will keep asking for a numeric input
        if float(inmat) and float(inmat) > 0:               # if the input is a positive numeric, isnum is set to true, stopping the loop
            isnum = True
    
    return float(inmat)                                     # when the function is done it returns users numerical input 
                                                            # in float format


#----- getPok           -----   -----                   -----                  -----   -----                   -----                  -----   -----
def getPok():
    width = float
    length = float
    isNum = False
    print("Enter weight and length of your pokemon.")
    
    print("\nwidth .....")
    width  =    getNum()                                    # get width from user
                                       
    print("\nlength .....")
    length =    getNum()                                    # get length from user
                                    
    return width, length                                    # return width and length


#-----sortByDist        -----   -----                   -----                  -----   -----                   -----                  -----   -----
def sortByDist(list, x, y):
    
    for p in list:                                          # for each pokemon in list calculate distance to point x,y
                                                            
        p["distance"] = math.dist([p["width"],p["length"]], [x, y])
                                                       
    newlist = sorted(pokList, key=lambda d: d["distance"])  # sort by distance into a new list
    return newlist                                          # return the new list 


#----- voting           -----   -----                   -----                  -----   -----                   -----                  -----   -----
def voting(list):
    pichuVote = 0
    pikachuVote = 0
    for i in range(10):                                     # for 0 to 10
        if list[i]["class"] == 0:                           # check each pokemons class in list
            pichuVote = pichuVote + 1
        else:                                               # and count votes
            pikachuVote = pikachuVote + 1

    if pichuVote > pikachuVote:                             # if pichu is in majority 
        return True                                         # return true
    else:                                           
        return False                                        # else return false


#----- grund            -----   -----                   -----                  -----   -----                   -----                  -----   -----
def grund():                                                # phase one initiation

    pokList = fromFile("datapoints.txt")                    # create a list of pokemons from datapoints

    pchuX, pchuY, pkachX, pkachY = getXY(pokList)           # extract x and y by type

    shwPok(pchuX, pchuY, pkachX, pkachY, "width", "length") # calling shwPok to plot all pokemons in their respective class
                                                    
    testList = fromFile("testpoints.txt")                   # crete a list of pokemons from testpoints                                                                                     

    decideClass(testList, pokList)                          # decide class of each pokemon in testList compared to pokList

    printPok(testList)                                      # print out the pokemons in testList

    return pokList                                          # return list of pokemons from datapoints


#----- letUserType      -----   -----                   -----                  -----   -----                   -----                  -----   -----
def letUserType(list):

    width, length = getPok()                                # let the user type width and length of pokemon

    distList = sortByDist(list, width, length)              # sort pokemons in a new list by distance from the users pokemon width,length point 

    if voting(distList):                                    # check the 10 closest, to decide by majority wich class the pokemon is
        print("\nIt's a pichu!")                            # if equal vote the function will return false value
    else:
        print("\nIt's a pikachu!")                          # so it's slightly biased towards pikachu


#----- accTest          -----   -----                   -----                  -----   -----                   -----                  -----   -----
def accTest(list):                                          # testing accuracy with a list of elements
    
    trueNeg = 0
    falseNeg = 0
    truePos = 0
    falsePos = 0
    
    random.shuffle(list)                                    # shuffle the list

    trainList = list[:100]                                  # slice the list into two parts at element 100
    testList = list[100:]

    for p in testList:
        distList = sortByDist(trainList, p["width"], p["length"])       
                                                            # sort pokemons in trainlist by distance from the current pokemon in testList 

        if voting(distList):                                # check the 10 closest, to decide by majority wich class the pokemon should be, equal vote returns false value
            if p["class"] == 0:                             # if predicted class pichu is same in pokemon p
                trueNeg = trueNeg + 1                       # count up trueNegative
            else:
                falseNeg = falseNeg +1                      # else count up falseNegative
        else:
            if p["class"] == 1 :                            # if predicted class pikachu is same in element p
                truePos = truePos + 1                       # count up truePositive
            else:
                falsePos = falsePos + 1                     # else count up falsePos
                
    accuracy = (trueNeg + truePos)/(trueNeg + truePos + falseNeg + falsePos)

    return accuracy                                         # return accuracy


#----- testAccuracy     -----   -----                   -----                  -----   -----                   -----                  -----   -----
def testAccuracy(list):

    m_accuracy = 0.0
    i = 0
    while i != 10:                                          # a while loop that runs 10 times
        i = i+1
        accuracy = accTest(list)                            # each time accuracy is tested with accTest and list as parameter
        m_accuracy = m_accuracy + accuracy                  # add up all accuracy results   
        plt.plot(i, accuracy,'ro')                          # and each time plot the accuracy and the test number into the graph

    m_accuracy = round((m_accuracy/ i), 3)                  # average accuracy = accumulated accuracy / number of tests, round to 3 decimals
    text = "average accuracy = {}"
    text = text.format(m_accuracy)                           

    plt.xlabel("test")
    plt.ylabel("accuracy")
    plt.title(text)                                     

    plt.show()                                              # show the graph


#----- askUser          -----   -----                   -----                  -----   -----                   -----                  -----   -----
def askUser():                                              # simple user interface 

    choice = 0
    while (choice != 1) and (choice != 2) and (choice !=3): # as long as user doesn't pick one of the three alternatives
        print("\n Do you want to :")                        # the loop will continue
        print(" 1 classify a pokemon ")
        print(" 2 test accuracy ")
        print(" 3 quit\n")
        choice = getNum()                                   # get number input from user
        if (choice != 1) and (choice != 2) and (choice != 3):
            print("\nSorry. What?")                         # if users input is a number but not 1, 2 or 3 
        
    return choice                                           # return users choice



# Main ----------------------------------------------------------------------------------------------------------------------------------------------
quit = False

print("\n\n... initiating Grunduppgift ...\n")

pokList = grund()                                           # execute Grunduppgift, returns a list of pokemons from datapoints 

while not quit:

    choice = askUser()
    if choice == 1:
        print("\n\n... initiating Uppgift 1 & 2 ...\n")

        letUserType(pokList)                                # send pokList to letUserType                                    
    
    if choice == 2:

        print("\n....... initiating Bonus .......\n")

        testAccuracy(pokList)                               # send pokList to testAccuracy
    
    if choice == 3:

        quit = True                                         # quit

    
print("\n          THE END\n")