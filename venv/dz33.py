def get_name():
    name = input('Введите имя: ')
    return name


def get_password():
    pas = input('Введите пароль: ')
    return pas
h = 'tuc'

name1 = 'Vlad'
pas1 = '1234'
name2 = 'Misha'
pas2 = '2345'
name3 = 'Boris'
pas3 = '3456'
name4 = 'Maks'
pas4 = '4567'
i = 0

while (i < 1):
    x = get_name()
    y = get_password()
    if x == name1 and y == pas1:
        print(f'Hey, {x}!')
        i = 1
    elif x == name2 and y == pas2:
        print(f'Hey, {x}!')
        i = 1
    elif x == name3 and y == pas4:
        print(f'Hey, {x}!')
        i = 1
    elif x == name4 and y == pas4:
        print(f'Hey, {x}!')
        i = 1
    else:
        print('Authentication Error. Check your name or password!')
