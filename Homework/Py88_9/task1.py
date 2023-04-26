from dataclasses import dataclass


@dataclass
class Human:
    name: str
    surname: str

    @staticmethod
    def hello():
        print(f'hello, {human.name}')

    @staticmethod
    def hello1():
        print(f'hello, {man.name}')

    @classmethod
    def call_me(cls):
        return print(f'call_me {cls}')


human = Human('Vlad', 'Zhidik')
print(human)
human.call_me()
Human.hello()
Man = type('Man', (Human, ), {human.name: str, human.surname: str})
man = Man('Maks', 'Mesha')
print(man)
man.hello1()
