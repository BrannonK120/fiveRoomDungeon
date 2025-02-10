import random, os, time

wepon = None
fight1 = True
fight2 = True
room2left = True
room1 = True
room2 = True
lockpicking1 = True
ability = None
item = None
Mainstat = None
counter1 = 0
counter2 = 0
platform = True
counter3 = 10
attempt = 0
item2 = None
abilityon = True
flee = random.randint(1, 10)
damage = random.randint(1, 8)
isplayingroom1 = True
isplayingroom2 = True
skeltonhealth = 30
skeltonguardhealth = 75
skeltonguardamage = 20
skeltonbosshealth = 125
abiltycounter = 0
skeltondamage = 5
skeltonguradamage = 20
skeltonbossdamage = 25
bossfight = True
classall = None
fight3 = True
indugen = True
Platform = True
fight4 = True
action4 = True
magicdamage = random.randint(1, 15)
blanket = None
room2right = True
potion = None
beaten = None
backroundstory = None
skeltonhealth2 = 30
story = None
weponname = None
blanketname = None
backroundname = None

strength = 10
constitution = 100
wisdom = 10
dexterity = 10
Intelligence = 10
chrisma = 0
print("Name your legend")


def diceroll1(times):
    diceroll2 = random.randint(1, 2)
    diceroll3 = random.randint(1, 10)
    result = (diceroll2 * diceroll3) + 10
    return result


def charatersheet():
    print()
    print(name1, "the almighty")
    print()
    print("Background:", backroundname)
    print()
    print("Class:", classall)
    print()
    print("Special ability", ability)
    print()
    print("Stats:")
    print("Strength:", strength)
    print("Health:", constitution)
    print("Wisdom:", wisdom)
    print("Dexterity:", dexterity)
    print("Intelligence:", Intelligence)
    print("Items:")
    print("Unilty:", item, )
    print("Potion:", item2)
    print("Wepon:", weponname, )
    print("Other:", blanketname, )


name1 = input("What is you name going to be? : ")
chartertype = input("""What charter type would you like to be"
1. Orc:Orcs specialize in melee combat they have high strength and high dexterity, but are low health
2. Elf:Elves specialize in magic. They are low in health and low in strength and high in intelligence and dexterity
3. Human: Humans are midrange in all categories but looks
4. Dwarf: Dwarfs are short but mighty they use melee combat they have mid damage and are high and health, and strength
What would you like to be? :""")
time.sleep(2)
os.system("clear")

print("1.Fighter")
print("2.Rouge")
print("3.Wizard")
print("4.Cleric")
classes = input("What class do you want to be each class has its own special ability?!! :")
time.sleep(2)
os.system("clear")

print("1.Assassin")
print("2.Farmhand")
print("3.Gambler")
print("4.Scholar")
print("5.Warrior")
background = input("What do you want your background to be?!! ")

if chartertype == "1":
    constitution -= 15
    strength += 5
    dexterity += 5

if chartertype == "2":
    constitution -= 15
    Intelligence += 5
    dexterity += 5

if chartertype == "4":
    constitution += 15
    strength += 5
    dexterity += 5

if classes == "1":
    strength += 5
    ability = "Rage"
    Mainstat = strength
    classall = "Fighter"

if classes == "3":
    Intelligence += 5
    ability = "Enlightment"
    Mainstat = Intelligence
    classall = "Wizard"

if classes == "4":
    wisdom += 5
    ability = "Healer"
    Mainstat = wisdom
    classall = "Cleric"

if classes == "2":
    dexterity += 5
    ability = "Weakening"
    Mainstat = dexterity
    classall = "Rouge"

if background == "3":
    wisdom += 5
    backroundstory = "money to gamble away"
    backroundname = "Gamabler"

if background == "2":
    constitution += 5
    backroundstory = "you to buy food for your cattle"
    backroundname = "Farmhand"

if background == "1":
    Intelligence += 5
    backroundstory = "your daughter to be able to go to school"
    backroundname = "Assassin"

if background == "5":
    strength += 5
    backroundstory = "some extra cash for some expisve armor"
    backroundname = "Warrior"

if background == "4":
    Intelligence += 5
    backroundstory = "your edcation because school is exensive"
    backroundname = "Soholar"

time.sleep(2)
os.system("clear")
print()
print(name1, "the almighty")
print()
print("Background:", backroundname)
print()
print("Class:", classall)
print()
print("Special ability", ability)
print()
print("Stats:")
print("Strength:", strength)
print("Health:", constitution)
print("Wisdom:", wisdom)
print("Dexterity:", dexterity)
print("Intelligence:", Intelligence)

print("To make some extra cash you go out adventing slaying and killing monster in the enchancted rose woodlands for",
      backroundstory, )
print(
    "After adventuring all day killing monsters skinning them for their resoures and the sun starts to go down and it starts to become dark.")
print(
    "As it becomes dawn you start to leave the forest and you see a giant hill. You become curious and walk up the hill to see a massive castle you walk back inmto teh forest to contuine fighting monsters.")
print(
    "As it starts to become dark monster start to chase you and you find yourself back at the giant hill and decide to run to the massive castle to shelter from the monsters chasing after you.")
print(
    "As you run towards the castle you see a dark ementing aura and you realizes the many times that you have come to this forest you have never seen this castle before. But you dissmie the thought from your mind and coniune to run towards the caslte")
print(
    "You slame the door shut and the monster crash into the door knocking them out as you turn around a faint light to your left and a spiral stair case to your right.")
print("When you look forward you again get the same chill and uneasy feeling you look up its another room.")
time.sleep(10)
os.system("clear")
print("""Game instrctions:
You will have the ability to move in three direction on every floor. In every room you will have the ability to see a chartersheet that display items and stats. 
In combact chose a number as you attack and latstly chose only number and when its a letter only upper case. That is all have fun with my game :)""")

while room1:
    doorways = input("Where do you want to go? R/F/L :")
    if doorways == "L":
        print("You walk to the room on the left and walk inside. It's an empty room with only a bed and a lit torch.")
        isplayingroom1 = True
        while isplayingroom1:
            action1 = input("""
    1.Inspect the bed
    2.Take the torch
    3.Walk out
    4.See charatersheet  :""")
            if action1 == "1":
                print(
                    "You inspect the bed and find a blanket ,and decided to put it on because you have a feeling it will be very useful later +5 health")
                constitution += 5
                blanket = True
                blanketname = "Blanket"


            elif action1 == "2":
                print("You pick up the torch this could be useful and lights up the room")
                item = "Torch"

            elif action1 == "3":
                print("You leave the room")
                isplayingroom1 = False

            elif action1 == "4":
                charatersheet()

    elif doorways == "R" and item == "Torch":
        print(
            "You walk down a dark stair case but your torch lights the stairwell and you see a tripwire you step over it and enter Room 2")
        room1 = False




    elif doorways == "R" and item == None:
        print("You walk down a dark staircase and trip on a tripwire and arrows come at you. You lose ten health")
        constitution -= 10
        room1 = False

    if doorways == "F" and story == True:
        print(
            "You walk into the room and get your body feels cold you leave the room after you fell your body start to freeze")
    if doorways == "F" and story == None:
        story = True
        print("""You walk foward into a room and he air in the dimly lit dungeon room grows colder as the heavy iron door creaks open. From the shadows, the Grim Reaper emerges, his skeletal form shrouded in a flowing black cloak."
    The soft rustle of his robes and the chilling sound of his scythe scraping the stone floor send shivers down your spine. His hollow eyes, burning with an otherworldly light, lock onto yours, and the room seems to grow even darker."
    The only sound now is the distant drip of water and the echo of your own heartbeat, pounding in your ears."
    The Reaper raises his massive scythe, the blade glinting ominously, and you know that your next move could be your last."
    Courage musters within you as you prepare to face this harbinger of death, knowing that the fate of your quest hangs in the balance but before you could attack the grim reaper goes into the wall and you fell the chillening aura leave""")
        time.sleep(10)
        os.system("clear")

time.sleep(3)
os.system("clear")
print(
    "In room 2 you see a door in front of you with a big and tall skeleton and it looks like it is guarding the door. He might let you by if you trade something to him. You also see two doors one on your left one on your right. ")
while room2:
    doorways2 = input("Where do you want to go? R/L/F : ")
    if doorways2 == "L":
        print("You see a skeleton and it charges at you")
        while fight1:
            diceroll20 = random.randint(1, 20)
            if diceroll20 + dexterity >= 25:
                print("""
    Health:""", constitution
                      , )
            fightingaction1 = input("""What do you want to do?
    1.Attack
    2.Magic attack
    3.Item
    4.Flee
    5.Special Ability : """)

            if constitution <= 0:
                print("You are not alive sorry")
                fight1 = False
                constitution = 0
                diceroll20 = 25


            elif fightingaction1 == "1":
                skeltonhealth2 -= damage + strength
                if skeltonhealth2 <= 0:
                    print("You have vanished the skeleton it collapses into a pile of bones")
                    fight1 = False
                else:
                    print("You attack the skeleton the skeleton. The skeleton has", skeltonhealth2, "health left")




            elif fightingaction1 == "2":
                skeltonhealth2 -= magicdamage + Intelligence
                if skeltonhealth2 <= 0:
                    print("You have vanished the skeleton it collapses into a pile of bones")
                    fight1 = False
                else:
                    print("You use a magic attack the skeleton has", skeltonhealth2, "health left")




            elif fightingaction1 == "3" and item2 == None:
                print("You have no items")


            elif fightingaction1 == "3" and item2 == "Healthpotion":
                print("You use the health potion you restore 25 health")
                constitution += 25


            elif fightingaction1 == "4":
                if flee > 5:
                    print("You're lucky you escape from the room")
                    fight1 = False
                    diceroll20 = 25
                elif flee <= 5:
                    print("You trip on air and you see a flyer to join Woonsocket WACTCC tech center")


            elif fightingaction1 == "5" and ability == "Rage":
                strength *= .20
                abiltycounter += 1
                print("You use your special ability rage. Boost your strength by 20 percent ")


            elif fightingaction1 == "5" and ability == "Healer":
                constitution += 25
                abiltycounter += 1
                print("You use you special ability healing. It restores 25 heath points")


            elif fightingaction1 == "5" and ability == "Enlightenment":
                Intelligence *= .20
                abiltycounter += 1
                print("You use your special ability Enlightment. Boost intelligence by 20 percent")


            elif fightingaction1 == "5" and ability == "Weakening":
                skeltondamage = 3
                skeltonguradamage = 10
                skeltonbossdamage = 13
                abiltycounter += 1
                print("You use you special ability Weakening. Weakening decreaseing all emmenys damage by 50 percent.")

            elif diceroll20 <= 15:
                constitution -= skeltondamage
                print("The skeleton attacks you and does", skeltondamage, "you have", constitution, "left")

                if skeltonhealth <= 0:
                    fight1 = False
                    print("After defeating the skeleton you look around and see a big chest with a lock on it ")
                    diceroll20 = 25

                if constitution <= 0:
                    print("You are not alive sorry")
                    fight1 = False
                    diceroll20 = 25



        room2left = True
        while room2left:
            action2left = input("""
    1.Go to the chest
    2.Leave the room
    3.Charatersheet:""")
            lockpick2 = random.randint(1, 20) + Intelligence
            if action2left == "1" and wepon == None:
                print(
                    "You walk over to the chest it lock you will need to lockpick it this will require intelligence")
                if lockpick2 >= 15:
                    print(
                        "You open the chest and inside is a shiny weapon that appears to be made of bones and a dark material (it does plus 10 damage) ")
                    Mainstat += 10
                    wepon = True
                    weponname = "Nighterbrigher"
                else:
                    print("You try to open the but your lockpick break and so does your ego. Try again")


            elif action2left == "1" and wepon == "True":
                print("You have already opened the chest")

            elif action2left == "2":
                print("You leave the room")
                room2left = False
                fight1 = False
                abilityon = False


            elif action2left == "3":
                charatersheet()

    elif doorways2 == "R":
        print("You enter the room on the right and there is nothing but a chest and a torch")
        print("A skelton charges at you from the dark")
        while fight3:
            diceroll23 = random.randint(1, 20)
            if diceroll23 + dexterity >= 25:
                print("""
    Health:""", constitution
                      , )
                fightingaction2 = input("""What do you want to do?
    1.Attack
    2.Magic attack
    3.Item
    4.Flee
    5.Special Ability : """)
                if fightingaction2 == "1":
                    skeltonhealth -= damage + Mainstat
                    if skeltonhealth <= 0:
                        print("You have vanquish the skelton it collapes into a pile of bones")
                    else:
                        print("You attack the skeleton has", skeltonhealth, "health left")

                elif fightingaction2 == "2":
                    skeltonhealth -= magicdamage + Intelligence
                    if skeltonhealth <= 0:
                        print("You have vanshied the skelton it collapes into a pile of bones")
                    else:
                        print("You attack the skeleton has", skeltonhealth, "health left")


                elif fightingaction2 == "3" and item2 == None:
                    print("You have no items")

                elif fightingaction2 == "3" and item2 == "Healthpotion":
                    print("You use the health potion you restore 25 health")
                    constitution += 25

                elif fightingaction2 == "4":
                    if flee >= 5:
                        print("You're lucky you escape from the room")
                        fight3 = False
                    else:
                        print("You're too slow ahhahahahh")


                elif fightingaction2 == "5" and ability == "Rage":
                    strength * .20
                    abiltycounter += 1
                    print("You use you special ability Rage. It boost you strength by 20 percent ")




                elif fightingaction2 == "5" and ability == "Healer":
                    constitution + 25
                    abiltycounter += 1
                    print("You use your special ability Healing. You restore 25 health points")




                elif fightingaction2 == "5" and ability == "Enlightenment":
                    Intelligence * .20
                    abiltycounter += 1
                    print("You use your special ability Enlightenment. You boost you intelligence by 20 percent")




                elif fightingaction2 == "5" and ability == "Weakening":
                    skeltondamage = 3
                    skeltonguradamage = 10
                    skeltonbossdamage = 13
                    abiltycounter += 1
                    print("You use your special ability weakening. It weakens all emmenys damage by 50 percent.")


            elif diceroll23 <= 15:
                constitution -= skeltondamage
                print("The skelton attacks you and does", skeltondamage, "you have", constitution, "left")

            if skeltonhealth <= 0:
                fight3 = False
                skeltonhealth = 0
                print("After defeating the skeleton you look around and see a big chest with a lock on it ")

            if constitution <= 0:
                print("You are not alive sorry")
                fight3 = False
                constitution = 0


        room2right = True
        while room2right:
            action2left = input("""
    1.Go to the chest
    2.Leave the room
    3.See charatersheet:""")
            lockpick2 = random.randint(1, 20) + Intelligence
            if action2left == "1":
                print(
                    "You walk over to the chest it lock you will need to lockpick it this will require intellgenece")
                if lockpick2 > 15:
                    print(
                        "You open the chest and inside is a health potion it restores 25 health points ")
                    item2 = "Healthpotion"
                else:
                    print("You attempt to open the chest but fail and leave the room because it hurt your ego")
                    room2left = False
                    abilityon = False

            if action2left == "2":
                print("You leave the room")
                room2right = False
                abilityon = False

            if action2left == "3":
                charatersheet()




    elif doorways2 == "F":
        print("You walk forward to the skeleton and the giant door")
        action3 = input("""What do you want to do
    1.Trading with him
    2.Attack the skeleton guard
    3.Sneak around the skeleton guard : """)
        if action3 == "1" and wepon == True:
            print("You trade him the weapon he opens the door and it leads to the boss room")
            beaten = True
            Mainstat -= 10
            while bossfight:
                diceroll22 = random.randint(1, 20)
                if diceroll22 + dexterity >= 25:
                    print("""
            Health:""", constitution)
                    fightingaction3 = input("""What do you want to do?
            1.Attack
            2.Magic attack
            3.Item
            4.Flee
            5.Special Ability : """)
                    if fightingaction3 == "1":
                        skeltonbosshealth -= damage + Mainstat
                        print("You attack the skeleton the skeleton has ", skeltonbosshealth, "health left")
                        if skeltonbosshealth <= 0:
                            bossfight = False
                            room2 = False
                            print("After defeating the Grim Reaper you look around and see a door emitting an aura ")
                            final = input("Do you want to want to walk through the door. Y/N")
                            if final == "N":
                                print(
                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                            if final == "Y":
                                print("You enter the door and you see a beautiful landscape it amazing.")
                                jump = input("Do you want to explore Y/N")
                                if jump == "Y" and blanket == "True":
                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                if jump == "Y" and blanket == "None":
                                    print(
                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                if jump == "N":
                                    print(
                                        "You sit on the top ledge near the door and stare at the beautiful landscape")
                        if constitution <= 0:
                            print("You have fallen in combat")
                            room2 = False


                    elif fightingaction3 == "2":
                        skeltonbosshealth -= damage + Intelligence
                        print("You use a magic attack the skeleton has", skeltonbosshealth, "health left")
                        if skeltonbosshealth <= 0:
                            bossfight = False
                            room2 = False
                            print("After defeating the Grim Reaper you look around and see a door emitting an aura ")
                            final = input("Do you want to want to walk through the door. Y/N")
                            if final == "N":
                                print(
                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                            if final == "Y":
                                print("You enter the door and you see a beautiful landscape it amazing.")
                                jump = input("Do you want to explore Y/N")
                                if jump == "Y" and blanket == True:
                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                if jump == "Y" and blanket == None:
                                    print(
                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                if jump == "N":
                                    print(
                                        "You sit on the top ledge near the door stare at the beautiful landscape")
                        if constitution <= 0:
                            print("You have fallen in combat")
                            room2 = False


                    elif fightingaction3 == "3" and item2 == None:
                        print("You have no items")


                    elif fightingaction3 == "3" and item2 == "Healthpotion":
                        print("You use the health potion you restore 20 health")
                        constitution += 20


                    elif fightingaction3 == "4":
                        print("You cant escape the boss room")


                    elif fightingaction3 == "5" and ability == "Rage":
                        strength * .20
                        abiltycounter += 1
                        print("You use your speical ability rage. Boost strength by 20 percent. ")


                    elif fightingaction3 == "5" and ability == "Healer":
                        constitution += 25
                        abiltycounter += 1
                        print("You use your speical ablity healing. You restore 25 hit points.")


                    elif fightingaction3 == "5" and ability == "Enlightenment":
                        Intelligence * .20
                        abiltycounter += 1
                        print("You use your speical ability Enlightenment. Boost your Intelligence by 20 percent.")


                    elif fightingaction3 == "5" and ability == "Weakening":
                        skeltondamage = 3
                        skeltonguradamage = 10
                        skeltonbossdamage = 13
                        abiltycounter += 1
                        print("You use you speical ability weakening. Decreases all emmenys damage by 50 percent.")

                    elif skeltonbosshealth == 0:
                        print("You defeated the great grim reaper")
                        bossfight = False
                        print("After defeating the Grim Reaper you look around and see a door emitting an aura")


                    elif constitution == 0:
                        print("You are not alive sorry")
                        bossfight = False

                if diceroll22 + dexterity <= 24:
                    constitution -= skeltonbossdamage
                    print("The grim reaper attacks you and does", skeltonbossdamage, " damage you have", constitution, "left")
                    if constitution <= 0:
                        print("You have fallen in combat")
                        bossfight = False
                        room2 = False
                    if skeltonbosshealth <= 0:
                        bossfight = False
                        print("After defeating the Grim Reaper you look around and see a door emitting an aura ")
                        final = input("Do you want to want to walk through the door. Y/N:")
                        if final == "N":
                            print(
                                "You don't walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                        if final == "Y":
                            print("You enter the door and you see a beautiful landscape it amazing.")
                            jump = input("Do you want to explore Y/N:")

                            if jump == "Y" and blanket == True:
                                print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                            if jump == "Y" and blanket == None:
                                print("You jump but fall on your head making you go to sleep on the beautiful grass")

                            if jump == "N":
                                print("You sit on top of the ledge and stare at the beautiful sunset")

        if action3 == "1" and wepon == None:
            print("You have nothing of value to offer")

        if action3 == "2":
            while fight4:
                diceroll23 = random.randint(1, 20)
                if diceroll23 + dexterity >= 25:
                    print("""
            Health:""", constitution
                          , )
                    fightingaction4 = input("""What do you want to do?
            1.Attack
            2.Magic attack
            3.Item
            4.Flee
            5.Special Ability : """)
                    if fightingaction4 == "1":
                        skeltonguardhealth -= damage + Mainstat
                        if skeltonguardhealth <= 0:
                            print(
                                "You have vanquish the skeleton guard and it turns to dust. The giant door it was guarding opens ")
                            fight4=False
                            beaten = True
                            print("You enter the boss room and the Grim Reaper charges at you ")
                            while bossfight:
                                diceroll22 = random.randint(1, 20)
                                if diceroll22 + dexterity >= 25:
                                    print("""
                            Health:""", constitution)
                                    fightingaction3 = input("""What do you want to do?
                            1.Attack
                            2.Magic attack
                            3.Item
                            4.Flee
                            5.Special Ability : """)
                                    if fightingaction3 == "1":
                                        skeltonbosshealth -= damage + Mainstat
                                        print("You attack the Grim Reaper the skeleton has ", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N")
                                                if jump == "Y" and blanket == "True":
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == "None":
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door and stare at the beautiful landscape")
                                    elif fightingaction3 == "2":
                                        skeltonbosshealth -= damage + Intelligence
                                        print("You use a magic attack the Grim Reaper has", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N")
                                                if jump == "Y" and blanket == True:
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == None:
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door stare at the beautiful landscape")
                                        if constitution <= 0:
                                            print("You have fallen in combat")
                                            room2 = False


                                    elif fightingaction3 == "3" and item2 == None:
                                        print("You have no items")


                                    elif fightingaction3 == "3" and item2 == "Healthpotion":
                                        print("You use the health potion you restore 20 health")
                                        constitution += 20


                                    elif fightingaction3 == "4":
                                        print("You cant escape the boss room")


                                    elif fightingaction3 == "5" and ability == "Rage":
                                        strength * .20
                                        abiltycounter += 1
                                        print("You use your speical abilty Weakening. Boost strength by 20 percent")

                                    elif fightingaction3 == "5" and ability == "Healer":
                                        constitution += 25
                                        abiltycounter += 1
                                        print("You use your speical abilty healing. Restore 25 health points ")


                                    elif fightingaction3 == "5" and ability == "Enlightenment":
                                        Intelligence * .20
                                        abiltycounter += 1
                                        print("You use your speical abilty Enlightenmenmt. boost Intelligence by 20 percent.")


                                    elif fightingaction3 == "5" and ability == "Weakening":
                                        skeltondamage = 3
                                        skeltonguradamage = 10
                                        skeltonbossdamage = 13
                                        abiltycounter += 1
                                        print("You use your speical abilty Weakening. Decreases all emmeny damage by 50 percent")


                                    elif skeltonbosshealth == 0:
                                        print("You defeated the great grim reaper")
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura")


                                    elif constitution == 0:
                                        print("You are not alive sorry")
                                        bossfight = False

                                if diceroll22 + dexterity <= 24:
                                    constitution -= skeltonbossdamage
                                    print("The Grim Reaper attacks you and does", skeltonbossdamage, " damage you have",
                                          constitution, "left")
                                    if constitution <= 0:
                                        print("You have fallen in combat")
                                        bossfight = False
                                        room2 = False
                                    if skeltonbosshealth <= 0:
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                        final = input("Do you want to want to walk through the door. Y/N:")
                                        if final == "N":
                                            print(
                                                "You don't walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                        if final == "Y":
                                            print("You enter the door and you see a beautiful landscape it amazing.")
                                            jump = input("Do you want to explore Y/N:")

                                            if jump == "Y" and blanket == True:
                                                print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                            if jump == "Y" and blanket == None:
                                                print(
                                                    "You jump but fall on your head making you go to sleep on the beautiful grass")

                                            if jump == "N":
                                                print("You sit on top of the ledge and stare at the beautiful sunset")


                    elif fightingaction4 == "2":
                        skeltonguardhealth -= magicdamage + Intelligence
                        if skeltonguardhealth <= 0:
                            print(
                                "You have vanished the skeleton guard it turns into dust the giant door it was guarding opens")
                            fight4 = False
                            beaten = True
                            print("You defeat the skelto9n guard the door opens and you enter the boss room. You see the Grim Reaper he turns around and charges at you ")
                            while bossfight:
                                diceroll22 = random.randint(1, 20)
                                if diceroll22 + dexterity >= 25:
                                    print("""
                            Health:""", constitution)
                                    fightingaction3 = input("""What do you want to do?
                            1.Attack
                            2.Magic attack
                            3.Item
                            4.Flee
                            5.Special Ability : """)
                                    if fightingaction3 == "1":
                                        skeltonbosshealth -= damage + Mainstat
                                        print("You attack the Grim Reaper the Grim Reaper has ", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N :")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N :")
                                                if jump == "Y" and blanket == "True":
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == "None":
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door and stare at the beautiful landscape")
                                        if constitution <= 0:
                                            print("You have fallen in combat")
                                            room2 = False


                                    elif fightingaction3 == "2":
                                        skeltonbosshealth -= damage + Intelligence
                                        print("You use a magic attack the Grim Reaper has", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N :")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N :")
                                                if jump == "Y" and blanket == True:
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == None:
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door stare at the beautiful landscape")
                                        if constitution <= 0:
                                            print("You have fallen in combat")
                                            room2 = False


                                    elif fightingaction3 == "3" and item2 == None:
                                        print("You have no items")


                                    elif fightingaction3 == "3" and item2 == "Healthpotion":
                                        print("You use the health potion you restore 20 health")
                                        constitution += 20


                                    elif fightingaction3 == "4":
                                        print("You cant escape the boss room")


                                    elif fightingaction3 == "5" and ability == "Rage":
                                        strength * .10
                                        abiltycounter += 1


                                    elif fightingaction3 == "5" and ability == "Healer":
                                        constitution += 25
                                        abiltycounter += 1


                                    elif fightingaction3 == "5" and ability == "Enlightenment":
                                        Intelligence * .10
                                        abiltycounter += 1


                                    elif fightingaction3 == "5" and ability == "Weakening":
                                        skeltondamage = 3
                                        skeltonguradamage = 10
                                        skeltonbossdamage = 13
                                        abiltycounter += 1
                                    elif abiltycounter == "3":
                                        abilityon = False


                                    elif skeltonbosshealth == 0:
                                        print("You defeated the great grim reaper")
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura")


                                    elif constitution == 0:
                                        print("You are not alive sorry")
                                        bossfight = False

                                if diceroll22 + dexterity <= 25:
                                    constitution -= skeltonbossdamage
                                    print("The grim reaper attacks you and does", skeltonbossdamage, "you have",
                                          constitution, "left")
                                    if constitution <= 0:
                                        print("You have fallen in combat")
                                        bossfight = False
                                        room2 = False
                                    if skeltonbosshealth <= 0:
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                        final = input("Do you want to want to walk through the door. Y/N:")
                                        if final == "N":
                                            print(
                                                "You don't walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                        if final == "Y":
                                            print("You enter the door and you see a beautiful landscape it amazing.")
                                            jump = input("Do you want to explore Y/N:")

                                            if jump == "Y" and blanket == True:
                                                print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                            if jump == "Y" and blanket == None:
                                                print(
                                                    "You jump but fall on your head making you go to sleep on the beautiful grass")

                                            if jump == "N":
                                                print("You sit on top of the ledge and stare at the beautiful sunset")



                    elif fightingaction4 == "3" and item2 == None:
                        print("You have no items")


                    elif fightingaction4 == "3" and item2 == "Healthpotion":
                        print("You use the health potion you restore 25 health")
                        constitution += 25



                    elif fightingaction4 == "4":
                        if flee > 5:
                            print("You're lucky you escape from the room")
                            fight4 = False
                        else:
                            print("You're too slow ahhahahahh")

                    elif fightingaction4 == "5" and ability == "Rage":
                        strength * .20
                        abiltycounter += 1
                        print("You use your special ability rage. Boost damage by 20 percent.")




                    elif fightingaction4 == "5" and ability == "Healer":
                        constitution += 25
                        abiltycounter += 1
                        print("You use your special ability healing. You restore 25 health")




                    elif fightingaction4 == "5" and ability == "Enlightenment":
                        Intelligence * .20
                        abiltycounter += 1
                        print("You use your special ability Enlightenment. Boost intelligence by 20 percent.")

                    elif fightingaction4 == "5" and ability == "Weakening":
                        skeltondamage = 3
                        skeltonguradamage = 10
                        skeltonbossdamage = 13
                        abiltycounter += 1
                        print("You use your special ability wakening. It lower all emmenys damage by 50 percent.")


                elif diceroll23 <= 15:
                    constitution -= skeltondamage
                    print("The skeleton attacks you and does", skeltondamage, "you have", constitution,
                          "left")

        if action3 == "3":
            sneakingarud = random.randint(1, 20) + Intelligence
            if sneakingarud >= 25:
                print("You sneak around the guard and enter the the next room but its a hallway")
                print(
                    "At the end of the hallway you reach a another room its just an empty room you take a step forward all the floor breaks and falls expect for 5 pieces(Guess a number between 1 and 5 and if you get it right you move on to the next platform if not you lose an attempt you only get 10 attempts if you miss all of them you lose 20 health ")
                while Platform:
                    platformgeuss = random.randint(1, 3)
                    platform1 = input("Guess a number between 1 and 3 :")
                    if platformgeuss == platform1:
                        print("You move on to the next platform")
                        counter3 -= 1
                    else:
                        print("You didn't guess right you use one attempt. You have" ,attempt,"tries left")
                        attempt += 1
                        if attempt >= 10:
                            print(
                                "You fall onto the spikes losing 20 health and knock out waking back up in the second room")
                            Platform = False
                            beaten = True
                        if counter3 == 3:
                            print("You jump on all the platforms and move into the boss room ")
                            beaten = True
                            while bossfight:
                                diceroll22 = random.randint(1, 20)
                                if diceroll22 + dexterity >= 25:
                                    print("""
                            Health:""", constitution)
                                    fightingaction3 = input("""What do you want to do?
                            1.Attack
                            2.Magic attack
                            3.Item
                            4.Flee
                            5.Special Ability : """)
                                    if fightingaction3 == "1":
                                        skeltonbosshealth -= damage + Mainstat
                                        print("You attack the skeleton the skeleton has ", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N :")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N :")
                                                if jump == "Y" and blanket == "True":
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == "None":
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door and stare at the beautiful landscape")
                                        if constitution <= 0:
                                            print("You have fallen in combat")
                                            room2 = False


                                    elif fightingaction3 == "2":
                                        skeltonbosshealth -= damage + Intelligence
                                        print("You use a magic attack the skeleton has", skeltonbosshealth,
                                              "health left")
                                        if skeltonbosshealth <= 0:
                                            bossfight = False
                                            room2 = False
                                            print(
                                                "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                            final = input("Do you want to want to walk through the door. Y/N :")
                                            if final == "N":
                                                print(
                                                    "You dont walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                            if final == "Y":
                                                print(
                                                    "You enter the door and you see a beautiful landscape it amazing.")
                                                jump = input("Do you want to explore Y/N :")
                                                if jump == "Y" and blanket == True:
                                                    print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                                if jump == "Y" and blanket == None:
                                                    print(
                                                        "You jump but fall on your head making you go to sleep on the beautiful grass")

                                                if jump == "N":
                                                    print(
                                                        "You sit on the top ledge near the door stare at the beautiful landscape")
                                        if constitution <= 0:
                                            print("You have fallen in combat")
                                            room2 = False


                                    elif fightingaction3 == "3" and item2 == None:
                                        print("You have no items")


                                    elif fightingaction3 == "3" and item2 == "Healthpotion":
                                        print("You use the health potion you restore 20 health")
                                        constitution += 20


                                    elif fightingaction3 == "4":
                                        print("You cant escape the boss room")


                                    elif fightingaction3 == "5" and ability == "Rage":
                                        strength * .20
                                        abiltycounter += 1
                                        print("You use your speical abilty Rage. Boost strength by 20 percent.")


                                    elif fightingaction3 == "5" and ability == "Healer":
                                        constitution += 25
                                        abiltycounter += 1
                                        print("You use your speical abilty Healing. Restores 25 health points")


                                    elif fightingaction3 == "5" and ability == "Enlightenment":
                                        Intelligence * .20
                                        abiltycounter += 1
                                        print("You use your speical abilty Enlightenment. Boost Intelligence by 20 percent")


                                    elif fightingaction3 == "5" and ability == "Weakening":
                                        skeltondamage = 3
                                        skeltonguradamage = 10
                                        skeltonbossdamage = 13
                                        abiltycounter += 1
                                        print("You use your speical abilty Weakening. Decreases all emmeny damage by 50 percent")


                                    elif skeltonbosshealth == 0:
                                        print("You defeated the great grim reaper")
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura")


                                    elif constitution == 0:
                                        print("You are not alive sorry")
                                        bossfight = False

                                if diceroll22 + dexterity <= 25:
                                    constitution -= skeltonbossdamage
                                    print("The grim reaper attacks you and does", skeltonbossdamage, " damage you have",
                                          constitution, "left")
                                    if constitution <= 0:
                                        print("You have fallen in combat")
                                        bossfight = False
                                        room2 = False
                                    if skeltonbosshealth <= 0:
                                        bossfight = False
                                        print(
                                            "After defeating the Grim Reaper you look around and see a door emitting an aura ")
                                        final = input("Do you want to want to walk through the door. Y/N:")
                                        if final == "N":
                                            print(
                                                "You don't walk through the door and go back home returning to your normal life never forgetting the dungeon.")

                                        if final == "Y":
                                            print("You enter the door and you see a beautiful landscape it amazing.")
                                            jump = input("Do you want to explore Y/N:")

                                            if jump == "Y" and blanket == True:
                                                print("You use the blanket to fly down and run into the sun set. Turns out you were dying from cancer and this was you path. Your family burys you and morns you death. The end")

                                            if jump == "Y" and blanket == None:
                                                print(
                                                    "You jump but fall on your head making you go to sleep on the beautiful grass")

                                            if jump == "N":
                                                print("You sit on top of the ledge and stare at the beautiful sunset")
                            
                                if sneakingarud <= 29:
                                                print("You try to jump to the next platform but are unsuccessful")
            if sneakingarud<=24:
                print("Dont test me mortal. Don't cheat your trial")
