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
    print('''
    ## Asztro Akadémia - Segítség

    **Játékmenet:**
    * A játék során különböző típusú kérdésekre kell válaszolnod.
    * Minden helyes válasz 5 pontot ér, a részleges válaszok pedig attól függöen,
      hogy mennyivel térsz el a helyes választól részleges pontott kapsz.
    * Helytelen válasz esetén 1 élet levononódik.
    * Ha elfogy az életed, a játék véget ér.

    **Kérdéstípusok:**
    * **Számos Kérdés:** Számot kell megadnod válaszként.
    * **Szöveges Kérdés:** Szöveget kell megadnod válaszként.
        A kérdés néha tartalmazhat egy minta kifejezést, amelyet a válasznak meg kell felelnie.
    * **Lebegő Pontos Kérdés:** Számot kell megadnod válaszként, egy megadott tűréshatáron belül.
    * **Dátum Kérdés:** Dátumot kell megadnod ÉÉÉÉ-HH-NN formában.

    **Tippek:**
    * Olvasd el figyelmesen a kérdéseket.
    * Gondold át a válaszokat, mielőtt begépeled őket.
    * Ha nem vagy biztos a válaszban, próbálj meg tippelni.

    **Jó szórakozást!**

    ''')


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
