## group 2 project 2 ##
## GEOM 67, Problem Solving and Programming, Karen Whillans ##
## Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte ##

## Find the Purrrrfect Friend Game ##


import math
import random

import Rachel
# import Vince    #uncomment other group member names to run whole program.  commented out for testing. 
# import Kendyll
# import Carol

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
    
#function to get user to imput name
def get_name():
    return input("Gamer, what is your name? ")







#defines a function with an array containing the four different location files
#random.shuffle returns the list in a random order


#defining the main program function
def main():
    location = ["LRachel", "LVince", "LKendyll", "LCarol"]
    random.shuffle(location)
    print(location)

    #user state to retain and hold accrued points and cats
    #dictionary to get passed around location files and hold the state of the game
    userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':9 }

    #call in print_intro
    print_intro()

    #get the user's name
    print()
    userstate['username'] = str(input("   Gamer, what is your name? "))
    #print(userstate['username'])
    

    #for loop to iterate through each location
    for loc in location:
        if loc == "LRachel":
            print("call main function of your program here Kendyll")
            Rachel.main(userstate)
            if userstate['lives'] == 0:
                break
        elif loc == "LKendyll":
            print("call main function of your program here Kendyll")
            if userstate['lives'] == 0:
                break
        elif loc == "LCarol":
            print("call main function of your program here Carol")
            if userstate['lives'] == 0:
                break
        else:
            print("call main function of your program here Vince")
            if userstate['lives'] == 0:
                break

    #TODO add function to end game with if user has gone through all four locations and still has lives, then end game and print out .txt file with results
    #add game ending 

    #NOTE use this code for running the game through all four locations
    #NOTE when using this, delete --> userstate = Rachel.main(userstate)
    # for location in locations():
    #    userstate = location.main(userstate)


if __name__=='__main__':  #calling defined function 'main'
    main()



    #ignore.
    #possibly extra code: 
    #call in CSV
#open file catdata.csv for reading
# with open('catdata.csv') as catdata:
#     for cat in catdata: