# Implementação do padrão Singleton

# Exemplo 1 (Este exemplo não é uma boa prática da implementação do padrão Singleton):
class Singleton:
    __instance = None

    def __new__(cls):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        return Singleton.__instance
    
    def __init__(self):
        self.__value = None

    def setValue(self, value):
        self.__value = value
    
    def __str__(self):
        return str(self.__value)
    
    def __repr__(self):
        return self.__str__()
    
if __name__ == '__main__':
    singleton = Singleton()
    print(f'Singleton: {singleton}')
    singleton.setValue(1)
    print(f'Singleton: {singleton}')

    singleton2 = Singleton()
    print(f'Singleton2: {singleton2}')
    singleton2.setValue(2)
    print(f'Singleton2: {singleton2}')
    print(f'Singleton: {singleton}')
