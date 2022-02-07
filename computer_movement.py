from replit import clear
import random

def computer_movement(computer_symbol,row_1,row_2,row_3):
    computer_row_number = random.randint(1,3)
    computer_collumn_number = random.randint(1,3)
    if computer_row_number == '1':
        if computer_collumn_number == '1':
            row_1[0] = computer_symbol
        elif computer_collumn_number =='2':
            row_1[1] = computer_symbol
        elif computer_collumn_number == '3':
            row_1[2] = computer_symbol
    elif computer_row_number == '2':
        if computer_collumn_number == '1':
            row_2[0] = computer_symbol
        elif computer_collumn_number =='2':
            row_2[1] = computer_symbol
        elif computer_collumn_number == '3':
            row_2[2] = computer_symbol
    elif computer_row_number == '3':
        if computer_collumn_number == '1':
            row_3[0] = computer_symbol
        elif computer_collumn_number =='2':
            row_3[1] = computer_symbol
        elif computer_collumn_number == '3':
            row_3[2] = computer_symbol
    
