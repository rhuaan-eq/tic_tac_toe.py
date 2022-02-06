from replit import clear

def single_player():
    row_1 = [' ', ' ', ' ']
    row_2 = [' ', ' ', ' ']
    row_3 = [' ', ' ', ' ']
    screen = (f'{row_1}\n\n{row_2}\n\n{row_3}')    

    print(screen)
    print('*****  TIC TAC TOE  *****\n')
    print('''you must type what line and what collumn you want separeted for a comma\n
    For example 2,3 means you choose the second line, and third column\n''')
    #------------------------------------------------------------------------------------------------
    user_symbol = input("What symbol do you want X or O: ").upper()
    while user_symbol != 'X' and user_symbol != 'O':
        clear()
        print(screen)
        print('*****  TIC TAC TOE  *****\n')
        print('''you must type what line and what collumn you want separeted for a comma\n
                For example 2,3 means you choose the second line, and third column\n''')

        user_symbol = input('You type wrong... X or O: ').upper()
    #------------------------------------------------------------------------------------------------
    user_choice = input('Choose you movement: ').split(',')
    while user_choice[0] != '1' and user_choice[0] != '2' and user_choice[0] != '3' and user_choice[1] != '1' and user_choice[1] != '2' and user_choice[1] != '3':
        clear()
        print(screen)
        print('*****  TIC TAC TOE  *****\n')
        print('''you must type what line and what collumn you want separeted for a comma\n
                For example 2,3 means you choose the second line, and third column\n''')
        user_choice = input('''You type an invalid number, keep rows and columns among 1 2 3\n
        Type you movement again: ''')
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
    
    print(screen)
    
    
        

clear()
single_player()