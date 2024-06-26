import os
import json

játékos_fájlnév = os.getcwd() + '\log\játékos.json'


def statisztika():
    sorszám = 1
    print('\n')
    if os.path.isfile(játékos_fájlnév):
        with open(játékos_fájlnév, encoding='UTF-8') as játékos_fájl:
            játékos_adatok_json = json.load(játékos_fájl)
    for játékos_adat in játékos_adatok_json:
        print(f'{sorszám}: {játékos_adat['jatekos_neve']} - pontszáma:  {játékos_adat['pontszam']}')
        sorszám += 1


def log():
    print('\n')
    print('Ez a log kiiratása')
    print('Munkálat alatt...')


def segítség():
    print('\n')
    print('Ez a segitség kiiratása')
    print('Munkálat alatt...')
