import math




def is_perfect_cube(n):
    c = int(n ** (1 / 3.))
    return (c ** 3 == n) or ((c + 1) ** 3 == n)


def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


my_setting = {'cycle': 0,
              'true': 0,
              'false': 0}


on_off = {'square': False,
          'cube': True}


range_number = {'x': 2,
                'y': 10}

my_list = []
for number in range(range_number['x'], range_number['y']):
    if number == 0:
        continue
    my_list.append(number)

my_setting['false'], my_setting['true'], my_setting['cycle'] = 0, 0, 0,
if on_off['square']:
    for a in my_list:
        for b in my_list:
            my_setting['cycle'] += 1
            c = a ** 2 + b ** 2
            if a ** 2 + b ** 2 == c and math.sqrt(c) == isqrt(c):
                print(a ** 2, '+', b ** 2, '=', c)
                print('Числа:', a, ',', b, ',', isqrt(c))
                my_setting['true'] += 1
            else:
                my_setting['false'] += 1
    print('Вывод: ')
    print('Успешных вариантов было обнаружено ', my_setting['true'])
    print('Не успешных вариантов было обнаружено ', my_setting['false'])
    print('Общее колличество вариантов было вопроизведено ', my_setting['cycle'])


if on_off['cube']:
    for a in my_list:
        for b in my_list:
            my_setting['cycle'] += 1
            c = a ** 3 + b ** 3
            if a ** 3 + b ** 3 == c and is_perfect_cube(c):
                print(a ** 3, '+', b ** 3, '=', c)
                print('Числа:', a, ',', b, ',', pow(c, 1 / 3))
                my_setting['true'] += 1
            else:
                my_setting['false'] += 1
    print('Вывод: ')
    print('Успешных вариантов было обнаружено ', my_setting['true'])
    print('Не успешных вариантов было обнаружено ', my_setting['false'])
    print('Общее колличество вариантов было вопроизведено ', my_setting['cycle'])
