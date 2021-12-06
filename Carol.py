# Carol.py test file; not a working code yet
# DESIGNED FOR:
# group 2 project 2
# GEOM 67, Problem Solving and Programming, Karen Whillans
# Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte
## Find the Purrrrfect Friend Game ##

# main definition and call at end is from RachelM

# to do for game:
# define variables for lives, purr points, cats adopted, 

import math
import random
#define functions
def main(username):
    print("Hello " + username)

# write up intros for each cat at Happy Tails Rescue: Gary, Buster, Ophelia, Artemis
# each cat needs 8 statements for positive and negative interactions

# location input exception: NOT USING randomizing location presentation instead
# def main(location_exception):
#   while current_location is chosen_location:
#     print("You're already here! Where would you like to go next?")
#     print(locations)
#     chosen_location = input("  Chose which location you'd like to go to:  ")

# from master file
#defining print_intro as a funtion
def print_intro():
    print('=^..^=     ','=^..^=     ','=^..^=     ' )
    print('      =^..^=     ','=^..^=     ')
    print("Welcome to 'PURRfect Pals'")
    print()
    print(' =^..^= ')
    print("Get ready to meet and adopt feline friends from four different cat rescues.")
    print("Each cat is looking for their furrever home, will you be the purrfect match?")

# from master file
# sets up user variables!
def main():
    #random.shuffle returns the list in a random order
    location = ["Rachel", "Vince", "Kendyll", "Carol"]
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
    

lives = 9
def main(nolivesremaining):
  # WITHIN LOOP: likely has to be defined and called after every full cat event
  if lives == 0:
    break # this will break the whole game loop onces lives have run out IF IN OUTER LOOP
    # end of FULL GAME LOOP due to loop break

adopted_cats = {}
purr_points = 0
def main(end_statements):
  if lives == 0:
    print("You've run out of lives!")
    print("GAME OVER")
    print("You adopted the following cats:"+ adopted_cats + "!")
    print("Purr points collected:" + purr_points)
  else:
    print("You adopted the following cats:"+ adopted_cats + "!")
    print("Purr points collected:" + purr_points + ";  Lives remaining:" + lives)

# def main(cat_interactions):
# # while loop for individual cat??
# negative_interactions = 0
# positive_interactions = 0
# while negative_interactions < 3:
#   print(action_options)
#   action = input("  What would you like to do with", current_cat, "? :  ")
#   if action = False:
#     negative_interactions+=1
#     print("negative interaction statment for cat")
#   else:
#     positive_interactions+=1
#     print("positive interaction statement for cat")
#   cats_interacted_with+=1


# cats_interacted_with = 0
# negative interactions in 3rd and following interactions with cats within cat interaction events
# def main(lostlife):
# if negative_interactions == 3:
#   print("Oh meow!! This cat doesn't want to come home with you!")
#   lives-=1
#   cats_interacted_with+=1
#   break     # will only affect the loop it is within, if nested outer loop will still run


# DON'T DELETE THIS?
if __name__=='__main__':  #calling defined function 'main
    username = input("What is your name?")
    main(username)

# print("""
#          *                  *
#              __                *
#           ,db'    *     *
#          ,d8/       *        *    *
#          888
#          `db\       *     *
#            `o`_                    **
#       *               *   *    _      *
#             *                 / )
#          *    (\__/) *       ( (  *
#        ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.
#       | @|  ={      }= | @|  / / | @|o |
#      _j__j__j_)     `-------/ /__j__j__j_
#      ________(               /___________
#       |  | @| \              || o|O | @|
#       |o |  |,'\       ,   ,'"|  |  |  |  hjw
#      vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v
#                 _) )    `. \ /
#                (__/       ) )
#                          (_/
# """)
