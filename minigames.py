import g_
from random import randint

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