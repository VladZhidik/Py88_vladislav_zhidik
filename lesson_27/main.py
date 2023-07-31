number = [3, 6, 2, 4, 5]
number.sort()


def sq(number):

    return sorted(list(map(lambda x: x**2, number)))


print(sq(number))
