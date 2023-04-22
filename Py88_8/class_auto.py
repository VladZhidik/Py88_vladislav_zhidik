class Auto:
    brand = input(str)
    age = input(int)
    mark = input(str)
    weight = 3
    color = 'Black'

    def move(self):
        print('Move')

    def birthday(self, age):
        age += 1

    def stop(self):
        print('Stop')
