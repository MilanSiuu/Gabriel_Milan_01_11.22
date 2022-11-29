import time
from data import *
from os import system
from functions import *

valasztott=''
while valasztott!='0': 
    fajlBetoltes()
    system('cls')
    valasztott=menu()
    if valasztott=='1':
         system('cls')
         ÖsszesautóKiírása()
         input('tovább...')
    elif valasztott=='2':
        autoKiírásatulajdonossal()
    elif valasztott=='3':
        Ujauto()
    elif valasztott=='4':
        autoTörlése()
    elif valasztott=='5':
        ÖsszesHely()
    elif valasztott=='6':
        SzabadHelyek()
    elif valasztott=='7':
        pass
    else:
        system('cls')
        print('Hibás válasz.')
        time.sleep(1.5)
    fajlMentes()      