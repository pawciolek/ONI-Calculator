import json

with open('Data.json', 'r', encoding='utf-8') as plik:
    dane = json.load(plik)

for dish in dane["Dishes"]:
    print(dish['name'])
    for ingredients in dish['ingredient']:
        print(f" - {ingredients['ingredient']} ({ingredients['amount']})")
