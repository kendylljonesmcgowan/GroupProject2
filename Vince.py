# PSP Assignment 3
# Location: AllPaws Cat Shelter
# Last modified: December 5, 2021

def userinput():
    print()
    ibrush = str(input("    Brush Me (Y/N): "))
    ipet = str(input("    Pet Me (Y/N): "))
    iother = str(input("    Have you already adopted another cat (Y/N): "))
    iplay = str(input("    B Me (Y/N): "))
    itreat = str(input("    Brush Me (Y/N): "))
    inputlist = [ibrush,ipet,iother,iplay,itreat]
    return inputlist

def lokipoints(illist):
    lokicombination = ("Y", "Y", "Y", "Y", "N")
    lokipoints = 0
    for trait in range(5):
        if lokicombination[trait] == illist[trait].upper():
            lokipoints += 1
    return lokipoints

def boopoints(iblist):
    boocombination = ("Y", "Y", "Y", "Y", "Y")
    boopoints = 0
    for trait in range(5):
        if boocombination[trait] == iblist[trait].upper():
            boopoints += 1
    return boopoints

def wandapoints(iwlist):
    wandacombination = ("N", "Y", "Y", "N", "N")
    wandapoints = 0
    for trait in range(5):
        if wandacombination[trait] == iwlist[trait].upper():
            wandapoints += 1
    return wandapoints

def tobipoints(itlist):
    tobicombination = ("N", "Y", "Y", "Y", "Y")
    tobipoints = 0
    for trait in range(5):
        if tobicombination[trait] == itlist[trait].upper():
            tobipoints += 1
    return tobipoints

#Not yet sure if this is useful might delete later
def pointstranslate(points):
    response = "should be overwritten"
    if points == 5:
        response = "We are going home together Pur-riend"
    elif points == 4:
        response = "Give me a sec! To think about it"
    elif points == 3:
        response = "I'm still deciding. But If I go with you, you have to be a better Owner! Meow!"
    else:
        response = """ 
        Don't like you Meow
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
        """
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
print("Welcome, AllPaws Cat Shelter")
print("Here you'll meet 4 new different cats")
print()

adoptedcatlist = []
loc4catlist = ["loki", "boo", "wanda", "tobi"]
random.shuffle(loc4catlist)

print(loc4catlist)
print()
for cats in loc4catlist:
    if cats == "loki":
        print("Meow, I’m Loki, I’m a beautiful Ragdoll Cat. I like warm places, and lounging in my favorite snuggly blanket. Paw-don me if I’m a little bit hiss-terical with kids, I’m just a little old now but I’m fiercely loyal kinda like a dog, but better because dogs are in-furior to cats. Duh!")
        lokiinput = userinput()
        print(lokiinput)
        print()
        print("The number of PurrPoints you got from Loki is: ", lokipoints(lokiinput))
        print()
        print(pointstranslate(lokipoints(lokiinput)))
        lokiadopt = adoptcat(lokipoints(lokiinput))
        if lokiadopt == 1:
            adoptedcatlist.append(cats)
            print("(=⚈ᆽ⚈=)")
            print("Friends forever") #make more puns
        elif lokiadopt == 0:
            print(
            """Don't like you Meow
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
        print()
        


    elif cats == "boo":
        print("Meow, I’m Boo! I’m a Persian kitten, please whisker me away to places because I love exploring! When I grow up, I want to join the olympics, because I’m cathletic! I love everyone including the UPS guy who brings me treats sometimes. I’m sure you’re going to love me meow until fur-ever!")
        booinput = userinput()
        print(booinput)
        print()
        print("The number of PurrPoints you got from Boo is: ", boopoints(booinput))
        print()
        print(pointstranslate(boopoints(booinput)))
        print()
        booadopt = adoptcat(boopoints(booinput))
        if booadopt == 1:
            adoptedcatlist.append(cats)
            print("(=⚈ᆽ⚈=)")
            print("Friends forever") #make more puns
        elif booadopt == 0:
            print(
            """Don't like you Meow
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
        print()



    elif cats == "wanda":
        print("Meow, are you feline good? I’m Wanda,and I love people. I dream of becoming the UN ambassador for Cat-nada! Snuggling is my number one priority! If only people were half as friendly as me, then the world would be paw-some.")
        wandainput = userinput()
        print(wandainput)
        print()
        print("The number of PurrPoints you got from Wanda is: ", wandapoints(wandainput))
        print()
        print(pointstranslate(wandapoints(wandainput)))
        print()
        wandaadopt = adoptcat(wandapoints(wandainput))
        if wandaadopt == 1:
            adoptedcatlist.append(cats)
            print("(=⚈ᆽ⚈=)")
            print("Friends forever") #make more puns
        elif wandaadopt == 0:
            print(
            """Don't like you Meow
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
        print()


    
    else:
        print("Meow, I’m Tobi! I’m a Burmese Cat. If I brush against you, that’s code for “Snuggles paw-lease”. Call the claw-enforcement because I will follow you all day, sit next to you, and brush against you!! What can I say? I just love you meowst.")
        tobiinput = userinput()
        print(tobiinput)
        print()
        print("The number of PurrPoints you got from Tobi is: ", tobipoints(tobiinput))
        print()
        print(pointstranslate(tobipoints(tobiinput)))
        print()
        tobiadopt = adoptcat(tobipoints(tobiinput))
        if tobiadopt == 1:
            adoptedcatlist.append(cats)
            print("(=⚈ᆽ⚈=)")
            print("Friends forever") #make more puns
        elif tobiadopt == 0:
            print(
            """Don't like you Meow
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
        print()


