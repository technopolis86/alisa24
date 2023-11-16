s = input()
z = d = 0
fd = 0
fz = 0
while s != '':
    if s == 'добрый':
        d += 1
        fd = 1
        fz = 0
    if s == 'злой':
        z += 1
        fz = 1
        fd = 0
    if s == 'Какой подарок?':
        if d > z and fd:
            print('серебряный шиллинг')
        elif z > d and fz:
            print('золотой шилинг')
        else:
            print('Ах, не знаю!')
            break
        d = z = 0
    s = input()