import json

slovar = {
    123456: ('Vlad', '21'),
    123457: ('Maks', '22'),
    123458: ('Misha', '23'),
    123459: ('Boris', '24'),
    123450: ('Artem', '25'),
    123451: ('Semen', '26')
}
with open ('data_file.json', 'w') as write_file:
    json.dump(slovar, write_file, indent = 4)
