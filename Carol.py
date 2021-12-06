# Carol.py test file; not a working code yet
# main definition adn call at end is from Rachel
import math
import random
#define functions
def main(username):
    print("Hello " + username)

# write up intros for each cat at Happy Tails Rescue: Gary, Buster, Ophelia, Artemis
# each cat needs 8 statements for positive and negative interactions

# location input exception:
def main(location_exception):
  while current_location = chosen_location:
    print("You're already here! Where would you like to go next?")
    print(locations)
    chosen_location = input("  Chose which location you'd like to go to:  ")

# while loop for full game
# define beginning variables for lives and points
lives = 9
purr_points = 0

def main(nolivesremaining):
  # WITHIN LOOP: likely has to be defined and called after every full cat event
  if lives == 0:
    break # this will break the whole game loop onces lives have run out IF IN OUTER LOOP
    # end of FULL GAME LOOP due to loop break

def main(end_statements):
  if lives == 0:
    print("You've run out of lives!")
    print("GAME OVER")
    print("YOu adopted the following cats:"+ adopted_cats + "!")
    print("Purr points collected:" + purr_points)
  else:
    print("You adopted the following cats:"+ adopted_cats + "!")
    print("Purr points collected:" + purr_points + ";  Lives remaining:" + lives)

def main(cat_interactions):
# while loop for individual cat??
negative_interactions = 0
positive_interactions = 0
cats_interacted_with = 0
while negative_interactions < 3:
  print(action_options)
  action = input("  What would you like to do with", current_cat, "? :  ")
  if action = False:
    negative_interactions+=1
    print("negative interaction statment for cat")
    cats_interacted_with+=1
  else:
    positive_interactions+=1
    print("positive interaction statement for cat")
    cats_interacted_with+=1

# negative interactions in 3rd and following interactions with cats within cat interaction events
def main(lostlife):
if negative_interactions == 3:
  print("Oh meow!! This cat doesn't want to come home with you!")
  lives-=1
  break     # will only affect the loop it is within, if nested outer loop will still run


# DON'T DELETE THIS
if __name__=='__main__':  #calling defined function 'main
    username = input("What is your name?")
    main(username)
