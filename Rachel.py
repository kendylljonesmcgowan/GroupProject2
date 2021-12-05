#Geom 67 Group 2 Purrfect Pals Computer Terminal Game
#Rachel's code for Gary's Cat Cafe location
#version 1.0

#call in CSV
#open file catdata.csv for reading
# with open('catdata.csv') as catdata:
#     for cat in catdata:


import math
import random
#import turtle for visual output?!
#bring in turtle from Assignment 1 .py files


#list of dictionaries for cats at Gary's cat cafe
def gary_cats():
    return [
            {
                'name': 'Periwinkle',
                'color': 'blue-point',
                "breed": "Siamese",
                "personality": "cuddly",
                'age': "senior",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': True},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treas', 'likes': False},
                ]
            },
            {
                'name': 'Tabitha',
                'color': 'orange',
                "breed": "short-hair",
                "personality": "athletic",
                'age': "adult",
                'actions': [
                    { 'actionName': 'brushing', 'likes': False },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': False},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treas', 'likes': True},
                ]
            },
            {
                'name': 'SugarPaws',
                'color': 'tuxedo',
                "breed": "short-hair",
                "personality": "shy",
                'age': "kitten",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': False},
                    {'actionName': 'othercats', 'likes': True},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treas', 'likes': True},
                ]
            },
            {
                'name': 'Zelda',
                'color': 'seal-point',
                "breed": "Birman",
                "personality": "playful",
                'age': "adult",
                'actions': [
                    { 'actionName': 'brushing', 'likes': True },
                    {'actionName': 'pets', 'likes': True},
                    {'actionName': 'othercats', 'likes': False},
                    {'actionName': 'playing', 'likes': True},
                    {'actionName': 'treats', 'likes': True},
                ]
            },
        ]
    


def catlist():
    mycats = gary_cats()
    random.shuffle(mycats)
    return mycats

def introduce_cat(cat):
    print("Hi I'm " + cat['name']) #####add int rest of cat intro statement calling from dictionary keys

def get_choice():
    print("You can: 1. Brush, 2. Pet, 3. Play, 4. Give a treat")
    useraction = int(input("What would you like to do? Type the number of the action you would like to do."))
    return useraction

def do_action(choice, cat, points):
    doesLike = cat['actions'][choice]['likes']
    if doesLike:
        print("Purrrfect!")
        points += 1
    else:
        print("The cat just scratched you!")
        points -= 1
    return points

def print_welcome_message():
    print("Welcome Gary's Cat Cafe.  Each of our cat pals is ready to find their furrever home.  Let's make a match! ")

def main(userstate):
    username = userstate['username']
    points = userstate['points']
    cats_collected = userstate['cats_collected']
    print("Hello " + username)
    print_welcome_message()

    

    for catdictionary in catlist():
        introduce_cat(catdictionary)
        for x in range(1,5):
            choice = get_choice()
            points = do_action(choice, catdictionary, points)
            #compare points before and after.  if user gained 3 points, cat is added to cats_collected
            #                                   anything other than ^, cat is not added to cats_collected

            print("Congratulations, you have " + str(points) + "points.")
    return {'points': points, 'cats_collected': cats_collected, 'username': username}

##################### Output message from four cats at Gary's Cat Cafe ##############################
#if cat = "Periwinkle"
    print("Do you love to talk? Me too!  I am Periwinkle and while I may be a cuddly senior kitty, but I still am full of energy!  I always have stories to tell and opinions to share.  Let's watch TV and talk over the dialogue together!  ")

#"Tabitha" ""
#"SugarPaws" ""
#"Zelda" ""



#################### Start of input ########################
# input_username =  []       			# create empty list for user name


    print('*****=^..^=*****') 
    print("Great! " + username + ", Pack your catnip and let's head to Gary's Cat Cafe!")
    print('*=^..^=*')
    print()
    print("""
                        (`.-,')
                        .-'     ;
                    _.-'   , `,-
            _ _.-'     .'  /._
            .' `  _.-.  /  ,'._;)
            (       .  )-| (
            )`,_ ,'_,'  \_;)  fL
    ('_  _,'.'  (___,))
    `-:;.-'
    """)

#begin loop for Gary's Cat Cafe




#back end computer things here





############### End of input, Start of calculations ################
print("""
                                     ,
              ,-.       _,---._ __  / \
             /  )    .-'       `./ /   \
            (  (   ,'            `/    /|
             \  `-"             \'\   / |
              `.              ,  \ \ /  |
               /`.          ,'-`----Y   |
              (            ;        |   '
              |  ,-.    ,-'         |  /
              |  | (   |        hjw | /
              )  |  \  `.___________|/
              `--'   `--'
              
              """)
#http://www.ascii-art.de/ascii/c/cat.txt



############## End of calculations, Start of output #################


###output .txt of user score and names of cats adopted.


#so i can run this file alone: delete for actual use. 
if __name__ == '__main__':
    main({'points':0, 'cats_collected':[], 'username':'TESTPERSON'})
    #(username, points, cats_collected)



# if __name__=='__main__':  #calling defined function 'main
#     username = input("What is your name?")
#     main(username, 0)