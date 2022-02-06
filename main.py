#TODO: create 3 rows to build a screen
#TODO: create a coordinating system to choose the blank space
from replit import clear


def single_player():

    row_1 = [' ', ' ', ' ']
    row_2 = [' ', ' ', ' ']
    row_3 = [' ', ' ', ' ']


    print(f'{row_1}\n\n{row_2}\n\n{row_3}')
    print('*****  TIC TAC TOE  *****\n')
    print('you must type what line and what collumn you want separeted for a comma\nFor example 2,3 means you choose the second line, and third column ')
    user_symbol = input("What symbol do you want X or O: ")
    user_choice = input('Choose you movement: ').split(',')
    print(user_choice)


clear()
print('*****  TIC TAC TOE  *****')
game_choice = input("Type 'S' for single player or 'M' for two players: ").lower()





if game_choice == 's':
    single_player()





