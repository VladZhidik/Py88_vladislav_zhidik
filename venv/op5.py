name1 = 'Vlad'
name2 = 'Misha'
name3 = 'Maks'
name4 = 'Boris'
pas1 = 1234
pas2 = 2345
pas3 = 3456
pas4 = 4567

def check_name(name):
    if name == name1:
        y = get_password()
        return(y)
    elif name == name2:
        y = get_password()
        return(y)
    elif name == name3:
        y = get_password()
        return(y)
    elif name == name4:
        y = get_password()
        return(y)
    else:
        print ('Authentication Error. Check your name or password!')
        return(None)

def get_name():
    name = input('Введите имя: ')
    x = check_name(name)
    return x

def check_password(pas):
    if name == name1:
        if pas == pas1:
            return(pas)
        else:
            print('Authentication Error. Check your name or password!')
            return (None)
        return(name)
    elif name == name2:
        y = get_password()
        return(y)
    elif name == name3:
        y = get_password()
        return(y)
    elif name == name4:
        y = get_password()
        return(y)
    else:
        print ('Authentication Error. Check your name or password!')
        return(None)

def get_password():
    pas = input('Введите пароль: ')
    z = check_password(pas)
    return z

n = get_name()
print(f'Hello, {n}!')

