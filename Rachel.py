#Geom 67 Group 2 Purrfect Pals Computer Terminal Game
#Rachel's code for Gary's Cat Cafe location
#version 1.0
#cat ascii art from: #http://www.ascii-art.de/ascii/c/cat.txt

import random

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
                    {'actionName': 'treats', 'likes': False},
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
                    {'actionName': 'treats', 'likes': True},
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
            }
        ]
    


def catlist():
    mycats = gary_cats()
    random.shuffle(mycats)
    return mycats

def introduce_cat(cat):
    print("Hi, friendly human, I'm " + cat['name'] + " and I'm a " + cat['color'] + ", " + cat['breed'] + " cat, who is very " + cat['personality'] + ". I am a " + cat['age'] + ".  Let's have fun!")  #####add int rest of cat intro statement calling from dictionary keys
    print()
    print("""ฅ^•ﻌ•^ฅ""")


def get_choice():
    print("Choose how you want to interact with me: 1. Brush, 2. Pet, 3. Play, 4. Give a treat")
    useraction = int(input("What would you like to do? Type the number for the action."))
    return useraction

def do_action(choice, cat, points):
    doesLike = cat['actions'][choice]['likes']
    if doesLike:
        print()
        print("PURR, I love it!")
        print("""ฅ^•ﻌ•^ฅ""")
        print("Purr-fect!")
        print()
        points += 1
    else:
        print("""
     (\
      ))         )\\
     ((         /  .(
      \\.-"```"'` =_/=
       >  ,       /
       \   )__.\ |
        > / /  ||\\
   jgs  \\ \\  \\ \\
         `" `" `"  `"
                   """)
        print("Boo. HISS. Boo! ")
        print("I just scratched you!")
        points -= 0
    return points

def print_welcome_message():
    print('=^..^=     ','=^..^=     ','=^..^=     ' )
    print("Welcome to Gary's Cat Cafe.  Each of our cat pals is ready to find their furrever home.  Let's make a match! ")
    print("""
            _,'|             _.-''``-...___..--';)
           /_ \'.      __..-' ,      ,--...--'''
          <\    .`--'''       `     /'
           `-';'               ;   ; ;
     __...--''     ___...--_..'  .;.'
 fL (,__....----'''       (,..--''
     """)

#TODO
#if lives is > 0 
#lif lives is <= 0 then print("You lost! Good bye. GAME OVER.")

def main(userstate):
    username = userstate['username']
    points = userstate['points']
    cats_collected = userstate['cats_collected']
    print('=^..^=')
    print("Hello " + username)
    print_welcome_message()

    

    for catdictionary in catlist():
        introduce_cat(catdictionary)
        for x in range(1,5):
            choice = get_choice()
            points = do_action(choice, catdictionary, points)
            #compare points before and after.  if user gained 3 points, cat is added to cats_collected
            #                                   anything other than ^, cat is not added to cats_collected

            print("Congratulations, you have " + str(points) + " points.")
            print()
            print()
    return {'points': points, 'cats_collected': cats_collected, 'username': username}

##################### Output message from four cats at Gary's Cat Cafe ##############################

#################### Start of input ########################

############### End of input, Start of calculations ################

############## End of calculations, Start of output #################

###output .txt of user score and names of cats adopted.

#so i can run this file alone: delete for actual use. 
if __name__ == '__main__':
    main({'points':0, 'cats_collected':[], 'username':'TESTPERSON'})
    #(username, points, cats_collected)

# if __name__=='__main__':  #calling defined function 'main
#     username = input("What is your name?")
#     main(username, 0)