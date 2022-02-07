#TODO: create 3 rows to build a screen
#TODO: create a coordinating system to choose the blank space
from replit import clear
import random
from single_player import single_player


clear()
print('*****  TIC TAC TOE  *****\n')
game_choice = input("Type 'S' for single player or 'M' for two players: ").lower()

if game_choice == 's':
    clear()
    single_player()







