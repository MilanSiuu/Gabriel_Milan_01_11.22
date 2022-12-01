from genericpath import exists
from data import *
from os import system
import time

fajl='AutokEsTulajdonosai.txt'

def menu():
    system=('cls')
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
    for i in range(0,len(autok)):
        print(f'\t{i+1}. {autok[i]}')
    time.sleep(10)
        
def ÖsszesHely():
    print(helyek)
    time.sleep(2)

def SzabadHelyek():
    parkoloAutokSzama=len(autok)
    szabad=helyek-parkoloAutokSzama
    print(szabad)
    time.sleep(2)

def autoKiírásatulajdonossal():
    system('cls')
    bekertautok=input('Adja meg az autó típusát: ').upper()
    if  bekertautok.upper() in autok:
        for i,item in enumerate(autok):
            if bekertautok.upper()==item.upper():
                print(f'\nAz autó tulajdonosa: {tulajdonosok[i]}')
                time.sleep(2)
    else:    
        print('Ez az autó nem található')
        time.sleep(2)

def autoTörlése():
    system('cls')
    bekertautok=input('Adja meg az autó típusát: ').upper()
    if  bekertautok.upper() in autok:
        for i,item in enumerate(autok):
            if bekertautok.upper()==item.upper():
                autok.pop(i)
                print(f'Az autó törölve')
                time.sleep(2)
    else:    
        print('Ez az autó nem található')
        time.sleep(2)

def Ujauto():
    system('cls')
    bekertauto=input('Kérem adja meg az új autó típusát: ')
    bekertnev=input('Kérem adja meg az új autó tulajdonosát: ')
    autok.append(bekertauto.upper())
    tulajdonosok.append(bekertnev.title())
    print('Az adatokat mentettük!')
    time.sleep(2)

def AutokTulajdonossal():
    system('cls')
    print('Autók és tulajdonosaik: ')
    for i in range(len(autok)):
        print(f'\t{autok[i]} - {tulajdonosok[i]}')
    time.sleep(5)