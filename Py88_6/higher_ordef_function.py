def func1():
    """ I am func1"""
    print(func1.__doc__)
    return print('№')


def func2():
    """ I am func2"""
    print(func2.__doc__)
    return print('№')


def func3():
    """ I am func3"""
    print(func3.__doc__)
    return print('№')


def repeat(func, n=10):
    for i in range(n):
        func(), print(i+1)


repeat(func1, 3)
repeat(func2, 5)
repeat(func3, 10)
repeat(func1)
