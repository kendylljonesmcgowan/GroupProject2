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

#defined main function
#calls one of the four location files
#random.shuffle will call each location file in a random order
def main():
    locations = [Rachel, Vince, Kendyll, Carol]
    for location in random.shuffle(locations): 
        location.main()






if __name__=='__main__':  #calling defined function 'main'
    main()