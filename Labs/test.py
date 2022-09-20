import math

with open("testpoints.txt", 'r') as reader:         # open testpoints
    line = reader.readline()                        # first line is of no interest
    line = reader.readline()                        # read first point
    
    while line != '':                               # The EOF char is an empty string
        text = line.split()                         # spliting the line, I only need 2nd and 3rd bit

        # I borrowed this bit of magic, cleans the strings from non alphanumerical chars
        testX = float(''.join(letter for letter in text[1] if letter.isalnum()))  # weight in float 
        testY = float(''.join(letter for letter in text[2] if letter.isalnum()))  # length in float
        # https://www.geeksforgeeks.org/python-removing-unwanted-characters-from-string/ 

        d = math.dist((0,0), (testX, testY)) 
        print(d)
        line = reader.readline()
    
    6