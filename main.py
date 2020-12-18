"""
coding: utf8
"""
import os
import json
import requests
from bs4 import BeautifulSoup


CURRENT_DIR = os.path.dirname(__file__)
URL ='https://fr.openfoodfacts.org/produit/'
SOURCE = CURRENT_DIR + '\\input\\View_Auchan_Simpliste_20200519.json'
OUTPUT = CURRENT_DIR + '\\output\\output.txt'


with open(SOURCE , 'r', encoding='utf8') as f:
    bdd = json.load(f)

for i in range (0, 50):
    #indique l'état d'avancement
    print('Article   n°{}    {}%'.format(i + 1,100*(i + 1)/len(bdd)))
    scrap = requests.get(URL + str(bdd[i]['Code_Barres']) + '/')
    if scrap.ok :
        soup = BeautifulSoup(scrap.text,'lxml')
        title = soup.find('title')
        new_Libelle = title.text
        bdd[i]['Libelle'] = new_Libelle

with open(OUTPUT, "a", encoding="utf8") as f:
    f.write('[')
    for i in range (0, 50):
        json.dump(bdd[i], f, ensure_ascii=False)
        f.write(',')
    f.write(']')
