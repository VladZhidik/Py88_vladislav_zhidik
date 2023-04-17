def get_name():
    name = input('Введите имя: ')
    return name


def get_password():
    pas = input('Введите пароль: ')
    return pas


user1 = {
    'Vlad': '1234'
}
user2 = {
    'Misha': '2345'
}
user3 = {
    'Boris': '3456'
}
user4 = {
    'Maks': '4567'
}
i = 0

while i < 1:
    user_name = get_name()
    user_pass = get_password()
    user = {user_name: user_pass}
    if user == user1:
        print(f'Hey, {user_name}!')
        i = 1
    elif user == user2:
        print(f'Hey, {user_name}!')
        i = 1
    elif user == user3:
        print(f'Hey, {user_name}!')
        i = 1
    elif user == user4:
        print(f'Hey, {user_name}!')
        i = 1
    else:
        print('Authentication Error. Check your name or password!')
