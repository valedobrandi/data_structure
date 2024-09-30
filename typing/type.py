from typing import Union, List
from typing import Any


def add_two_numbers(num1: int, num2: int) -> int:
    return num1 + num2


# print(add_two_numbers(1, 2.0))


class HomeAppliance:
    def __init__(
        self, color: str, power: int, voltage: int, price: Union[float, int]
    ) -> None:
        self.color = color
        self.price = price
        self.power = power
        self.voltage = voltage
        self.max_speed = 3

        # Inicia os valores de `speed` e `is_on`
        # chamando o método `turn_off` direto no construtor
        self.turn_off()

    def turn_on(self, speed: int) -> None:
        self.is_on = True
        self.speed = speed if speed <= self.max_speed else self.max_speed

    def turn_off(self) -> None:
        self.is_on = False
        self.speed = 0


class Blender(HomeAppliance):
    def is_on(self) -> str:
        return "Sim" if super().is_on() else "Não"


class Fan(HomeAppliance):
    def __init__(
        self,
        color: str,
        power: int,
        voltage: int,
        price: float | int,
        amount_of_fan_speed=1,
    ) -> None:
        super().__init__(color, power, voltage, price)
        self.amount_of_fan_speed = amount_of_fan_speed


class Person:
    def __init__(self, name: str, age: int, height: float, account_balance: float):
        self.name = name
        self.age = age
        self.height = height
        self.account_balance = account_balance
        self.blender: Blender | None = None
        self.home_apliances = List[HomeAppliance] = []

    def buy_home_apliance(self, home_apliance: HomeAppliance) -> None:
        if home_apliance.price <= self.account_balance:
            self.account_balance -= home_apliance
            self.home_apliances.append(home_apliance)

    def buy_blender(self, blender: Blender) -> None:
        if blender.price <= self.account_balance:
            self.account_balance -= blender.price
            self.blender = blender


person = Person("Jacquin", 35, 1.80, 1000.0)
red_blender = Blender("red", 1000, 220, 350.0)
person.buy_blender(red_blender)


class SuperClass:
    def do_something(self, value: Any) -> None:
        print(value)


class SubClass(SuperClass):
    def do_another_thing(self) -> None:
        print("SuperClass")
        super().do_something(value=1)


# sub_object = SubClass()
# sub_object.do_another_thing()


class Vehicle:
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity

    def move(self, distance: int) -> str:
        return (
            f"{self.name} carried {self.capacity} people across {distance} kilometers."
        )


class Car(Vehicle):
    def __init__(self, name: str, capacity: int) -> None:
        super().__init__(name, capacity)

    def move(self, distance: int) -> str:
        return "One car have named" + super().move(distance)


car = Car("Dacia", 5)
print(car.move(10))


class Motocycle(Vehicle):
    def __init__(self, name: str) -> None:
        super().__init__(name, 2)


moto = Motocycle("Honda")
print(moto.move(5))


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        return f"{self.name} fazendo som"


class Mammal(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def breastfeed(self):
        pass


class Dog(Mammal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def bak(self):
        return f" {self.name} Au au!"


catucha = Dog("catucha")
catucha.breastfeed()
print(catucha.bak())


class Rectangle:
    def __init__(self, base: float, height: float) -> None:
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return self.base * self.height

    def calculate_perimeter(self) -> float:
        return 2 * (self.base + self.height)


rectangle = Rectangle(base=5.0, height=10.0)

print(rectangle.calculate_area())
rectangle.calculate_perimeter()
