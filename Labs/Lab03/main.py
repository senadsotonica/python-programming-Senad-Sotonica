# this is for purpose of demonstrating
# the classes in shapes.py
# but I did it for the fun of it
# //Sotonica

import sys
import time
import random

sys.path.append(".")

from shapes import Circle
from shapes import Rect
from shapes import Sphere
from shapes import Cuboid


#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
#   just a hello    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def hello():
    print("")
    time.sleep(0.4)                                                                 
    print("<<<([ Howdy Stranger!")
    time.sleep(0.4)                                     
    print("<<<([ I am RANGER Shapes.")
    time.sleep(0.4)
    print("<<<([ RAN(dom) GE(nerato)R of Shapes")
    time.sleep(0.4)
    print("<<<([ These are your options :")   


#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
#   main menu   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def main_menu():
    time.sleep(0.4)
    print("")
    time.sleep(0.15)
    print("-.,.-*'] M E N U ['*-.,.-")
    time.sleep(0.15)
    print("")
    time.sleep(0.15)
    print("   1   run demo")
    time.sleep(0.15)
    print("   2   shut me down")
    time.sleep(0.15)
    print("")
    time.sleep(0.15)
    print("-*'^-.o]>> ~*~ <<[o.-^'*-")
    time.sleep(0.15)
    print("")

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #   -   -   -   -   -   -   -   -   -
#   func retrieving n from user -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   - 
def get_n() -> int:
    x = False
    while not x:
        main_menu()                                                             # show options to user                                                             
        print("<<<([ Your choice")
        n = input("])>>> ")                                                     # getting input from user
        if n == '1' or n == '2':                                                # is the input 1 or 2 ?       
            x = True                                                            # if so don't repeat, go to return
        else:
            print("\n<<<([ No can do !")                                        # if not tell user
                                                                                # and repeat

    return int(n)                                                               # return n as int

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #   -   -   -   -   -   -   -   -   -
#   func for creating a list of n shapes    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def create_shapes(n = 1, choice = "2d"):

    if choice == "2d":                                                          # setting the conditions
        rand_a = 1
        rand_b = 2
    elif choice == "3d":
        rand_a = 3
        rand_b = 4
    else:
        raise ValueError("<<<([ Critical ERR: check second parameter in create_shapes()")

    time.sleep(0.4)
    print("\n<<<([ generating %s random %s shapes ])>>>\n" % (n, choice))
    time.sleep(0.4)

    list = []
    
    x = 0
    while x < n:                                                                # for each n
        choice = random.randint(rand_a, rand_b)                                 # randomize between 1 and 2 if 2d
                                                                                # randomize between 3 and 4 if 3d
        time.sleep(1)
        if choice == 1:                                                         # depending on value of choice
            txt = "([ circle ])"                                                # an object will be generated
            list.append(Circle(random.randint(1, 10)))                          # and added to the list
        elif choice == 2:
            txt = "([ rectangle ])"
            list.append(Rect(random.randint(1, 10), random.randint(1, 10)))
        elif choice == 3:
            txt = "([ sphere ])"
            list.append(Sphere(random.randint(1, 10)))
        elif choice == 4:
            txt = "([ cuboid ])"
            list.append(Cuboid(random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)))
        else:
            raise ValueError("<<<([ ERR: << n out of range >>")
        print("<<<([ shape nr %s is a %s:" % ((x + 1), txt))
        print(str(list[x]))
        x = x + 1

    return list                                                                 # return list when finnished


#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #   -   -   -   -   -   -   -   -   -
#   func prints the objects in the list -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def print_list(list, t = "2d", p = 0):                                          # print objects of list
                                                                                # t is by default "2d", or set to "3d"
                                                                                # set p to 1 to print position of object
    row1       = "<<<([ type     : "                                            # labeling row1
    if t == 0 :                                                                 # depending on t
        row2   = "<<<([ area     : "                                            # different attributes are of interest
    else:                                                                       # label for row2 is set
        row2   = "<<<([ volume   : "

    if p != 0:                                                                  # if position is to be printed
        row3   = "<<<([ position : "                                            # label for row3

    for x in range(len(list)):                                                  # iterate list with x in range of length of list
        txt = str(list[x].i_am()).rsplit('.')                                   # retrieve type from object
        if len(txt[1]) == 6:                                                    # and clean up the string
            spc = "       "
        else:                                                                   # adjust space in txt
            spc = "     "
        row1 = row1 + txt[1].replace("'>", spc)                                 # add txt to row 1

        if t == "2d":                                                           # if 2D object, area is of interest
            txt = str(list[x].area)                                             # txt is area
        elif t == "3d":                                                         # if 3D object, volume is of interest
            txt = str(list[x]._volume)                                          # txt is volume
        else:                                                                   
            raise ValueError("<<<([ ERR: << wrong type 2nd argument in print_list() ")

        txt = txt[:6]
        while len(txt) < 6:                                                     # ljust() didn't work for me
            txt = txt + ' '                                                     # so I did this instead
        row2 = row2 + txt + "     "                                             # add txt to row2 with needed spacing

        if p != 0:                                                              # if position is to be printed
            txt = str(list[x].x) + ", " + str(list[x].y)                        # add x and y to txt
            if t == "3d":                                                       # and z if 3D
                txt = txt + ", " + str(list[x].z) 
                txt = txt + "    "                                              # adjust spacing to 3D
            else:
                txt = txt + "       "                                           # spacing when 2D
            row3 = row3 + txt                                                   # add txt to row 3


    time.sleep(0.4)   
    print(row1)                                                                 # print row 1
    time.sleep(0.4)
    print(row2)                                                                 # print row 2
    
    if p!= 0:
        time.sleep(0.4)
        print(row3)                                                             # print row 3


#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #   -   -   -   -   -   -   -   -   -
#   func translates objects in list -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def translate_list(list, t = "2d"):

    for x in range(len(list)):                                                  # iterate list
        if t == "2d":                                                           # if 2D, randomize x and y with 
            list[x].translate(random.randint(1, 5), random.randint(1, 5))       # values 1 to 5
        elif t == "3d":                                                         # if 3 D, randomize x, y and z 
            list[x].translate(random.randint(1, 5), random.randint(1, 5), random.randint(1, 5))
        else:
            raise ValueError("<<<([ ERR: << wrong second argument in translate_list()")

#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   #   -   -   -   -   -   -   -   -   -
#   func demo   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
def demo():
    
    n = 5                                                                       # n is 5
    list_2d = create_shapes(n, "2d")                                            # generate n 2d shapes in a list
    list_3d = create_shapes(n, "3d")                                            # generate n 3d shapes in a list
    print("\n<<<([ These are the 2D shapes I have generated:")
    print_list(list_2d)                                                         # print list of 2d shapes
    time.sleep(0.4)                                                             # time.sleep 0.5 sec is only for dramatic effect
    print("\n<<<([ These are the 3D shapes I have generated:")
    print_list(list_3d, "3d")                                                   # print list of 3d shapes
    time.sleep(0.4)                                                               
    print(" ")

    print("\n<<<([ Sorting list with 2D shapes ...")
    list_2d.sort()                                                              # sort list 2d
    time.sleep(0.4)

    print("\n<<<([ Sorting list with 3D shapes ...")
    list_3d.sort()                                                              # sort list 3d
    time.sleep(0.4)

    print("\n<<<([ Printing the sorted 2D list ...")
    print_list(list_2d, "2d")                                                   # print list 2d
    time.sleep(0.4)
    
    print("\n<<<([ Printing the sorted 3D list ...")
    print_list(list_3d, "3d")                                                   # print list 3d
    time.sleep(0.4)

    print("\n randomly translate objects in 2D list ...")
    translate_list(list_2d, "2d")                                               # let the objects have new positions x, y
    time.sleep(0.4)

    print("\n randomly translate objects in 2D list ...")
    translate_list(list_3d, "3d")                                               # let the objects have new positions x, y, z
    time.sleep(0.4)

    print("\n print 2D list with the new positions...")
    print_list(list_2d, "2d", 1)                                                # print list 2d and show position
    time.sleep(0.4)

    print("\n print 3D list with the new positions...")
    print_list(list_3d, "3d", 1)                                                # print list 3d and show position
    time.sleep(0.4)

    
#   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
#   main    -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -

hello()                                                                         # wellcome screen :)

run_it = True

while run_it == True:

    n = get_n()                                                                 # get choice from user
    if n == 1 or n == 2:
        print("\n<<<([ Allrighty then !!!")
        if n == 1:                                                              # if 1 run demo
            demo()  
        elif n == 2:                                                            # if 2 quit
            run_it = False
            print("\n<<<([ Have a nice day... night ? something ? whatever. C'ya!\n")
    else:                                                                       # else ask wtf?
        print("\n<([ Pardon? You're mumbling ...\n")

