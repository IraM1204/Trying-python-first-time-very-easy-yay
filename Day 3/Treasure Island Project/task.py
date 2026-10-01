print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're stuck at a crossroad. Which way do you go? Left or Right: ")
if direction == "Left":
    cave = input("You walk the path and reach a cave. What do you choose? Go in or Keep walking: ")
    if cave == "Go in":
        shuffle = input("You enter the cave and it's completely dark. You hear something shift near you. What do you do now? Keep going or Run: ")
        if shuffle == "Keep going":
            print("You're attacked by a paranormal entity. Game over.")
        else:
            print("Wise choice. You could have been killed by a paranormal entity.")
            river = input("You go ahead and see an X on the ground. It's the treasure! But to reach that treasure you need to cross a river of piranhas. Do you Swim or Take a longer way to the treasure by crossing the Haunted Hallows? Type s for the former or h for the latter: ")
            if river == "s":
                print("You're attacked by the piranhas. Game over.")
            else:
                haunted_hallows = input("You risk it and choose to go through the Haunted Hallows. As you go deeper in the forest. You hear leaves crunch behind you. Someone's there. Do you turn back or keep walking without looking back? Type t for the former and w for the latter: ")
                if haunted_hallows == "t":
                    print("A paranormal creature attacks you and enslaves your soul. You're stuck in the Hallows for life, as a zombie.")
                else:
                    input("You keep walking, even though you're very scared. But you eventually cross the Haunted Hallows and reach the treasure. You win!")
    else:
        water = input("You walk some distance and get thirsty. There's no stream anywhere close. You see a cottage but it's very creepy with a skull hanging at the porch. Do you risk it and ask for some water or keep walking thirsty? Type r for the former or t for the latter: ")
        if water == "r":
            print("A little dwarf comes out and helps you. You thank him and ask whatever you could do for his help. He takes it literally and makes you do his housework for forever. Oops..")
        else:
            print("You keep walking and due to immense thirst do not survive. Game over.")
else:
    fight = input("You get teleported to a witch's house. She's going to attack you. There are 3 objects. Which one do you choose to fight with? Broom or Cauldron or Chair: ")
    if fight == "Broom":
        room = input('The witch easily defeats you and you are injured. You have fainted and when you wake up, youre locked in a dark room. You hear a shuffling. What do you do? Scream (and risk your presence revealed) or Stay silent (and keep waiting till someone finally comes to rescue you:')
        if room == "Scream":
            print("The monster detects your presence and eats you alive. Game over.")
        else:
            dark = input("After what felt like eternity, the door unlocked and a kind old lady opens the door. You ask the lady for directions to get out of the house. She helps you out and you're out on a street but it's getting dark. You need shelter quickly. What do you do? Do you search for a shelter or rest under a tree? Type s for the former and r for the latter: ")
            if dark == "s":
                print("You find many small houses at a distance. You reach there and are greeted by dwarfs. They give you the shelter and at night you overhear them whispering about moving the treasure. When they're fast asleep, you hunt the houses and find the treasure int the cellar. You steal it and run away. You win. But you have very bad manners of eavesdropping and stealing. Shame on you.")
            else:
                print("You try to rest under a big tree but at night you're attacked by the same witch and she doesnt spare you this time. Game over.")
    elif fight == "Cauldrom":
        key = input("You easily defeat the witch by injuring her on the head with the cauldron. You see a key tied to her pendant. It could either be helpful for finding the treasure or could be cursed. What do you choose? Take it or Leave it: ")
    else:
        print("It backfired. The witch used a sword to harm you. Game over.")