def bevezető():
    cím = '*'+ (' ' * 15) + 'ASZTRO AKADÉMIA' + (' ' * 15) + '*'
    print('*' * len(cím))
    print('*' + (' ' * 45) + '*')
    print(cím)
    print('*' + (' ' * 45) + '*')
    print('*' * len(cím))

    készítette = 'Készítette: Novák Ákos'
    dátum = '2024'
    vonalak_hossza = (len(cím) - (len(készítette) + len(dátum) + 4)) // 2
    print(('-' * vonalak_hossza) + ' ' + készítette + ', ' + dátum + ' ' + ('-' * vonalak_hossza))



