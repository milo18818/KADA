from random import seed
from random import randint
from datetime import datetime

#area choice start:
coast_chosen = 0
jungle_chosen = 0
desert_chosen = 0
cold_choice = 0

#action related
first_action_complete = 0

#resources:
wood_resource = 0
stone_resource = 0
food_resource = 0


def area_name_pick():
    print("choose your countries name")
    global player_country_name
    player_country_name = input()
    print("your countries name is " + player_country_name)
    print("what area do you want to start in: \n[🏖Coastline🏖]\n[🌳Jungle🌳]\n[🏜Desert🏜]\n[❄The Cold (Hard mode)❄]")
    player_country_area_choice = input()
    if player_country_area_choice == "coast":
        global coast_chosen
        coast_chosen = 1
    elif player_country_area_choice == "jungle":
        global jungle_chosen
        jungle_chosen = 1
    elif player_country_area_choice == "desert":
        global desert_chosen
        desert_chosen = 1
    elif player_country_area_choice == "cold":
        global cold_choice
        cold_choice = 1


def people_generator():
    print("generating people")
    seed_generator = datetime.now()
    seed(seed_generator.second)
    for x in range(1):
        value = randint(0, 5)
        if value == 1:
            global first_survivor1
            first_survivor1 = 1
            print("your first survivor is 1")
        elif value == 2:
            global first_survivor2
            first_survivor2 = 1
            print("your first survivor is 2")
        elif value == 3:
            global first_survivor3
            first_survivor3 = 1
            print("your first survivor is 3")
        elif value == 4:
            global first_survivor4
            first_survivor4 = 1
            print("your first survivor is 4")
        else:
            global first_survivor5
            first_survivor5 = 1
            print("your first survivor is 5")


def terrain_generation_beggining():
    print("generating terrain")
    if coast_chosen == 1:
        print("the country of " + player_country_name + " 🏖️begins on the coast🏖️")
    elif jungle_chosen == 1:
        print("the country of " + player_country_name + " 🌳starts inside a dense forest🌳")
    elif desert_chosen == 1:
        print("the country of " + player_country_name + " 🏜️starts in a barren desert🏜️")
    else:
        print("the country of " + player_country_name + " ❄starts in the freezing wasteland❄")

def jungle_first_action():
    global first_action_complete
    while first_action_complete == 0:
        print("what is your first aciton as" + player_country_name + "\n[🪵Gather wood🪵]\n[🥩Hunt🥩]\n[🛖Build🛖]")
        global jungle_first_action
        jungle_first_action = input()
        if jungle_first_action == "wood":
            first_action_complete = first_action_complete + 1
            print("you harvested wood")
            global wood_resource
            wood_resource = wood_resource + 1
            print("you now have " + str(wood_resource) + " wood")
        elif jungle_first_action == "hunt":
            first_action_complete = first_action_complete + 1
            print("hunting placeholder")
        elif jungle_first_action == "build":
            first_action_complete = first_action_complete + 1
            print("build placeholder")
        else:
            print("invalid option")

def coatline_action():
    global first_action_complete
    while first_action_complete == 0:
        print("what is your first action as " + player_country_name + "\n[🎣Fish🎣]\n[🪵Gather wood🪵]\n[🛖Build🛖]")
        global coast_first_action
        coast_first_action = input()
        if coast_first_action == "wood":
            first_action_complete = first_action_complete + 1
            print("you harvested wood")
            global wood_resource
            wood_resource = wood_resource + 1
            print("you now have " + str(wood_resource) + " wood")
        elif coast_first_action == "fish":
            first_action_complete = first_action_complete + 1
            print("fishing placeholder")
        elif coast_first_action == "build":
            first_action_complete = first_action_complete + 1
            print("build placeholder")
        else:
            print("invalid option")

def desert_action():
    global first_action_complete
    while first_action_complete == 0:
        print("what is your first action as " + player_country_name + "\n[🥩Hunt🥩]\n[🌵Harvest cactus🌵]\n[🛖build🛖]")
        global desert_first_action
        desert_first_action = input()
        if desert_first_action == "cactus":
            first_action_complete = first_action_complete + 1
            print("you harvested cactus")
            global wood_resource
            wood_resource = wood_resource + 2
            print("you now have " + str(wood_resource) + " wood")
        elif desert_first_action == "fish":
            first_action_complete = first_action_complete + 1
            print("fishing placeholder")
        elif desert_first_action == "build":
            first_action_complete = first_action_complete + 1
            print("build placeholder")
        else:
            print("invalid option")
def first_action_tutorial():
    if jungle_chosen == 1:
        jungle_first_action()
    elif coast_chosen == 1:
        coatline_action()
    elif desert_chosen == 1:
        desert_action()
    else:
        print("the cold placeholder")
    if first_action_complete == 1:
        print("egg roll")

area_name_pick()
people_generator()
terrain_generation_beggining()
first_action_tutorial()
