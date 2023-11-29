import g_
from random import randint
from random import seed
from datetime import datetime

#constants
WOOD_STARTRANGE=0
WOOD_ENDRANGE=50

def wood_minigame():
    for x in range(1):
        wood_minigame_number1 = randint(WOOD_STARTRANGE, WOOD_ENDRANGE)
        wood_minigame_number2 = randint(WOOD_STARTRANGE, WOOD_ENDRANGE)
        wood_minigame_answer = int(input("what is " + str(wood_minigame_number1) + " + " + str(wood_minigame_number2) + " "))
        if wood_minigame_answer == wood_minigame_number1 + wood_minigame_number2:
            g_.wood_resource = g_.wood_resource + 1
            print("you succesfully cut down a tree you now have " + str(g_.wood_resource) + " wood")
        else:
            print("wrong answer")

#people check
first_survivor_kevin = 0
first_survivor_Michael = 0
first_survivor_Sangres = 0
first_survivor_Joenas = 0
first_survivor_Harold = 0

#stats
#kevin
first_survivor_kevin_health = 10
first_survivor_kevin_attack = 5
#Michael
first_survivor_Michael_health = 15
first_survivor_Michael_attack = 3
#Sangres
first_survivor_Sangres_health = 10
first_survivor_Sangres_attack = 10
#Joenas
first_survivor_Joenas_health = 12
first_survivor_Joenas_attack = 6
#Harold
first_survivor_Harold_health = 5
first_survivor_Harold_attack = 10


def hunting_minigame():
    if first_survivor_kevin == 1:
        g_.survivor1_name = "kevin"
        survivor1_health = first_survivor_kevin_health
        survivor1_attack = first_survivor_kevin_attack
    elif first_survivor_Michael == 1:
        g_.survivor1_name = "Michael"
        survivor1_health = first_survivor_Michael_health
        survivor1_attack = first_survivor_Michael_attack
    elif first_survivor_Sangres == 1:
        g_.survivor1_name = "Sangres"
        survivor1_health = first_survivor_Sangres_health
        survivor1_attack = first_survivor_Sangres_attack
    elif first_survivor_Joenas == 1:
        g_.survivor1_name = "Joenas"
        survivor1_health = first_survivor_Joenas_health
        survivor1_attack = first_survivor_Joenas_attack
    else:
        g_.survivor1_name = "Harold"
        survivor1_health = first_survivor_Harold_health
        survivor1_attack = first_survivor_Harold_attack
    seed_generator = datetime.now()
    seed(seed_generator.second)
    for x in range(1):
        value = randint(0, 5)
        if value == 1:
            animal1_name = "wolf"
            animal1_health = 10
            animal1_attack = 1
        elif value == 2:
            animal1_name = "Bear"
            animal1_health = 13
            animal1_attack = 3
        elif value == 3:
            animal1_name = "Rabbit"
            animal1_health = 4
            animal1_attack = 0
        elif value == 4:
            animal1_name = "Snake"
            animal1_health = 5
            animal1_attack = 10
        else:
            animal1_name = "Deer"
            animal1_health = 5
            animal1_attack = 0
        while animal1_health > 0:
            print(g_.survivor1_name + " finds and attacks a " + animal1_name)
            animal1_health = animal1_health - survivor1_attack
            print("the " + animal1_name + " has " + str(animal1_health) + " health remaining")
            if animal1_health < 0 or animal1_health == 0:
                print("the " + animal1_name + " is killed and you gain 1 food")
                break
            survivor1_health = survivor1_health - animal1_attack
            print("the " + animal1_name + " attacks " + g_.survivor1_name + " ,he now has " + str(survivor1_health) + " health remaining")
            print("what do you do")
            mid_fight_action = input()
            if mid_fight_action == "fight":
                while animal1_health > 0:
                    animal1_health = animal1_health - survivor1_attack
                    print("the " + animal1_name + " has " + str(animal1_health) + " health remaining")
                if animal1_health == 0:
                    print("the" + animal1_name + "is killed and you gain 1 food")