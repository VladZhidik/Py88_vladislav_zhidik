letter = ('Vladislav', 'Boris', 'UlylU', 'YanaY', 'Maks', 'Misha')


def letter_palindrom(letter):
    return letter==letter[::-1]


print(tuple(filter(letter_palindrom, letter)))
