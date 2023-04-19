names = ('Vladislav', 'Boris', 'Uly', 'Yan', 'Maks', 'Misha')


def names_length1(names):
    return len(names) > 4


def names_length2(names):
    return len(names) <= 3


print(tuple(filter(names_length1, names)))
print(tuple(filter(names_length2, names)))
