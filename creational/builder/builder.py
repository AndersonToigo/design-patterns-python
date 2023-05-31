from typing import Optional


"""
A classe "House" define um projeto para criar objetos com atributos para tipo, paredes e telhado.
"""
class House:
    def __init__(self):
        self.type: Optional[str] = None
        self.walls: Optional[str] = None
        self.roof: Optional[str] = None

    def __str__(self) -> str:
        return f"Type: {self.type}\n" \
               f"Walls: {self.walls}\n" \
               f"Roof: {self.roof}"


"""
A classe BuilderHouse é um projeto para criar um objeto House com métodos para definir seu tipo, construir paredes e construir um telhado.
"""
class BuilderHouse:
    def __init__(self):
        self.house: Optional[House] = None

    def create_house(self) -> None:
        self.house = House()
    
    def set_type(self) -> None:
        pass

    def build_walls(self) -> None:
        pass

    def build_roof(self) -> None:
        pass


"""
A classe BuilderStone é um projeto para criar uma casa de pedra com métodos para definir seu tipo, construir paredes e construir um telhado.
"""
class BuilderStone(BuilderHouse):
    def set_type(self) -> None:
        self.house.type = "Stone"

    def build_walls(self) -> None:
        self.house.walls = "Stone walls"

    def build_roof(self) -> None:
        self.house.roof = "Stone roof"
    


"""
A classe BuilderWood é um projeto para criar uma casa de madeira com métodos para definir seu tipo, construir paredes e construir um telhado.
"""
class BuilderWood(BuilderHouse):
    def set_type(self) -> None:
        self.house.type = "Wood"

    def build_walls(self) -> None:
        self.house.walls = "Wood walls"

    def build_roof(self) -> None:
        self.house.roof = "Wood roof"


"""
A classe ConstructionDirector é um projeto para criar uma casa com métodos para construir uma casa.
"""
class ConstructionDirector:
    def build_house(self, builder: BuilderHouse) -> House:
        builder.create_house()
        builder.set_type()
        builder.build_walls()
        builder.build_roof()
        return builder.house


"""
A classe main é um projeto para criar uma casa de pedra e uma casa de madeira.
"""
if __name__ == '__main__':
    # Criando uma casa de pedra
    stone_builder = BuilderStone()
    director = ConstructionDirector()
    stone_house = director.build_house(stone_builder)

    # Criando uma casa de madeira
    wood_builder = BuilderWood()
    wood_house = director.build_house(wood_builder)

    # Mostrando as casas construídas
    print("Stone House:")
    print(stone_house)

    print("\nWooden House:")
    print(wood_house)
