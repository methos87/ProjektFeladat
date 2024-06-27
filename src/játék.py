import re
import os
import json
import random
import datetime
import unidecode
from src import naplo_stat
from abc import ABC, abstractmethod
from difflib import SequenceMatcher


class NemSzám(Exception): pass


class Kérdés(ABC):
    pontszám = 0
    kérdések_száma = 0
    helyes_válaszok_száma = 0
    helytelen_válaszok_száma = 0
    részleges_válaszok_száma = 0
    tolerancia = 0.1
    életpont = 3

    def __init__(self, kérdés, helyes_válasz):
        self.kérdés = kérdés
        self.helyes_válasz = helyes_válasz

    def _dekorator(függvény):
        def alfüggvény(self):
            print('\n')
            print(str(Kérdés.kérdések_száma) + '. kérdés')
            if 'DátumKérdés' in str(self):
                print('A választ ÉÉÉÉ-HH-NN formában add meg.')
            függvény(self)

        return alfüggvény

    @_dekorator
    def kérdés_feltesz(self) -> None:
        while True:
            try:
                kérdés_feltétele = input(self.kérdés)
                helyes_e, információ = self._választ_kiértékel(kérdés_feltétele)
                if helyes_e:
                    print(f'A válasz helyes! {információ}')
                else:
                    print(f'{információ}')
                break
            except ValueError:
                print(f'Nem megfelelő adattípust adtál meg. Kérlek, próbáld újra!')
            except Exception as E:
                print(f'Hiba: {E}')

    @staticmethod
    def egyszerüsit(szöveg) -> str:
        return unidecode.unidecode(szöveg.strip().lower())

    @staticmethod
    def _pontszám_számláló(pont) -> None:
        Kérdés.pontszám += pont

    @staticmethod
    def _részleges_válaszok_számláló() -> None:
        Kérdés.részleges_válaszok_száma += 1

    @staticmethod
    def _helyes_valasz_számláló() -> None:
        Kérdés.helyes_válaszok_száma += 1

    @staticmethod
    def _helytelen_válasz_számláló() -> None:
        Kérdés.helytelen_válaszok_száma += 1

    @staticmethod
    def _élet_vesztés() -> None:
        Kérdés.életpont -= 1

    @abstractmethod
    def _választ_kiértékel(self, kérdés_feltétele) -> (bool, str):
        pass


class SzámosKérdés(Kérdés):
    def _választ_kiértékel(self, kérdés_feltétele) -> (bool, str):
        if int(kérdés_feltétele) == int(self.helyes_válasz):
            Kérdés._pontszám_számláló(5)
            Kérdés._helyes_valasz_számláló()
            return True, 'Plusz 5 pont'
        else:
            pontosság = (abs(int(self.helyes_válasz) - int(kérdés_feltétele)) / abs(int(self.helyes_válasz))) * 100
            if 0 <= pontosság <= 10:
                Kérdés._pontszám_számláló(4)
                Kérdés._részleges_válaszok_számláló()
                return False, 'Majdnem jó, ám az eltérés 10% alatt van ezért kapsz 4 plusz pontott.'
            elif 10 < pontosság <= 20:
                Kérdés._pontszám_számláló(3)
                Kérdés._részleges_válaszok_számláló()
                return False, 'Majdnem jó, ám az eltérés 20% alatt van ezért kapsz 3 plusz pontott.'
            elif 20 < pontosság <= 30:
                Kérdés._pontszám_számláló(2)
                Kérdés._részleges_válaszok_számláló()
                return False, 'Majdnem jó, ám az eltérés 30% alatt van ezért kapsz 2 plusz pontott.'
            elif 30 < pontosság <= 40:
                Kérdés._pontszám_számláló(1)
                Kérdés._részleges_válaszok_számláló()
                return False, 'Majdnem jó, ám az eltérés 40% alatt van ezért kapsz 1 plusz pontott.'
            else:
                Kérdés._helytelen_válasz_számláló()
                Kérdés._élet_vesztés()
                return False, f'Nem jó. A válasz {str(self.helyes_válasz)} lett volna!'


class SzövegesKérdés(Kérdés):
    def __init__(self, kérdés, helyes_válasz, minta):
        super().__init__(kérdés, helyes_válasz)
        self.minta = minta

    def _választ_kiértékel(self, kérdés_feltétele) -> (bool, str):

        if (self.minta != '') and bool(re.search(self.minta, kérdés_feltétele)):
            Kérdés._pontszám_számláló(5)
            Kérdés._helyes_valasz_számláló()
            return True, 'Plusz 5 pont'
        elif (self.minta == '') and Kérdés.egyszerüsit(kérdés_feltétele) == Kérdés.egyszerüsit(self.helyes_válasz):
            Kérdés._pontszám_számláló(5)
            Kérdés._helyes_valasz_számláló()
            return True, 'Plusz 5 pont'
        else:
            if SequenceMatcher(None, Kérdés.egyszerüsit(kérdés_feltétele),
                               Kérdés.egyszerüsit(self.helyes_válasz)).ratio() > 0.75:
                Kérdés._pontszám_számláló(3)
                Kérdés._részleges_válaszok_számláló()
                print(f'Majdnem, a válasz {self.helyes_válasz if (self.minta == "") else self.minta[2:-2]} lett volna!')
                return False, 'Kapsz ezért kapsz 3 plusz pontott.'
            else:
                Kérdés._helytelen_válasz_számláló()
                Kérdés._élet_vesztés()
                return False, f'Nem helyes! A válasz {self.helyes_válasz if (self.minta == "") else self.minta[2:-2]}' \
                              f' lett volna!'


class LebegőPontosKérdés(Kérdés):
    def _választ_kiértékel(self, kérdés_feltétele) -> (bool, str):

        if str(kérdés_feltétele) == str(self.helyes_válasz):
            Kérdés._pontszám_számláló(5)
            Kérdés._helyes_valasz_számláló()
            return True, 'Plusz 5 pont'
        else:
            if float(self.helyes_válasz) - Kérdés.tolerancia < float(
                    kérdés_feltétele) < float(self.helyes_válasz) + Kérdés.tolerancia:
                Kérdés._pontszám_számláló(3)
                Kérdés._részleges_válaszok_számláló()
                return True, 'Plusz 3 pont'
            else:
                Kérdés._helytelen_válasz_számláló()
                Kérdés._élet_vesztés()
                return False, f'Nem jó. A válasz {str(self.helyes_válasz)} lett volna!'


class DátumKérdés(Kérdés):
    def _választ_kiértékel(self, kérdés_feltétele) -> (bool, str):

        dátum_válasz = datetime.date.fromisoformat(kérdés_feltétele)
        dátum_helyes_válasz = datetime.date.fromisoformat(self.helyes_válasz)
        eltérés_nap = abs((dátum_válasz - dátum_helyes_válasz).days)
        if eltérés_nap == 0:
            Kérdés._pontszám_számláló(5)
            Kérdés._helyes_valasz_számláló()
            return True, 'Plusz 5 pont'
        elif 0 < eltérés_nap < 365:
            Kérdés._pontszám_számláló(3)
            Kérdés._részleges_válaszok_számláló()
            print(f'Majdnem, a válasz {self.helyes_válasz} lett volna!')
            return False, 'Kapsz ezért kapsz 3 plusz pontott.'
        else:
            Kérdés._helytelen_válasz_számláló()
            Kérdés._élet_vesztés()
            return False, f'A válasz helytelen. A helyes válasz {dátum_helyes_válasz} lett volna!'


def játék_kezdése(játékos_neve):
    Kérdés.pontszám = 0
    Kérdés.kérdések_száma = 0
    kérdések_és_helyes_válaszok = []

    statisztika.log(játékos_neve, Kérdés.pontszám)

    # Kérdések fájl beolvasása
    kérdések_fájlnév = os.getcwd() + '\json\kérdések_és_helyes_válaszok.json'
    if os.path.isfile(kérdések_fájlnév):
        with open(kérdések_fájlnév, encoding='UTF-8') as kérdés_fájl:
            kérdések_és_helyes_válaszok_json = json.load(kérdés_fájl)
    else:
        print(f'Nem található a {kérdések_fájlnév} nevű fájl')

    for khv in kérdések_és_helyes_válaszok_json:
        if khv['típus'] == 'DátumKérdés':
            kérdések_és_helyes_válaszok.append(DátumKérdés(khv['kérdés'], khv['válasz']))
        elif khv['típus'] == 'SzámosKérdés':
            kérdések_és_helyes_válaszok.append(SzámosKérdés(khv['kérdés'], khv['válasz']))
        elif khv['típus'] == 'SzövegesKérdés':
            kérdések_és_helyes_válaszok.append(SzövegesKérdés(khv['kérdés'], khv['válasz'], khv['regex']))
        elif khv['típus'] == 'LebegőPontosKérdés':
            kérdések_és_helyes_válaszok.append(LebegőPontosKérdés(khv['kérdés'], khv['válasz']))

    try:
        while Kérdés.életpont:
            Kérdés.kérdések_száma += 1
            random.choice(kérdések_és_helyes_válaszok).kérdés_feltesz()

        eredmény = int(100 * Kérdés.pontszám / 45)

        print('\n')

        if eredmény < 30:
            print('Sajnos ez most nem sikerült. Próbáld meg mégegyszer!')
        elif 31 < eredmény < 99:
            print('A játékot sikeresen befejezted!')
        else:
            print('Gratulálok, az összes kérdésre tudtad a válasz!')

        print('\n')

        print('EREDMÉNYED')
        print(f'Kérdések száma: {Kérdés.kérdések_száma}')
        print(f'Helyes válaszok száma: {Kérdés.helyes_válaszok_száma}')
        print(f'Részleges válaszok száma: {Kérdés.részleges_válaszok_száma}')
        print(f'Helytelen válaszok száma: {Kérdés.helytelen_válaszok_száma}')
        print(f'Pontszám: {Kérdés.kérdések_száma * 5} / {Kérdés.pontszám}')

        statisztika.log_pontszám_frissit(Kérdés.pontszám)

    except FileNotFoundError as FNFE:
        print(f'A {FNFE.filename} nevü fájl hiányzik!')
