# ## File: PSP Assignment 2, Implementation
# ## Find the PURRfect Friend Game
# ## Carol Buckingham, Kendyll Jones-McGowan, Rachel Manderfeld, Vince Ruel Alonte, GEOM 67 Section 61 
# ## Last modified November 29th, 2021
# ## Inputs: Player Name, Interaction Action, Adoption Selection, 
# ## Outputs: Purr Points, Lives Lost, 

# import random
# import math

# ## fix lives portion: add negative interactions and then use if for neg actions and tethert that to lives ##


# def main(username):
#         print("Hello" + username)
#         # all code goes below

#         ## call in csv

#         ## Location Code, begin Location Loop ##

#         Location = "Kitten City Rescue"
#         print("Meow-come to Kitten City Rescue! We have so many purrrfect cats here, and all of them can't wait to meet you! We hope you have a blast getting to know each of our paw-some friends! Enjoy," + username "and stay as long as you would like!"))

#         # for index in Location

#         ## Cat Intro's and Reactions ** still have to figure out "Purr Points" points system ** refer back to troll game assignment 1 for inspo ##

#         ## add inputs for these and print them at the beginning of each cat ##

#         purrpoints = int(0)
#         lives = int(9)
#         brushaction = str("Y/N")
#         petaction = str("Y/N")
#         playaction = str("Y/N")
#         treataction = str("Y/N")


#         ## CatName,Location,LocAlias,Colour,Breed,Personality,Age,      Brushing,Pets,OtherCats,Playing,Treats

#         # if catname = "Yams"
#         ## Yams,B,Kitten City Rescue,Orange,Short-Hair,athletic,kitten,n,y,y,y,y

#                 print("Meow, my name is Yams! I am an orange Short-Hair kitten with lots of energy. Lets go on an adventure outside and get lost! It is so much fun to sneak out of the house. I love pets, playng and yummy treats...")

#                 if brushaction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if petaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if playaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if treataction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat        

#         # if catname = "Leaf"
#         ## Leaf,B,Kitten City Rescue,Black,Short-Hair,aloof,adult,y,n,n,n,y

#                         print("Meow, my name is Leaf! I am a black Short-Hair adult and like to act aloof. I am happiest when napping in the corner while you read on a cozy winters day. I love brushing and yummy treats...")

#                 if brushaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if petaction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if playaction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if treataction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#         # if catname = "Fox"
#         ## Fox,B,Kitten City Rescue,Orange-White,Short-Hair,curious,adult,n,y,y,y,y

#                         print("Meow, my name is Fox! I am an orange-white Short-Hair adult that's full of curosity. I like to stare out the window and watch birds all day. I love pets, playng and yummy treats...")

#                 if brushaction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if petaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if playaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if treataction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#         # if catname = "Dana"
#         ## Dana,B,Kitten City Rescue,Calico,Short-Hair,independent,adult,y,y,n,n,n

#                         print("Meow, my name is Dana! I am a calico Short-Hair adult that is very independent. My dream day includes sleeping all day and running around the house late at night. I love brushing...")

#                 if brushaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if petaction == "N".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if playaction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

#                 if treataction == "Y".upper():
#                         print("Meow, I didnt like that, I dont think this is going to work...")
#                         print("No Purr Points earned")
#                         print("One life lost!")
#                         lives = (lives - 1)
#                         ## add ascii cat walking away
#                 else:
#                         print("Meow, you seem like a lot of fun, I think this is going to work out!")
#                         print("I would love for you to adopt me!")
#                         purrpoints = (purrpoints + 1)
#                         lives = (lives - 0)
#                         ## add happy ascii cat

# ## add outro for kitty city rescue! ##




## Old code to save just in case ##

# print("Welcome to the find your PURRfect friend game!")

# playername = input(str("What is your name?"))

# print( "Hello," + playername + "Welcome to Meow York City!! We will go thru 4 different Cat Discovery Areas. Where we will get to know the Unique Personalities of the different Cats To become the PURfect Cat Owner!" )
# print( "The goal of the game is to adopt all of the 16 cats. Each correct action towards a cat earns you “Purr Points”. The more Purr Points you earn the higher probability to adopt the cat. You have nine lives and you will lose a life and 3 “Purr Points” if the cat chooses not to be adopted." )
# print( "CATch them all! Hope you have PAWsome time playing our game!" )

def main(userstate):
        username = userstate['username']
        points = userstate['points']
        cats_collected = userstate['cats_collected']
        print('=^..^=')
        print("Hello " + username)
        print_welcome_message()

        def userinput():
                print()
                ibrush = str(input(" Would you like to Brush Me? (Y/N): "))
                ipet = str(input(" Would you like to Pet Me? (Y/N): "))
                iother = str(input(" Have you already adopted another cat? (Y/N): "))
                iplay = str(input(" Would you like to play with Me? (Y/N): "))
                itreat = str(input(" Would you like to give me a treat? (Y/N): "))
                inputlist = [ibrush,ipet,iother,iplay,itreat]
                return inputlist

        def yamspoints(iylist):
                yamscombination = ("N","Y","Y","Y","Y")
                yamspoints = 0
                for trait in range(5):
                        if yamscombination[trait] == iylist[trait].upper():
                                yamspoints += 1
                return yamspoints

        def leafpoints(illist):
                leafcombination = ("Y","N","N","N","Y")
                leafpoints = 0
                for trait in range(5):
                        if leafcombination[trait] == illist[trait].upper():
                                leafpoints += 1
                return leafpoints

        def foxpoints(iflist):
                foxcombination = ("N","Y","Y","Y","Y")
                foxpoints = 0
                for trait in range(5):
                        if foxcombination[trait] == iflist[trait].upper():
                                foxpoints += 1
                return foxpoints

        def danapoints(idlist):
                danacombination = ("Y","Y","N","N","N")
                danapoints = 0
                for trait in range(5):
                        if danacombination[trait] == idlist[trait].upper():
                                danapoints += 1
                return danapoints

        #Not yet sure if this is useful might delete later
        def pointstranslate(points):
                response = "should be overwritten"
                if points == 5:
                        response = "We are going home together Pur-riend"
                elif points == 4:
                        response = "Purrr... Give me a sec To think about it..."
                elif points == 3:
                        response = "I'm still deciding... But If I go with you, you have to be a better Owner! Meow!"
                else:
                        response = "Meow, I don't think this is going to work out... I don't want to go home with you."
                return response

        def adoptcat(points):
                import random
                adopt = 99999 # should be over written to 0 or 1. Zero NO ADOPT. One ADOPT
                if points == 5:
                        adopt = 1
                elif points == 4:
                        chance = random.randint(1,10)
                        if chance <= 2:
                                adopt = 0
                        else:
                                adopt = 1
                elif points == 3:
                        chance = random.randint(1,10)
                        if chance <= 4:
                                adopt = 0
                        else:
                                adopt = 1
                else:
                        adopt = 2 # Set to this so the if else statement on the vince main fuinction wont return anything since the translate function already said bye. Will fix later
                return adopt



        import random
        # Introduction to the Location
        print("Meow-come to Kitten City Rescue! We have so many purrrfect cats here, and all of them can't wait to meet you! We hope you have a blast getting to know each of our paw-some friends! Enjoy," + username "and stay as long as you would like!")
        print(username + ", Here you'll meet 4 new cat friends!")
        print()

        adoptedcatlist = [] #change to the dictionary
        purrpoints = 0 #change to the dictionary
        lives = 1 #change to the dictionary

        adoptedcatlist = []
        loc2catlist = ["yams", "leaf", "fox", "dana"]
        random.shuffle(loc2catlist)

        print(loc2catlist)
        print()
        for cats in loc2catlist:
                if cats == "yams":
                        print("Meow, my name is Yams! I am an orange Short-Hair kitten with lots of energy. Lets go on an adventure outside and get lost! It is so much fun to sneak out of the house. I love pets, other cats, playing and yummy treats...")
                        yamsinput = userinput()
                        print(yamsinput)
                        print()
                        print("The number of PurrPoints you got from Yams is: ", yamspoints(yamsinput))
                        print()
                        print(pointstranslate(yamspoints(yamsinput)))
                        yamsadopt = adoptcat(yamspoints(yamsinput))
                        if yamsadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                   _ |\_
                   \` ..\
              __,.-" =__Y=
            ."        )
      _    /   ,    \/\_
     ((____|    )_-\ \_-`
     `-----'`-----` `--`""")
                                print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go outside for a walk!") #make more puns
                        elif yamsadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
                  _
               |\/(__
               /     \_  
               |  __==/
               /   (
              ;     \
             /      |
            /    ,  /
          .'      | |
         /      --; |
         |         ||  __
         |        /_;-` _`'.
         \  '-----' _.-` '._)
          `'-------'""")
                                print("Sorry, you have lost a life")
                                lives -= 1#change to to use the master
                                if lives == 0:
                                        break
                        print()


                elif cats == "leaf":
                        print("Meow, my name is Leaf! I am a black Short-Hair adult cat and I like to act aloof. I am happiest when napping in the corner while you read on a cozy winter day. I don't like other cats, but I love brushing and yummy treats...")
                        leafinput = userinput()
                        print(leafinput)
                        print()
                        print("The number of PurrPoints you got from Leaf is: ", leafpoints(leafinput))
                        print()
                        print(pointstranslate(leafpoints(leafinput)))
                        print()
                        leafadopt = adoptcat(leafpoints(leafinput))
                        if leafadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""       
   /\_/\
   >^.^<.---.
  _'-`-'     )\
 (6--\ |--\ (`.`-.
     --'  --'  ``-'""")
                                print("Meow! I am so excited to go home with you. Friends fuuurever! I am going to nap alone in the corner now.")
                        elif leafadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
            /\
            \ \
             \ \
             / /
            / /
           _\ \_/\/\
          /  *  \@@ =
         |       |Y/
         |       |~
          \ /_\ /
           \\ //
            |||
           _|||_
          ( / \ )
            """)
                                print("Sorry, you have lost a life")
                                lives -= 1#change to to use the master
                                if lives == 0:
                                        break
                        print()


                elif cats == "fox":
                        print("Meow, my name is Fox! I am an orange-white Short-Hair adult cat that's full of curosity. I like to stare out the window and watch birds all day. I love pets, other cats, playng and yummy treats...")
                        foxinput = userinput()
                        print(foxinput)
                        print()
                        print("The number of PurrPoints you got from Fox is: ", foxpoints(foxinput))
                        print()
                        print(pointstranslate(foxpoints(foxinput)))
                        print()
                        foxadopt = adoptcat(foxpoints(foxinput))
                        if foxadopt == 1:
                                adoptedcatlist.append(cats)
                                print("""
                      ,
                    _/((
           _.---. .'   `\
         .'      `     ^ T=
        /     \       .--'
       |      /       )'-.
       ; ,   <__..-(   '-.)
        \ \-.__)    ``--._)
         '.'-.__.-.
           '-...-'  """)
                                print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go bird watching!")
                        elif foxadopt == 0:
                                print(
                        """Meow, I don't think this is going to work out...
            |\___/|
            )     (
           =\     /=
             )===(
            /     \
            |     |
           /       \
           \       /
            \__  _/
              ( (
               ) )
              (_(
            """)
                                print("Sorry, you have lost a life")
                                lives -= 1#change to to use the master
                                if lives == 0:
                                        break
                        print()



        else:
                print("Meow, my name is Dana! I am a calico Short-Hair adult cat that is very independent. My perfect day includes napping while the sun is up and running around the house late at night. I don't like other cats, but I love brushing...")
                danainput = userinput()
                print(danainput)
                print()
                print("The number of PurrPoints you got from Dana is: ", danapoints(danainput))
                print()
                print(pointstranslate(danapoints(danainput)))
                print()
                danaadopt = adoptcat(danapoints(danainput))
                if danaadopt == 1:
                        adoptedcatlist.append(cats)
                        print("""
                 (\(\
                 / ..(
              .-' ,_Y/
            .'     (
           /   \/  |
          _|  _/| //
        .',_\__)\_))
        '----,)""")
                        print("Meow! I am so excited to go home with you. Friends fuuurever! Let's go nap!") #make more puns
                elif danaadopt == 0:
                        print(
                """Meow, I don't think this is going to work out...
                              / )
              (\__/)         ( (
              )    (          ) )
            ={      }=       / /
              )     `-------/ /
             (              */
              \              |
             ,'\       ,    ,'
             `-'\  ,---\   | \
                _) )    `. \ /
               (__/       ) ) 
                         (_/""")
                        print("Sorry, you have lost a life")
                        lives -= 1#change to to use the master
                        if lives == 0:
                                break
                print()

        if lives == 0:
                print ("GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! GAME OVER!! ")
        print ("Here is you game summary: ")
        print ("Cats Adopted")
        print (adoptedcatlist)
        print ("PurrPoints")
        print (purrpoints)

        # extra goodbye code
#                 print("""       
#        _                        
#        \`*-.                    
#         )  _`-.                 
#        .  : `. .                
#        : _   '  \               
#        ; *` _.   `*-._          
#        `-.-'          `-.       
#          ;       `       `.     
#          :.       .        \    
#          . \  .   :   .-'   .   
#          '  `+.;  ;  '      :   
#          :  '  |    ;       ;-. 
#          ; '   : :`-:     _.`* ;
#       .*' /  .*' ; .*`- +'  `*' 
#       `*-*   `*-*  `*-*'"""
#         )

if __name__ == '__main__':
        main({'points':0, 'cats_collected':[], 'username':'', 'userlives':''})
        #(username, points, cats_collected)