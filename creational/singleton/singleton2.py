# Implementação do padrão Singleton

# Exemplo 2:
def singleton(the_class):
    instances = {}
    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    return get_class


@singleton
class Singleton:
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
