# Implementação do Abstract Factory

from abc import ABC, abstractmethod


"""
Esse código define uma classe base abstrata chamada Transport que contém um método abstrato chamado delivery().

Três classes concretas, Truck, Ship e Airplane, herdam de Transport e cada classe define sua própria implementação do método delivery().

A classe Truck imprime "Entrega via caminhão".
Classe do navio print "Entrega via navio".
Aula de avião imprime "Entrega via avião".
Essas implementações indicam os métodos de entrega usados pelo respectivo modo de transporte ao entregar mercadorias em seus destinos.
"""
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(Transport):
    def deliver(self):
        print("Entrega via caminhão")

class Ship(Transport):
    def deliver(self):
        print("Entrega via navio")

class Airplane(Transport):
    def deliver(self):
        print("Entrega via avião")


"""
Esse código define uma classe base abstrata chamada Charge que contém um método abstrato chamado calculate().

Três classes concretas, TruckCharge, ShipCharge e AirplaneCharge, herdam de Charge e cada classe define sua própria implementação do método calculate().

A classe TruckCharge imprime "Calculando frete via caminhão".
A classe ShipCharge imprime "Calculando frete via navio".
A classe AirplaneCharge imprime "Calculando frete via avião".
Essas implementações indicam as diferentes formas de calcular as despesas de envio correspondentes para cada meio de transporte.
"""
class Charge(ABC):
    @abstractmethod
    def calculate(self):
        pass

class TruckCharge(Charge):
    def calculate(self):
        print("Calculando frete via caminhão")

class ShipCharge(Charge):
    def calculate(self):
        print("Calculando frete via navio")

class AirplaneCharge(Charge):
    def calculate(self):
        print("Calculando frete via avião")


"""
Esse código define uma classe base abstrata denominada Logística que contém dois métodos abstratos denominados create_transport() e create_charge().

Três classes concretas, RoadLogistics, SeaLogistics e AirLogistics, herdam de Logistics e cada classe define sua própria implementação dos métodos create_transport() e create_charge().
A classe RoadLogistics retorna uma instância de Truck (presumivelmente um objeto de transporte de caminhão) do método create_transport() e uma instância de TruckCharge (presumivelmente o objeto de frete correspondente) do método create_charge().
A classe SeaLogistics retorna uma instância de Ship (presumivelmente um objeto de transporte de navio) do método create_transport() e uma instância de ShipCharge (presumivelmente o objeto de encargo de remessa correspondente) do método create_charge().
A classe AirLogistics retorna uma instância de Airplane (presumivelmente um objeto de transporte de avião) do método create_transport() e uma instância de AirplaneCharge (presumivelmente o objeto de frete correspondente) do método create_charge().
Essas implementações indicam três maneiras diferentes de criar um objeto de transporte e seu objeto de frete correspondente, para três modos de transporte diferentes.
"""
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    @abstractmethod
    def create_charge(self):
        pass

class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()
    
    def create_charge(self):
        return TruckCharge()
    
class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()
    
    def create_charge(self):
        return ShipCharge()
    
class AirLogistics(Logistics):
    def create_transport(self):
        return Airplane()
    
    def create_charge(self):
        return AirplaneCharge()

 
"""
Esse código define uma função chamada client_code que recebe um criador de argumento, que deve ser um objeto de uma classe herdada da classe base abstrata de Logística.

Dentro da função client_code, dois métodos são chamados no objeto criador: create_transport() e create_charge(). Esses métodos criam instâncias de objetos de transporte e carga, respectivamente, com base no modo de transporte especificado no criador.
Em seguida, o método delivery() é chamado no objeto de transporte, que presumivelmente inicia o processo de entrega. Após a entrega bem-sucedida, o método calculate() é chamado no objeto charge, que calcula a taxa de envio do item entregue.

De forma geral, esta função executa o processo de entrega de um determinado meio de transporte e calcula a cobrança correspondente.
"""
def client_code(creator):
    transport = creator.create_transport()
    charge = creator.create_charge()

    transport.deliver()
    charge.calculate()


# Este código verifica se o módulo atual está sendo executado diretamente e realiza três chamadas de função com seus respectivos objetos logísticos.
if __name__ == "__main__":
    # Início da logística do caminhão.
    print("App: Iniciando com logística de caminhão")
    # Chama a função 'client_code()' com o argumento 'RoadLogistics()', que cria um objeto de transporte logístico do tipo "caminhão".
    client_code(RoadLogistics())
    print()

    # Início da logística do navio.
    print("App: Iniciando com logística de navio")
    # Chama a função 'client_code()' com um argumento 'SeaLogistics()', que cria um objeto de transporte logístico do tipo "navio".
    client_code(SeaLogistics())
    print()

    # Início da logística do avião.
    print("App: Iniciando com a logística de avião")
    # Chama a função 'client_code()' com o argumento 'AirLogistics()', que cria um objeto de transporte logístico do tipo "avião".
    client_code(AirLogistics())
    print()

