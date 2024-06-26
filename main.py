import os
import time
import json
import datetime
from src import bevezető
from src import játék
from src import statisztika
from src import szöveg_kiirás

játékos_neve = ''


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def fő_menü():
    menü_elemek = ['Kvíz indítása', 'Statisztika', 'Segítség', 'Kilépés']
    while True:
        print('\n')
        print(szöveg_kiirás.gépelés('Válasz az alábbi lehetőségekből: '))
        for elem in menü_elemek:
            time.sleep(0.5)
            print(menü_elemek.index(elem) + 1, f'- {elem}')

        fő_menü_választ = input()
        match fő_menü_választ:
            case '1':
                clr()
                bevezető.bevezető()
                játék.játék_kezdése()
            case '2':
                clr()
                bevezető.bevezető()
                statisztika.statisztika()
            case '3':
                clr()
                bevezető.bevezető()
                statisztika.segítség()
            case '4':
                clr()
                print('Kiléptél a játékból!')
                quit()
            case _:
                continue


if __name__ == '__main__':
    clr()
    bevezető.bevezető()

    while True:
        játékos_neve = input(szöveg_kiirás.gépelés('\nKérlek add meg a neved: '))
        if len(játékos_neve) <= 24:

            with open('log\játékos.json', 'r', encoding='UTF-8') as játékos_fájl:
                játékos_adatok = json.load(játékos_fájl)

            játékos_adatok[0]["jatekos_neve"] = játékos_neve
            játékos_adatok[0]["datum"] = str(datetime.datetime.now())

            with open('log\játékos.json', 'w', encoding='UTF-8') as játékos_fájl:
                json.dump(játékos_adatok, játékos_fájl)

            szöveg_kiirás.gépelés(f'Üdv {játékos_neve} a kvíz játékban!')
            break
        else:
            szöveg_kiirás.gépelés(f'Túl hosszú nevet adtál meg!')

    fő_menü()
