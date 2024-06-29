import os
import json
import datetime

játékos_fájlnév = "log/játékos.json"


def statisztika():
    sorszám = 1
    print('\n')
    if os.path.isfile(játékos_fájlnév):
        with open(játékos_fájlnév, encoding='UTF-8') as játékos_fájl:
            játékos_adatok_json = json.load(játékos_fájl)
    for játékos_adat in játékos_adatok_json:
        print(f'{sorszám}:' + (' ' * (9 - len(f"{sorszám}:"))) +
              f'{játékos_adat["jatekos_neve"]}' + (' ' * (13 - len(f'{játékos_adat["jatekos_neve"]}'))) +
              f'{játékos_adat["datum"][0:-7]}     '
              f'{játékos_adat["pontszam"]}')
        sorszám += 1


def naplo(játékos_neve, pontszám=0):
    print('\n')
    with open('log/játékos.json', 'r', encoding='UTF-8') as játékos_fájl:
        játékos_adatok = json.load(játékos_fájl)

    játékos_adatok.append({"jatekos_neve": játékos_neve,
                           "datum": str(datetime.datetime.now()),
                           "pontszam": pontszám,
                           })

    with open('log/játékos.json', 'w', encoding='UTF-8') as játékos_fájl:
        json.dump(játékos_adatok, játékos_fájl, indent=4)


def naplo_pontszám_frissit(pontszám):
    print('\n')
    with open('log/játékos.json', 'r', encoding='UTF-8') as játékos_fájl:
        játékos_adatok = json.load(játékos_fájl)

    játékos_adatok[-1]["pontszam"] = pontszám

    with open('log/játékos.json', 'w', encoding='UTF-8') as játékos_fájl:
        json.dump(játékos_adatok, játékos_fájl, indent=4)
