import matplotlib.pyplot as plt
import random
import math

pokList = []                                        # list of pokemons

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
    


def accTest(list):
    
    trueNeg = 0
    falseNeg = 0
    truePos = 0
    falsePos = 0
    
    random.shuffle(list)                                    # shuffle the list

    trnList = list[:100]                                    # slice the list into two parts at element 100
    tstList = list[100:]

    for p in tstList:
        distList = sortByDist(trnList, p["width"], p["length"])       
                                                            # sort pokemons from trainlist by distance from the current test pokemon width,length point 

        if whichIsIt(distList):                             # check the 10 closest, to decide by majority wich class the pokemon is, if equal vote it vill return false value
            if p["class"] == 0:                             # if predicted class pichu is same in element p
                trueNeg = trueNeg + 1                       # count up trueNegative
            else:
                falseNeg = falseNeg +1                      # else count up falseNegative
        else:
            if p["class"] == 1 :                            # if predicted class pikachu is same in element p
                truePos = truePos + 1                       # count up truePositive
            else:
                falsePos = falsePos + 1                      # else count up falsePos
                
    accuracy = (trueNeg + truePos)/(trueNeg + truePos + falseNeg + falsePos)

    return accuracy
        


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
            
        line = reader.readline()                    # read in next line from file, before repeating 

i = 0
while i != 10:                                      # a while loop that runs 10 times
    i = i+1
    accuracy = accTest(pokList)                     # each time accuracy is tested with accTest and pokList as parameter
    plt.plot(i, accuracy,'ro')                      # and each time we plot the accuracy into the graph
    

m_accuracy = accuracy/ i                            # average accuracy
text = "average accuracy = {}"
text = text.format(m_accuracy)                      # as text      

    
plt.xlabel("test")
plt.ylabel("accuracy")
plt.title(text)                                     

plt.show()                                          #show the graph
