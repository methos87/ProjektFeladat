import time
from src import játék
from src import naplo_stat
from src import eszközök


def fő_menü(játékosneve):
    menü_elemek = ['Új játék', 'Statisztika', 'Segítség', 'Kilépés']
    while True:
        print('\n')
        print(eszközök.gépelés('Válasz az alábbi lehetőségekből: \n'))
        for elem in menü_elemek:
            time.sleep(0.5)
            print(menü_elemek.index(elem) + 1, f'- {elem}')

        fő_menü_választ = input()
        match fő_menü_választ:
            case '1':
                eszközök.clr()
                eszközök.bevezető()
                játék.játék_kezdése(játékosneve)
            case '2':
                eszközök.clr()
                eszközök.bevezető()
                naplo_stat.statisztika()
            case '3':
                eszközök.clr()
                eszközök.bevezető()
                eszközök.segítség()
            case '4':
                eszközök.clr()
                print('Kiléptél a játékból!')
                quit()
            case _:
                continue


def indit(*args, **kwargs):
    eszközök.clr()
    eszközök.bevezető()

    while True:
        játékos_neve = input(eszközök.gépelés('\nKérlek add meg a neved: '))
        if len(játékos_neve) <= 10:

            eszközök.gépelés(f'Üdv {játékos_neve} a kvíz játékban!')
            break
        else:
            eszközök.gépelés('Kérlek maximum 10 karakter hosszú nevet adj meg.')

    fő_menü(játékos_neve)


if __name__ == '__main__':
    indit()
