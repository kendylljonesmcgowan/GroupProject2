#Geom 67 Group 2 Purrfect Pals Computer Terminal Game
#version 1.0

import math
import turtle
#import turtle for visual output?!
#bring in turtle from Assignment 1 .py files


#define functions


#call in CSV
#open file catdata.csv for reading
with open('catdata.csv') as catdata:
    for cat in catdata:




def main():

    # Display program purpose
    print("Welcome to 'PURRfect Pals'")
    print("Get ready to meet and adopt feline friends from four different cat rescues.")
    print("Each cat is looking for their furrever home, will you be the purrfect match?")
    

#################### Start of input ########################
input_username =  []       			# create empty list for user name

username = str(input("Gamer, what is your name? "))
print("Great! " + username + ", Pack your catnip and let's head to our first cat rescue!")
print('*****=^..^=*****') 
print('*****=^..^=*****')




############### End of input, Start of calculations ################





############## End of calculations, Start of output #################






if __name__=='__main__':  #calling defined function 'main'
    main()