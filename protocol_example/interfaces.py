from typing import Protocol


class Connection(Protocol):
    """Protocolo de conexão com banco de dados"""

    def execute(self, query: str) -> list[str]:
        """Executa uma query no banco e retorna os dados, caso existem"""
        ...


class Database(Protocol):
    """Protocolo de um bando de dados"""

    def connect(self, connction_url: str) -> Connection:
        """Realiza uma conexão com o banco de dados"""
        ...


class CalculatePerimeter(Protocol):
    def calculate_perimeter(self) -> float:
        pass


class Square(CalculatePerimeter):
    def __init__(self, side: int) -> None:
        self.side = side

    def calculate_perimeter(self) -> float:
        return f"O perímetro do quadrado é de {self.side * 4} cm"


class Triangle(CalculatePerimeter):
    def __init__(self, side_1: int, side_2: int, side_3: int) -> None:
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def calculate_perimeter(self) -> float:
        return 1.0

    def calculate_area(self) -> str:
        return (
            f"O perímetro do triângulo é de"
            f"{self.side_1 + self.side_2 + self.side_3} cm"
        )


class Deliverables(Protocol):
    def devilvery(self, customer: Customer, adress: Adress):
        pass
