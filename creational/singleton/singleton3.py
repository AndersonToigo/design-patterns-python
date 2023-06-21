# Implementação do padrão Singleton

# Exemplo 3:
class Person(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]
    
class Person(metaclass=Person):
    def __init__(self):
        self.__name = ''

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    def setName(self, value):
        self.__name = value
    
    def __str__(self):
        return str(self.__name)
    
    def __repr__(self):
        return self.__str__()
    

if __name__ == '__main__':
    person = Person()
    print(f'Person: {person}')
    person.setName('Fulano')
    print(f'Person: {person}')

    person2 = Person()
    print(f'Person2: {person2}')
    person2.setName('Tal')
    print(f'Person2: {person2}')
    print(f'Person: {person}')
    print(f'Person é igual a Person2? {person == person2}')