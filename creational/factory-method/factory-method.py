from abc import ABC, abstractmethod
from typing import Union


"""
A classe Transport é uma classe abstrata definida usando o módulo ABC e os decoradores @abstractmethod. 
Isso significa que não é possível criar uma instância direta da classe Transport, mas deve ser usada como uma classe base para classes de transporte específicas. 
Além disso, as classes que herdam de Transport devem implementar os métodos send() e get_price().

As classes AirPlane, Ship, Train e Truck herdam da classe Transport e fornecem implementações para os métodos abstratos send() e get_price(). 
Cada classe substitui os métodos abstratos para imprimir informações específicas do meio de transporte correspondente.

A implementação dos métodos send() e get_price() nas classes derivadas consiste em imprimir mensagens no console. 
Isso parece ser apenas uma representação básica das ações realizadas por cada meio de transporte e os preços associados.

Em resumo, o código estabelece uma estrutura básica para representar diferentes meios de transporte e fornece métodos abstratos que devem ser implementados nas classes derivadas. 
"""
class Transport(ABC):
    @abstractmethod
    def send(self) -> None:
        pass

    @abstractmethod
    def get_price(self) -> None:
        pass

class AirPlane(Transport):
    def send(self):
        print('Enviando Avião')
    
    def get_price(self):
        print("Preço: R$3.000,00")

class Ship(Transport):
    def send(self):
        print('Enviando Navio')
    
    def get_price(self):
        print("Preço: R$2.000,00")

class Train(Transport):
    def send(self):
        print('Enviando Trem')
    
    def get_price(self):
        print("Preço: R$1.500,00")

class Truck(Transport):
    def send(self):
        print('Enviando Caminhão')

    def get_price(self):
        print("Preço: R$1.000,00")


"""
A classe Logistic é uma classe abstrata definida usando o módulo ABC e os decoradores @abstractmethod. Ela define dois métodos abstratos: create_transport() e type_logistic(). 
Além disso, possui os métodos deliver() e get_price(), que chamam os métodos send() e get_price() da classe de transporte associada.

As classes AirLogistic, TerrainLogistic e SeaLogistic herdam da classe Logistic e fornecem implementações para os métodos abstratos create_transport() e type_logistic(). 
Cada classe define um tipo específico de logística (aérea, terrestre ou marítima) e associa uma classe de transporte específica.

A classe AirLogistic possui o método create_transport() que define a classe de transporte como AirPlane, que é associada à logística aérea.

A classe TerrainLogistic possui o método create_transport() que recebe um objeto de transporte (do tipo Train ou Truck) 
e associa esse objeto como a classe de transporte para a logística terrestre.

A classe SeaLogistic possui o método create_transport() que define a classe de transporte como Ship, associada à logística marítima.

No geral, o código fornece uma estrutura básica para implementar diferentes tipos de logística. A classe Logistic define a interface comum e os métodos para entrega e obtenção de preço. 
As classes derivadas específicas implementam os métodos abstratos para configurar o tipo de logística e associar a classe de transporte apropriada. 
"""
class Logistic(ABC):
    @abstractmethod
    def create_transport(self) -> None:
        pass

    @abstractmethod
    def type_logistic(self) -> None:
        pass

    def deliver(self) -> None:
        self.transport().send()
    
    def get_price(self) -> None:
        self.transport().get_price()

class AirLogistic(Logistic):
    def create_transport(self):
        self.transport = AirPlane
    
    def type_logistic(self):
        print("Logistica Aérea")

class TerrainLogistic(Logistic):
    def create_transport(self, transport: Union[Train, Truck]):
        self.transport = transport
    
    def type_logistic(self):
        print("Logistica Terrestre")

class SeaLogistic(Logistic):
    def create_transport(self):
        self.transport = Ship
    
    def type_logistic(self):
        print("Logistica Marítima")


"""
São criadas instâncias das classes de logística específicas, como AirLogistic, TerrainLogistic e SeaLogistic, e os métodos create_transport(), type_logistic(), deliver() e get_price() 
são chamados para cada instância.

Primeiro, é criada uma instância de AirLogistic e é chamado o método create_transport() para configurar o transporte como um avião. 
Em seguida, são chamados os métodos type_logistic(), deliver() e get_price() para exibir as informações sobre a logística aérea e realizar a entrega.

Depois, é criada uma instância de TerrainLogistic e o método create_transport() é chamado com o argumento Truck para configurar o transporte como um caminhão. 
Os métodos type_logistic(), deliver() e get_price() são chamados novamente para exibir as informações sobre a logística terrestre e realizar a entrega.

Uma segunda instância de TerrainLogistic é criada, mas desta vez o método create_transport() é chamado com o argumento Train para configurar o transporte como um trem. 
Os métodos type_logistic(), deliver() e get_price() são chamados novamente para exibir as informações sobre a logística terrestre e realizar a entrega.

Por fim, é criada uma instância de SeaLogistic e o método create_transport() é chamado para configurar o transporte como um navio. 
Os métodos type_logistic(), deliver() e get_price() são chamados novamente para exibir as informações sobre a logística marítima e realizar a entrega.

No geral, o código demonstra como criar instâncias das classes de logística e transporte e chamar seus métodos para exibir informações e realizar operações específicas de cada tipo de logística. 
"""
if __name__ == '__main__':
    logistic = AirLogistic()
    logistic.create_transport()
    logistic.type_logistic()
    logistic.deliver()
    logistic.get_price()

    print()

    logistic = TerrainLogistic()
    logistic.create_transport(Truck)
    logistic.type_logistic()
    logistic.deliver()
    logistic.get_price()

    print()

    logistic = TerrainLogistic()
    logistic.create_transport(Train)
    logistic.type_logistic()
    logistic.deliver()
    logistic.get_price()

    print()

    logistic = SeaLogistic()
    logistic.create_transport()
    logistic.type_logistic()
    logistic.deliver()
    logistic.get_price()
