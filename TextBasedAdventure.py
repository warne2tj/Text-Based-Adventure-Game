"""
Text Based Adventure Game
"""
#These are import statements. They are used to include extra functions used for the program.
#Declare them at the top, and you'll always know where to find them
import time
import os
import random
import sys




""" GLOBAL VARAIBLES """

#Character Attributes
health = 100
intelligence = 10
strength = 10
dexterity = 10
charisma = 10


#Character and Map Booleans
has_health_potion = False
has_strength_potion = False
treasure_location = random.randint(1, 4)
has_shield = False
visited_cave = False
visited_beach = False





""" FUNCTION DECLARATIONS """

"""
format_console method - This command is going to format the console to the dimensions
that we want, as well as the background and text color. You can use this to change the
color of the text and/or background midgame. But I'll let you figure that out.
"""
def format_console():
    os.system('mode con: cols=175 lines=50')
    os.system('color 20')
"""

Clear method - This is how you can clear the text from the screen. Just type clear().
"""
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

"""
clean_input method - This is how we are going to make sure that responses are numbers
and not text. Feel free to allow text based responses (yes/no) in your game. But you'll
have to figure it out.

If the text entered what a number, it will return that number in
integer form (because the user inputs text (a string), not an integer). If it the text
entered was a actual text (a string), return -1.
"""
def clean_input(response):
    try:
        response = int(response)
        return response
    except ValueError:
        return -1

def visit_cave():
    os.system('color 87')
    global visited_cave
    visited_cave = True
    response = 0
    clear()

    #Bat encounter
    print("As you approach the entrance of the cave, you hear squeaking coming from the cave.")
    time.sleep(2)
    print("... now you hear the sound of wings flapping..")
    input("Press enter to continue...")
    clear()
    time.sleep(1)
    print("A swarm of bats flies out of the cave, and they bite and scratch you as they swarm around you!")
    time.sleep(2)
    print("You have lost 5 hitpoints!")
    global health
    health = health - 10
    time.sleep(1)
    input("Press enter to continue...")
    clear()

    print("After the bats have flown off, you cautiously step foot into the cave.")
    time.sleep(2)
    print("It is so dark, you can't see your hand waving in front of your face.")
    input("Press enter to continue...")
    clear()

    response = 0
    while response < 1 or response > 2:
        if response == -1:
            input("You must select a number 1 through 2. (Press enter to continue..)")
            clear()
        print("You hear a low, deep rumbling that sounds like the ceiling of the cave is collapsing.")
        time.sleep(2)
        print("Would you like to enter the cave?\n")
        print("1. Yes, charge onward!")
        print("2. Probably best that I don't.")
        response = input("(Choose a number 1-2)")
        response = clean_input(response)
        if response < 1 or response > 2:
            response = -1

    clear()
    if response == 1:
        global has_health_potion
        has_health_potion = True
        print("You push onward into the cave, and before long, you kick something that sounds like glass...")
        time.sleep(2)
        print("You reach down and pick up the glass object.")
        time.sleep(1)
        input("Press enter to continue...")
        clear()
        print("You have found a heart shaped vial full of a thick, red liquid...")
        time.sleep(2)
        print("You have aquired 1 Health Potion!")
        time.sleep(1)
        input("Press enter to continue...")
        clear()
        print("You've found something useful, its probably best not to press your luck in this cave.")
        time.sleep(2)
        print("You turn around and head back towards the entrance of the cave.")
        input("Press enter to continue...")
        clear()
    if response == 2:
        print("You decide that it is best leave the collasping cave. Afterall, you like not having rocks crushing your lungs.")
        input("Press enter to continue...")
        clear()
    print("As you leave the cave, the entrance collaspses behind you, leaving the cave inaccessible.")
    time.sleep(2)
    input("You head back to the meadow. Press enter to continue...)")
    clear()
    location_selection()

def visit_beach():
    os.system('color 17')
    global visited_beach
    visited_beach = True
    clear()
    print("As you approach the beach, the wind picks up and the air is much cooler. You see a man standing on a sand dune near the water.")
    time.sleep(2)
    print("You walk towards the man, and he calls out to you...")
    time.sleep(2)
    input("Press enter to continue...")
    clear()
    print('"Hello traveler. You see the three areas in the sand in front of us? One of those contains buried treasure. But you can only pick one."')
    time.sleep(2)
    input('"The sand is loose from the waves, and will cause the other areas to sink back into the ocean." (Press enter to continue...)')
    clear()
    response = 0
    while response < 1 or response > 4:
        if response == -1:
            input("You must select a number 1 through 4. (Press enter to continue..)")
            clear()
        print("Which area would you like to choose?\n")
        print("1. Area one")
        print("2. Area two")
        print("3. Area three")
        print("4. Area four")
        response = input()
        response = clean_input(response)
        clear()
    global treasure_location
    if response == treasure_location:
        print("As you dig the hole, you shovel hits something solid!")
        time.sleep(1)
        print("You reach down, and you pull up a heavy, oak treasure chest. You open the chest and sift through the junk until you find something useful.")
        time.sleep(2)
        input("Press enter to continue...")
        clear()
        print("You found a fist shaped vial with a thick, blue liquid...")
        time.sleep(2)
        print("You have aquired 1 Strength Potion!")
        global has_strength_potion
        has_strength_potion = True
        time.sleep(1)
        input("Press enter to continue...")
        clear()
    else:
        print("You dig in the hole, and you find nothing.")
        time.sleep(1)
        input("Press enter to continue...")
        clear()
    print("As you climb out of the hole you dug, you feel the earth shift, and you know the other treasure areas have sunk back into the ocean.")
    time.sleep(2)
    print("You decide it is best to leave the beach and continue on your journey.")
    time.sleep(2)
    input("Press enter to continue...")
    clear()
    location_selection()


def visit_marrow():
    clear()
    os.system('color 87')
    print("You follow the path that leads to the City of Marrow. After a while, you can see the large, stone walls and the tall, wooden draw-bridge.")
    time.sleep(2)
    print("As you approach the gates, a guard begins to make his way toward you. He doesn't look too happy...")
    time.sleep(2)
    input("Press enter to continue...")
    clear()
    print('"Who goes there?"')
    time.sleep(2)
    print('"Ha! I don\'t care! The city is closed, unless you have some shiny gold pieces that say otherwise..."')
    input("Press enter to continue...")
    clear()
    print('"You don\'t have any gold? Fine, then my fighting skills could use some practice!"')
    time.sleep(2)
    print('"If you beat me in a duel, you can enter the city."')
    time.sleep(1)
    input("Press enter to continue...")
    clear()

    guard_health = 135
    third_round_special = 0
    defending = False
    while True:
        global has_health_potion
        global dexterity
        global health
        global strength
        global has_strength_potion
        global has_shield

        response = 0
        #Dexterity is too low, guard attacks first
        if dexterity <= 10:
            #calculate damage received
            damage_received = calculate_guard_damage(third_round_special, defending)
            if third_round_special == 3:
                third_round_special = 0
            #Player recieves damage, check if they are dead.\
            print("The guard deals " + str(damage_received) + " damage!")
            health = health - damage_received

            if health <= 0:
                input("Press enter to continue...")
                clear()
                if has_health_potion:
                    health = 100
                    input("Your strength has run out, but before you breathe your last breath, you drink your health potion and are fully restored! (Press enter to continue...)")
                    clear()
                    has_health_potion = False
                else:
                    die()
            else:
                print("You have " + str(health) + " health remaining!")
                time.sleep(1)
                input("Press enter to continue...")
                clear()

        defending = False
        while response < 1 or response > 2:
            if response == -1:
                input("You must select a number 1 through 2. (Press enter to continue...)")
                clear()
            print("Would you like to attack or defend this round?\n")
            print("1. Attack")
            print("2. Defend")
            response = input()
            response = clean_input(response)
            clear()

        if response == 1:
            #damage multiplier is based on strength and having a strength potion
            multiplier = strength / 10.0
            if has_strength_potion:
                multiplier = multiplier + 0.2
            damage_given = random.randint(8, 18) * multiplier
            print("You deal " + str(damage_given) + " damage to the guard!")
            guard_health = guard_health - damage_given
            if guard_health <= 0:
                input("Press enter to continue...")
                clear()
                victory_sequence()
            time.sleep(1)
            input("The guard has " + str(guard_health) + " left! (Press enter to continue...)")
            clear()
        elif response == 2:
            defending = True
            input("You are going to defend against the next attack! (Press enter to continue...)")
            clear()
        #Dexterity is high, so player attacked first
        if dexterity > 10:
            damage_received = calculate_guard_damage(third_round_special, defending)
            if third_round_special == 3:
                third_round_special = 0
            #Player recieves damage, check if they are dead.
            print("The guard deals " + str(damage_received) + " damage!")
            health = health - damage_received

            if health <= 0:
                input("Press enter to continue...")
                clear()
                if has_health_potion:
                    health = 100
                    input("Your strength has run out, but before you breathe your last breath, you drink your health potion and are fully restored! (Press enter to continue...)")
                    clear()
                    has_health_potion = False
                else:
                    die()
            else:
                print("You have " + str(health) + " health remaining!")
                time.sleep(1)
                input("Press enter to continue...")
                clear()
        third_round_special = third_round_special + 1
        if third_round_special == 1:
            input("The guard starts to charge up for a strong attack! (Press enter to continue...)")
        elif third_round_special == 2:
            input("The gurard is still charging up for a strong attack! (Press enter to continue...)")
        elif third_round_special == 3:
            input("The guard is about to release a strong attack! (Press enter to continue...)")
        clear()

def calculate_guard_damage(third_round_special, defending):
    if third_round_special == 3:
        damage_received = random.randint(15, 30)
    else:
        damage_received = random.randint(5, 15)
    if defending:
        print("You take a strong, stable defensive stance! Damage taken is reduced!")
        time.sleep(1)
        damage_received = damage_received * 0.4
    if has_shield:
        damage_received = damage_received * 0.9
    return damage_received

def die():
    os.system('color 07')

    clear()
    time.sleep(2)
    print("The guard kicks you in the chest, and you fall onto your back. You are beaten and battered, and have no energy left...")
    time.sleep(3)
    print("Through your closing eyes, you can see the guard standing over you, smiling, as he lifts his sword over his head...")
    time.sleep(2)
    input("Press enter to continue...")
    clear()
    print("As he swings the sword down, everything goes black...")
    time.sleep(2)
    input("Press enter to continue...")
    clear()
    print("You have died!")
    sys.exit()

def victory_sequence():
    clear()
    print("With one last blow, the guard falls to his knees.")
    time.sleep(2)
    print('"Ha! It looks like I could use some more practice! You are free to enter the city..."')
    time.sleep(1)
    input("Press enter to contniue...")
    clear()
    print("You begin to walk towards the gate, and as it begins to open, it reveals the setting sun.")
    time.sleep(2)
    print("It is so bright, and as you lift your hand to shield your eyes, you walk into the city to find the thugs who stole your belongings...")
    time.sleep(2)
    input("To be continued...")
    clear()
    sys.exit()

#Location selection.
def location_selection():
    os.system('color 20')
    response = 0
    while response < 1 or response > 3:
        if response == -1:
            input("You must select a number 1 through 3. (Press enter to continue...)")
            clear()
        print("Looking out of the meadow, you see a few locations you can travel to. There is a small cave, a beach next to a lake, and Marrow.")
        time.sleep(2)
        print("Where would you like to go?\n")

        print("1. The Cave")
        print("2. The Beach")
        print("3. The City of Marrow (Dangerous)")
        response = input("(Chose a number 1-3)")
        response = clean_input(response)
        if response < 1 or response > 4:
            response = -1

    if response == 1 and visited_cave is False:
        visit_cave()
    elif response == 2 and visited_beach is False:
        visit_beach()
    elif response == 3:
        visit_marrow()
    else:
        clear()
        if response == 1:
            selected_location = "The Cave"
        elif response == 2:
            selected_location = "The Beach"
        input("You have already visited " + selected_location + ". Please select a different location. (Press enter to continue...)")
        clear()
        location_selection()





""" START THE ADVENTURE """

#Format the console
format_console()

#Intro text
print("You wake up a stones throw away from the road, in a an peaceful, grassy meadow. Looking around, you see tall mountains surrounding you with a river to your left.")
time.sleep(3)
print("That last thing you remember was being ambushed by bandits while you were traveling from your home village of Gravelston to the trading city of Marrow.")
time.sleep(2)
input("Press enter to continue..")
clear()

#Backstory Selection
response = 0
while response < 1 or response > 5:
    if response == -1:
        input("You must select a number 1 through 5. (Press enter to continue..)")
        clear()
    # \n is the new line character. Every print statement adds a new line after it, but you can manually
    # add more new lines by typing \n anywhere in the print statement.
    print("Why were you traveling to Marrow?\n")

    print("1. I'm a wheat farmer looking to sell some of my harvest to Vassal.")
    print("2. I'm a hunter looking to sell furs and meat at the market.")
    print("3. I'm a thief moving to a new area to drop my old identity.")
    print("4. I'm an adventurer looking for an epic quest.")
    print("5. I'm a student hoping to study at the Mage's college there.")
    # What we are doing here is called casting. The user is inputing text (a string), but we want it to be an integer (an int). So we cast their input to an integer.
    response = input("(Choose a number 1-5)")
    response = clean_input(response)
    # This checks if the number is not numeric and if it is not between 1 an 5. If either fails, we know the user didn't pick one of our choices.
    if response < 1 or response > 5:
        response = -1

if response == 1:
    charisma = charisma + 2
elif response == 2:
    dexterity = dexterity + 1
    strength = strength + 1
elif response == 3:
    dexterity = dexterity + 2
elif response == 4:
    strength = strength + 1
    charisma = charisma + 1
elif response == 5:
    intelligence = intelligence + 2
clear()


#Weapon Selection
print("You no longer have your horse or most of your belongings, but you do have your weapon, a half-full waterskin, and some unleven bread.")
time.sleep(3)

response = 0
while response < 1 or response > 4:
    if response == -1:
        input("You must select a number 1 through 4. (Press enter to continue..)")
        clear()
    print("What is your weapon?\n")

    print("1. A two handed sword.")
    print("2. A one handed sword and a shield.")
    print("3. A bow and quiver of arrows.")
    print("4. A lute.")
    response = input("(Choose a number 1-4)")
    response = clean_input(response)
    if response < 1 or response > 4:
        response = -1

if response == 1:
    strength = strength + 2
elif response == 2:
    dexterity = dexterity + 1
    strength = strength + 1
    has_shield = True
elif response == 3:
    dexterity = dexterity + 2
elif response == 4:
    #Because lutes are cool
    charisma = charisma + 2
    dexterity = dexterity + 2
    strength = strength + 2

clear()
location_selection()
