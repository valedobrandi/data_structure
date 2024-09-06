class Liquidificador:

    def __init__(self, cor, potencia, tensao, preco):
        self.preco = preco
        self.cor = cor
        self._potencia = potencia
        self._tensao = tensao
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    def ligar(self, velocidade):
        if velocidade > self.__velocidade_maxima or velocidade < 0:
            raise ValueError(
                f"Velocidqde deve ester entre 0 e {self.__velocidade_maxima}"
            )
        self.__velocidade = velocidade
        self.__corrente_atual_no_motor = (
            (self._potencia / self._tensao) / self.__velocidade_maxima
        ) * velocidade
        self.__ligado = True

    def desligar(self):
        self.__ligado = False
        self.__velocidade = 0

    def estar_ligado(self):
        return self.__ligado

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("This color dont exist")
        self.__cor = nova_cor


liquidificador_vermelho = Liquidificador("vermelho", 250, 220, 100)
liquidificador_vermelho.ligar(1)
# print("Está ligado?", liquidificador_vermelho.estar_ligado())

liquidificador_vermelho.desligar()
# print("Está ligado?", liquidificador_vermelho.estar_ligado())

liquidificador = Liquidificador("Azul", "110", "127", "200")

# # print(f"A cor atual é {liquidificador.__cor}")

# print(f"A cor atual é {liquidificador.cor}")

liquidificador.cor = "Vermelho"

# print(liquidificador.cor)

# liquidificador.set_cor("turquesa")


class Eletrodomestico:
    def __init__(self, cor, preco=0, tensao=None, potencia=0):
        self.cor = cor
        self.preco = preco
        self.tensao = tensao
        self.potencia = potencia
        self.__ligado = False

    def ligar_desligar(self, action):
        if action:
            self.__ligado = True
            print("ligado")
        else:
            self.__ligado = False
            print("desligado")

    def esta_ligado(self):
        return self.__ligado


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.eletrodomestico = []

    # adiciona

    def __str__(self) -> str:
        return f"""
        {self.nome} = nome
        {self.saldo_na_conta} = saldo_na_conta
        {self.purchased()}        
        """

    def purchased(self):
        return self.eletrodomestico

    def comprar_eletrodomestico(self, eletrodomestico):
        if eletrodomestico.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= eletrodomestico.preco
            self.eletrodomestico.append(eletrodomestico)


class Ventilador(Eletrodomestico):
    def __init__(self, cor, preco, potencia, tensao):
        super().__init__(cor, preco, tensao, potencia)
        self.__ligado = False
        self.__velocidade = 0
        self.__velocidade_maxima = 3
        self.__corrente_atual_no_motor = 0

    @property
    def cor(self):
        return self.__cor.upper()

    @cor.setter
    def cor(self, nova_cor):
        if nova_cor.lower() == "turquesa":
            raise ValueError("This color dont exist")
        self.__cor = nova_cor


ventilador = Ventilador("vermalho", 100, 100, 120)

chef = Pessoa("Bernardo", 2000)

chef.comprar_eletrodomestico(ventilador)
chef.comprar_eletrodomestico(liquidificador_vermelho)

print(chef)


class Aspirador(Eletrodomestico):
    def __init__(self, cor, preco=0, tensao=None, potencia=0):
        # chama ao construtor da superclasse
        super().__init__(cor, preco, tensao, potencia)

    def ligar_desligar(self, action):
        return print("Sim") if super().esta_ligado() else print("Não")


aspirado_azul = Aspirador("azul", preco=150, tensao=120, potencia=500)
""" aspirado_azul.ligar_desligar(True)
aspirado_azul.ligar_desligar(False) """

from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def execute(self, query): ...


class MongoDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mongo")


class MySQLDatabase(Database):
    def execute(self, query):
        print(f"executando query '{query}' no mysql")


class Classe:
    _atributo_da_classe = 1

    @classmethod
    def seta_atributo_da_classe(cls, valor):
        cls._atributo_da_classe = valor

    @classmethod
    def retorna_atributo_da_classe(cls):
        return cls._atributo_da_classe

    @staticmethod
    def método_estático():
        print("Olá")


objeto = Classe()
Classe.método_estático()
objeto.método_estático()

object_one = Classe()
object_two = Classe()
object_one.seta_atributo_da_classe(3)
print(object_one.retorna_atributo_da_classe())
print(object_two.retorna_atributo_da_classe())
