# A guessing program
# user vs computer

import random

#[      --- menu ---        ]#                                                                # in int format
def menu():
    print("\n         ...:::'[ Menu ]':::...\n")
    print("1  - Computer picks. User guesses.")
    print("2  - User picks. Computer guesses.")  
    print("3  - quit")
    print("\nWhat will it be? ")

def guess(nr):
    
    #start = 1
    end = 100
    count = 0
    search = end / 2
    guess = search
    
    right = False
    while not right:
        # guess = random.randrange(start, end)
        
        count = count + 1
        print(guess)
        a = input("guess")
        if guess == nr:
            right = True
            a = input("r")
        else:
            if search > 1:
                search = int(search/2)
            if guess < nr:
                guess = guess + search
                print("left")
            else: 
                guess = guess - search
                print("right")
        
    return count, a


nr = random.randrange(1, 100)
print(nr)
print(guess(nr))
