from replit import clear
from computer_movement import computer_movement
import choice_check
import random

def single_player():
    #---------------------------------------------WELCOME SCREEN---------------------------------------------
    row_1 = [' ', ' ', ' ']
    row_2 = [' ', ' ', ' ']
    row_3 = [' ', ' ', ' ']
    
    screen = (f'{row_1}\n\n{row_2}\n\n{row_3}')    
    print(screen)
    print('*****  TIC TAC TOE  *****\n')
    print('''you must type what line and what collumn you want separeted for a comma\n
    For example 2,3 means you choose the second line, and third column\n''')
    #---------------------------------------------USER SYMBOL SELECT---------------------------------------------------
    user_symbol = input("What symbol do you want X or O: ").upper()
    while user_symbol != 'X' and user_symbol != 'O':
        clear()
        print(screen)
        print('*****  TIC TAC TOE  *****\n')
        print('''you must type what line and what collumn you want separeted for a comma\n
                For example 2,3 means you choose the second line, and third column\n''')

        user_symbol = input('You type wrong... X or O: ').upper()
    if user_symbol == 'X':
        computer_symbol = 'O'
    else:
        computer_symbol = 'X'
    #---------------------------------------------------GAME START----------------------------------------
    game = True
    while game is True:
        #--------------------------------------------USER MOVEMENT SELECT----------------------------------------------------
        check_blank_space = False
        user_choice = input('Choose your movement: ').split(',')
        while user_choice[0] != '1' and user_choice[0] != '2' and user_choice[0] != '3' and user_choice[1] != '1' and user_choice[1] != '2' and user_choice[1] != '3' and check == True:
            clear()
            print(screen)
            print('*****  TIC TAC TOE  *****\n')
            print('''you must type what line and what collumn you want separeted for a comma\n
                    For example 2,3 means you choose the second line, and third column\n''')
            user_choice = input('''You type an invalid number, keep rows and columns among 1 2 3\n
            Type your movement again: ''')
            choice_check.user_choice_checker(user_choice,row_1,row_2,row_3)
        #--------------------------------------------MOVEMENT CHECK ---------------------------------------
        
        #------------------------------------------------------------------------------------------------
        if user_choice[0] == '1':
            if user_choice[1] == '1':
                row_1[0] = user_symbol
            elif user_choice[1] =='2':
                row_1[1] = user_symbol
            elif user_choice[1] == '3':
                row_1[2] = user_symbol
        elif user_choice[0] == '2':
            if user_choice[1] == '1':
                row_2[0] = user_symbol
            elif user_choice[1] =='2':
                row_2[1] = user_symbol
            elif user_choice[1] == '3':
                row_2[2] = user_symbol
        elif user_choice[0] == '3':
            if user_choice[1] == '1':
                row_3[0] = user_symbol
            elif user_choice[1] =='2':
                row_3[1] = user_symbol
            elif user_choice[1] == '3':
                row_3[2] = user_symbol
        computer_movement(computer_symbol,row_1,row_2,row_3)
        new_screen = (f'{row_1}\n\n{row_2}\n\n{row_3}')
        clear()
        print(f'{new_screen}')
        print(computer_symbol)
    
    
        

clear()
single_player()