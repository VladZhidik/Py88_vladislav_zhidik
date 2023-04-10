
name, name1, name2, name3, name4 = 'Misha', 'Vlad', 'Borya', 'Maks', 'Artem'

names = (name, name1, name2, name3, name4)
one, two, three, four, five = names
names = (one, two, three, four, five)
print(names)

one, five = five, one
names = (one, two, three, four, five)
print(names)

one = two = three = four = five = two
names = (one, two, three, four, five)
print(names)