from data import autókéstulajdonosai
from os import system
from functions import menu, ÖsszesautóKiírása

valasztott=''
while valasztott!='0': 
    system('cls')
    valasztott=menu()
    if valasztott=='1':
         system('cls')
         ÖsszesautóKiírása()
         input('tovább...')
    elif valasztott=='2':
        pass
    elif valasztott=='3':
        pass
    elif valasztott=='4':
        pass
    elif valasztott=='5':
        pass
    elif valasztott=='6':
        pass
    elif valasztott=='7':
        pass
        