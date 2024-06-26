import os
import json

számol = 0
kérdések = []
ismédlődő_kérdések = []

kérdések_fájlnév = os.getcwd() + '\json\kérdések_és_helyes_válaszok.json'
if os.path.isfile(kérdések_fájlnév):
    with open(kérdések_fájlnév, encoding='UTF-8') as kérdés_fájl:
        kérdések_és_helyes_válaszok_json = json.load(kérdés_fájl)


for kérdés in kérdések_és_helyes_válaszok_json:
    kérdések.append(kérdések_és_helyes_válaszok_json['kérdés'])
