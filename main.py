from random import seed
from random import randint
from datetime import datetime
from formatting import *

#area choice start:
coast_chosen = 0
jungle_chosen = 0
desert_chosen = 0
cold_choice = 0


#resources:
wood_resource = 0
food_resource = 0
day_energy = 3


def area_name_pick():
    print("choose your countries name")
    global player_country_name
    player_country_name = input()
    print("your countries name is " + player_country_name)
    print("what area do you want to start in: \n[🏖" + (underline("Coast"))+ "line🏖]\n[🌳" + (underline("Jungle")) + "🌳]\n[🏜" + (underline("Desert")) + "🏜]\n[❄The " + (underline("Cold"))+ " " + "(" + colour_red("HARD MODE") + ")❄]")
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
            global first_survivor_kevin
            first_survivor_Kevin = 1
            print("your first survivor is Kevin")
        elif value == 2:
            global first_survivor_Michael
            first_survivor_Michael = 1
            print("your first survivor is Michael")
        elif value == 3:
            global first_survivor_Sangres
            first_survivor_Sangres = 1
            print("your first survivor is Sangres")
        elif value == 4:
            global first_survivor_Joenas
            first_survivor_joenas = 1
            print("your first survivor is Joenas")
        else:
            global first_survivor_Harold
            first_survivor_Harold = 1
            print("your first survivor is Harold")


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

def wood_minigame():
    for x in range(1):
        wood_minigame_number1 = randint(0, 50)
        wood_minigame_number2 = randint(0, 50)
        wood_minigame_answer = int(input("what is " + str(wood_minigame_number1) + " + " + str(wood_minigame_number2) + " "))
        if wood_minigame_answer == wood_minigame_number1 + wood_minigame_number2:
            global wood_resource
            wood_resource = wood_resource + 1
            print("you succesfully cut down a tree you now have " + str(wood_resource) + " wood")
        else:
            print("wrong answer")

def jungle_first_action():
    global day_energy
    while day_energy > 0:
        print("what is your desired aciton as" + player_country_name + "\n[🪵Gather wood🪵]\n[🥩Hunt🥩]\n[🛖Build🛖]")
        global jungle_first_action
        jungle_first_action = input()
        if jungle_first_action == "wood":
            day_energy = day_energy - 1
            wood_minigame()
        elif jungle_first_action == "hunt":
            day_energy = day_energy - 1
            print("hunting placeholder")
        elif jungle_first_action == "build":
            day_energy = day_energy - 1
            print("build placeholder")
        else:
            print("invalid option")

def day_actions():
    day_energy = 3
    if jungle_chosen == 1:
        jungle_first_action()
    elif coast_chosen == 1:
        print("coast placeholder")
    elif desert_chosen == 1:
        print("desert placeholder")
    else:
        print("the cold placeholder")

area_name_pick()
people_generator()
terrain_generation_beggining()
day_actions()
