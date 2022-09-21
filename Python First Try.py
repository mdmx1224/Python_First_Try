from atexit import _clear
from filecmp import clear_cache
import os
from turtle import clearscreen


bol = True
while bol is True:
    os.system('cls' if os.name == 'nt' else 'clear')
    bol = False
    print('You want convert \n :::> kilometer to Mile \n Or \n :::> Mile to kilometer')
    Personal_decision = input()
    # Mile To Kilometer    <-------
    if Personal_decision[0] == 'm' or Personal_decision[0] == 'M' or Personal_decision[0] == '1':
        print('Please Enter Mile')
        Put_In = input()
        print('A few digits later. Do you want?')
        Decimal = input()
        Kilometer = round(float(Put_In) * 1.6, int(Decimal))
        print('kilometer --->' + str(Kilometer))
        print('Do you want Try again??')
        Try = input()
        if Try[0] == 'y' or Try[0] == 'Y' or Try[0] == '1':
            bol = True
            os.system('cls' if os.name == 'nt' else 'clear')
            
    # Kilometer To Mile    <-------    
    elif Personal_decision[0] == 'k' or Personal_decision[0] == 'K' or Personal_decision[0] == '0':
        print('Please Enter Kilometer')
        Put_In = input()
        print('A few digits later "." Do you want?')
        Decimal_1 = input()
        Mile = round(float(Put_In) / 1.6, int(Decimal_1))
        print('Mile --->' + str(Mile))
        print('Do you want Try again??')
        Try = input()
        if Try[0] == 'y' or Try[0] == 'Y' or Try[0] == '1':
            bol = True
            os.system('cls' if os.name == 'nt' else 'clear')
