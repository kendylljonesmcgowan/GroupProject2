## group 2 project 2 ##
## GEOM 67, Problem Solving and Programming, Karen Whillans ##
## Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte ##

## Find the Purrrrfect Friend Game ##


import math
import random

# import Rachel
# import Vince    #uncomment other group member names to run whole program.  commented out for testing. 
# import Kendyll
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


#defining the main program function
def main():
    #random.shuffle returns the list in a random order
    location = ["LRachel", "LVince", "LKendyll", "LCarol"]
    random.shuffle(location)
    print(location)

    #user state to retain and hold accrued points and cats
    #dictionary to get passed around location files and hold the state of the game
    userstate = {'points':0, 'cats_collected':[], 'username':' ', 'lives':3 }

    #call in print_intro
    print_intro()

    #get the user's name
    print()
    userstate['username'] = str(input("   Gamer, what is your name? "))
    print()
    #print(userstate['username'])
    

    #for loop to iterate through each location
    for loc in location:
        if loc == "LRachel":
            print("call main function of your program here Rachel")
            # userstate = Rachel.main(userstate)
            if userstate['lives'] == 0:
                break
        elif loc == "LKendyll":
            print("call main function of your program here Kendyll")
            # kendylltuple=(Kendyll.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives']))
            # userstate['points'] = kendylltuple[0]
            # userstate['lives'] = kendylltuple[1]
            if userstate['lives'] == 0:
                break
        elif loc == "LCarol":
            print("call main function of your program here Carol")
            # test
            caroltuple = Carol.main(userstate)
            print(caroltuple)
            # userstate['points'] = caroltuple[0]
            # userstate['lives'] = caroltuple[1]
            if userstate['lives'] == 0:
                break
        else:
            print("call main function of your program here Vince")
            # vincetuple = Vince.main(userstate['points'],userstate['cats_collected'],userstate['username'],userstate['lives'])
            # print(vincetuple)
            # userstate['points'] = vincetuple[0]
            # userstate['lives'] = vincetuple[1]
            if userstate['lives'] == 0:
                break

    #TODO add function to end game with if user has gone through all four locations and still has lives, then end game and print out .txt file with results
    #add game ending

    #Will be fixed to look better
    if userstate['lives'] == 0:
        print()
        print ("GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! ")
        print ("Here is you game summary: ")
        print ("Cats Adopted")
        print (userstate["cats_collected"])
        print ("PurrPoints")
        print (userstate["points"])
    else:
        print()
        print ("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMEOW!!!!!!")
        print ("Congratulations for Finishing the the game!")
        print ("Here is you game summary: ")
        print ("Cats Adopted")
        print (userstate["cats_collected"])
        print ("PurrPoints")
        print (userstate["points"])
        print ("Lives Left")
        print (userstate["lives"])



if __name__ == '__main__':
    main()
    #(username, points, cats_collected, userlives)



    #ignore.
    #possibly extra code: 
    #call in CSV
#open file catdata.csv for reading
# with open('catdata.csv') as catdata:
#     for cat in catdata: