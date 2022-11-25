from genericpath import exists
from data import autókéstulajdonosai

fajl='autók és tulajdonosai.txt'

def menu():
    system='cls'
    valasztott=''
    print('------------MENÜ------------')
    print('0 - Kilépés')
    print('1 - Összes autó kiírása')
    print('2 - Egy adott autó kiírása tulajdonossal')
    print('3 - Új parkoló autó')
    print('4 - Autó törlése')
    print('5 - Összes hely száma')
    print('6 - Szabad helyek száma')
    print('7 - Összes parkoló autó kiírása tulajdonossal')
    valasztott=input('Válasszon egy menüpontot: ')
    return valasztott

def fajlBetoltes():   
    if exists(fajl):
        file=open(fajl,'r',encoding='utf-8')
        for row in file:
            autókéstulajdonosai.append(row.strip())  
        file.close()
        input('A fájl betöltése sikeres volt.')


def ÖsszesautóKiírása():
    print('Összes parkoló autó:')
    for i in range(0,len(autókéstulajdonosai)):
        print(f'\t{i+1}. {autókéstulajdonosai[i]}')