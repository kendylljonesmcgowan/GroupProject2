## group 2 project 2 ##
## GEOM 67, Problem Solving and Programming, Karen Whillans ##
## Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte ##

## Find the Purrrrfect Friend Game ##


import math
import random

import Rachel
import Vince
import Kendyll
import Carol

# Display program purpose
#defining print_intro as a funtion
def print_intro():
    print('=^..^=     ','=^..^=     ','=^..^=     ' )
    print('      =^..^=     ','=^..^=     ')
    print("Welcome to 'PURRfect Pals'")
    print()
    print(' =^..^= ')
    print("Get ready to meet and adopt feline friends from four different cat rescues.")
    print("Each cat is looking for their furrever home, will you be the purrfect match?")
    print()
    print("The Goal of the game is to adopt all 16 cats!")
    print("And to collect as many PurrPoints as possible!")
    print("You have 9 lives!!")
    print("Note: Be sure to read the instruction for each location as there may be some quirks!!")



#defining the main program function
def main():
    #random.shuffle returns the list in a random order
    location = ["LRachel", "LVince", "LKendyll", "LCarol"]
    random.shuffle(location)

    #user state to retain and hold accrued points and cats
    #dictionary to get passed around location files and hold the state of the game
    userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':9 }

    #call in print_intro
    print_intro()

    #get the user's name
    print()
    userstate['username'] = str(input("   Gamer, what is your name? "))
    print()
    

    #for loop to iterate through each location
    for loc in location:
        if loc == "LRachel":
            userstate = Rachel.main(userstate)
            if userstate['lives'] == 0:
                break
        elif loc == "LKendyll":
            kendylltuple=(Kendyll.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives']))
            userstate['points'] = kendylltuple[0]
            userstate['lives'] = kendylltuple[1]
            if userstate['lives'] == 0:
                break
        elif loc == "LCarol":
            caroltuple = Carol.main(userstate)
            print(caroltuple)
            # had to change keys to points/lives vs 0/1 as they were in default program layout
            userstate['points'] = caroltuple['points']
            userstate['lives'] = caroltuple['lives']
            if userstate['lives'] == 0:
                break
        else:
            vincetuple = Vince.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives'])
            print(vincetuple)
            userstate['points'] = vincetuple[0] #updates the current number of purrpoint
            userstate['lives'] = vincetuple[1] #update the current number of lives
            if userstate['lives'] == 0:
                break

    if userstate['lives'] == 0:
        print()
        print ("GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! ")
        print ("Here is you game summary: ")
        print ("    You were able to adopt these cat:")
        print ("        " + str(userstate["cats_collected"]))
        print ("    The amount PurrPoints collected is " + str(userstate["points"]))
    else:
        print()
        print ("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMEOW!!!!!!")
        print ("Congratulations for Finishing the the game!")
        print ("Here is you game summary: ")
        print ("    You were able to adopt these cat:")
        print ("        " + str(userstate["cats_collected"]))
        print ("    The amount PurrPoints collected is " + str(userstate["points"]))
        print ("    Lives Left: " + str(userstate["lives"]))



if __name__=='__main__':  #calling defined function 'main'
    main()