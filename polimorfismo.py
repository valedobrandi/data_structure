from typing import Optional
from typing import Union


class Person:
    def __init__(
        self,
        name: str,
        age: Optional[int] = None,
        account_balance: Optional[int] = None,
    ) -> None:
        self.age = age
        self.name = name
        self.account_balance = account_balance


person_1 = Person("Marcelo", 22, 700)
person_2 = Person("Matheus")
person_3 = Person("Maria", 33)
person_4 = Person("Márcia", account_balance=100)


class Blender:
    AVAILABLE_COLORS = {"VERMELHO", "ROSA", "PRETO", "BRANCO"}

    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: Union[float, int],
    ) -> None:
        # Observe que usamos o setter para já validarmos o primeiro valor
        self.color = color
        # Demais variáveis omitidas para este exemplo

    @property
    def color(self) -> str:
        return self.__color.upper()

    @color.setter
    def color(self, new_color: str) -> None:
        if new_color.upper() not in self.AVAILABLE_COLORS:
            raise ValueError(f"A cor '{new_color}' não está disponível")
        self.__color = new_color


class Product:
    def __init__(self, name, price) -> None:
        self._name = (name,)
        self._price = price

    def get_description(self):
        pass

    def get_price(self):
        pass


class Book(Product):
    def __init__(self, name, price, author) -> None:
        super().__init__(name, price),
        self._author = author

    def get_description(self):
        return f"{self._name} por {self._author}"

    def get_price(self):
        return self._price


class DVD(Product):
    def __init__(self, name, price, director) -> None:
        super().__init__(name, price),
        self._director = director

    def get_description(self):
        return f"{self._name} por {self._director}"

    def get_price(self):
        return self._price


def print_detail():
    new_book = Book("O Senhor dos Anéis", "J.R.R. Tolkien", 29.99)
    new_dvd = DVD("O Poderoso Chefão", "Francis Ford Coppola", 19.99)

    print(new_dvd.get_description())
    print(new_book.get_description())


print_detail()


class Tv:
    def __init__(
        self,
        tamanho,
        volume=50,
        canal=1,
        ligada=False,
    ) -> None:
        self.__volume = (volume,)
        self.__canal = (canal,)
        self.tamanho = (tamanho,)
        self.__ligada = ligada

    def ligar_desligar(self):
        self.ligada = not self.__ligada

    @property
    def volume(self):
        return self.__volume

    def aumentar_volume(self):
        if self.__volume > 0 and self.__volume < 100:
            self.__volume += 1

    def diminuir_volume(self):
        if self.__volume > 0 and self.__volume < 100:
            self.__volume -= 1

    @property
    def canal(self):
        return self.__canal

    def modificar_canal(self, canal):
        if canal > 1 and canal < 100:
            self.__canal = canal
            return
        return ValueError
