from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name

    @abstractmethod
    def example(self) -> None:
        print("Classe-base abstrata")

    @abstractmethod
    def print_role(self) -> None:
        pass


class Seller(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def name(self):
        return super().name

    def example(self) -> None:
        print("subclasse")
        return super().example()

    def print_role(self) -> None:
        return "Meu cardo é de vendedor"


seller = Seller("Alexandre")
seller.example()
print(seller.name())
print(seller.print_role())


class Manager(Person):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def example(self) -> None:
        return super().example()

    def name(self):
        pass

    def print_role(self) -> None:
        return "Meu cargo é de gerente"


manager = Manager("Alexandre")
print(manager.print_role())


class Employee:
    def calculate_salaty(self) -> float:
        raise NotImplementedError("Employee deriivated must be implement")


class Analyst(Employee):
    pass


# analyst = Analyst()
# analyst.calculate_salaty()


class Product:
    def print_price(self):
        raise NotImplementedError


class Book(Product):
    def __init__(self, price: int) -> None:
        super().__init__()
        self.price = price

    def print_price(self):
        print(self.price)


book = Book(10)
book.print_price()
