from genericpath import exists
from data import *

fajl='AutokEsTulajdonosai.txt'

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
            halmaz=row.strip().split(';')
            autok.append(halmaz[0])
            tulajdonosok.append(halmaz[1])
        file.close()

def fajlMentes():
    if exists(fajl):
        file=open(fajl,'w',encoding='UTF-8')
    for i in range(len(autok)):
        file.write(f'{autok[i]};{tulajdonosok[i]}\n')
    file.close()
    autok.clear()
    tulajdonosok.clear()

def ÖsszesautóKiírása():
    print('Összes parkoló autó:')
    for i in range(0,len(autok)-1):
        print(f'\t{i+1}. {autok[i]}')
        
def ÖsszesHely():
    print(helyek)

def SzabadHelyek():
    print(helyek-parkoloAutokSzama)