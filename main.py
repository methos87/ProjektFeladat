import os
import time
from src import játék
from src import naplo_stat
from src import szövegek


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')


def fő_menü(játékos_neve):
    menü_elemek = ['Kvíz indítása', 'Statisztika', 'Segítség', 'Kilépés']
    while True:
        print('\n')
        print(szövegek.gépelés('Válasz az alábbi lehetőségekből: \n'))
        for elem in menü_elemek:
            time.sleep(0.5)
            print(menü_elemek.index(elem) + 1, f'- {elem}')

        fő_menü_választ = input()
        match fő_menü_választ:
            case '1':
                clr()
                szövegek.bevezető()
                játék.játék_kezdése(játékos_neve)
            case '2':
                clr()
                szövegek.bevezető()
                statisztika.statisztika()
            case '3':
                clr()
                szövegek.bevezető()
                szövegek.segítség()
            case '4':
                clr()
                print('Kiléptél a játékból!')
                quit()
            case _:
                continue


if __name__ == '__main__':

    clr()
    szövegek.bevezető()

    while True:
        játékos_neve = input(szövegek.gépelés('\nKérlek add meg a neved: '))
        if len(játékos_neve) <= 24:

            szövegek.gépelés(f'Üdv {játékos_neve} a kvíz játékban!')
            break
        else:
            szövegek.gépelés('Túl hosszú nevet adtál meg!')

    fő_menü(játékos_neve)
