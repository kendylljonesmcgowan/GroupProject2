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

    print("Welcome to 'PURRfect Pals'")
    print('*****=^..^=*****')
    print("Get ready to meet and adopt feline friends from four different cat rescues.")
    print("Each cat is looking for their furrever home, will you be the purrfect match?")
    
#function to get user to imput name
def get_name():
    return input("Gamer, what is your name? ")


#defines a function with an array containing the four different location files
#random.shuffle returns the list in a random order
def locations():
    return random.shuffle([Rachel, Vince, Kendyll, Carol])

#defining the main program function
def main():
    #call in print_intro
    print_intro()
    #get the user's name
    username = get_name()

    #for loop to iterate through each location
    for location in locations():
        location.main()








if __name__=='__main__':  #calling defined function 'main'
    main()