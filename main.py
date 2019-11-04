import json
table = json.load(open('./periodic_table.json'))

mode = input('Wybierz tryb (liczba atomowa - 1, symbol - 2): ')

if (mode == '1'):
    number = input('Podaj liczbę atomową: ')

    for atom in table['elements']:
        if (atom['number'] == int(number)):
            foundAtom = atom
            break
    
    try: foundAtom
    except NameError: foundAtom = None
    if (foundAtom == None):
        print('Nie znaleziono takiego atomu')
    else:
        print(foundAtom['electron_configuration'])
elif (mode == '2'):
    symbol = input('Podaj symbol atomu: ')

    for atom in table['elements']:
        if (atom['symbol'] == symbol):
            foundAtom = atom
            break
    
    try: foundAtom
    except NameError: foundAtom = None
    if (foundAtom == None):
        print('Nie znaleziono takiego atomu')
    else:
        print(foundAtom['electron_configuration'])
else:
    print('Nie istnieje tryb ', mode)


