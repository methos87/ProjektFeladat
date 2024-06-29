import os
import time


def bevezető():
    cím = '*' + (' ' * 15) + 'ASZTRO AKADÉMIA' + (' ' * 15) + '*'
    print('*' * len(cím))
    print('*' + (' ' * 45) + '*')
    print(cím)
    print('*' + (' ' * 45) + '*')
    print('*' * len(cím))

    készítette = 'Készítette: Novák Ákos'
    dátum = '2024'
    vonalak_hossza = (len(cím) - (len(készítette) + len(dátum) + 4)) // 2
    print(('-' * vonalak_hossza) + ' ' + készítette + ', ' + dátum + ' ' + ('-' * vonalak_hossza))


def gépelés(szöveg):
    print('\r')
    for i in szöveg:
        print(i, end='', flush=True)
        time.sleep(0.035)
    time.sleep(0.5)
    return ''


def segítség():
    print('\n')
    print('Ez a segitség kiiratása')
    print('Munkálat alatt...')


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
