from abc import ABC, abstractmethod
from typing import Protocol, Union, Tuple
from queue import Queue


class Employee(ABC):
    @abstractmethod
    def calculate_bonus(self, salary):
        return salary + (salary * 0.1)


class Developer(Employee):
    def calculate_bonus(self, salary):
        return salary + (salary * 0.2)


class Analyst(Employee):
    def calculate_bonus(self, salary):
        return salary + (salary * 0.3)


class Manager(Employee):
    def calculate_bonus(self, salary):
        return salary + (salary * 0.4)


class Customer:
    def __init__(self, name: str, phone: int) -> None:
        self.name = name
        self.phone = phone


class Adress:
    def __init__(self, street: str, number: int, city: str, state: str) -> None:
        self.street = street
        self.number = number
        self.city = city
        self.state = state


class Mail:
    def devilvery(self, customer: Customer, adress: Adress):
        print("Delivered with success")


class ShippingCompany:
    def devilvery(self, customer: Customer, adress: Adress):
        print("Delivered with success")


class Deliverables(Protocol):
    def devilvery(self, customer: Customer, adress: Adress):
        pass


class MessagingProtocol(Protocol):
    def send_message(self, to: str, message: str) -> bool:
        pass

    def receive_message(self) -> Union[str, None]:
        pass


class InMemoryMessaging(MessagingProtocol):
    def __init__(self) -> None:
        self.messages: Queue[Tuple[str, str]] = Queue()

    def send_message(self, to: str, message: str) -> bool:
        self.messages.put((to, message))
        return True

    def receive_message(self) -> Union[str, None]:
        if self.messages.empty():
            return None
        return self.messages.get()


class FileMessaging(MessagingProtocol):
    def __init__(self, file: str) -> None:
        self.file = file

    def send_message(self, to: str, message: str) -> bool:
        with open(self.file, "a") as file:
            file.write(f"{to}:{message}\n")
        return True

    def receive_message(self) -> Union[Tuple[str, str], None]:
        with open(self.file, "r") as file:
            lines = file.readlines()
        if not lines:
            return None
        line = lines[0]
        with open(self.file, "w") as file:
            file.writelines(line[1:])
        return line.split(":"), line.split(":")[1]


def main():
    developer = Developer()
    print(developer.calculate_bonus(100))
    analyst = Analyst()
    print(analyst.calculate_bonus(100))
    manager = Manager()
    print(manager.calculate_bonus(100))
    mail = Mail()
    shippingCompany = ShippingCompany()

    customer = Customer("Alexandre", 199)
    adress = Adress("estrada sem fim", 199, "Salvador", "Bahia")

    shippingCompany.devilvery(customer, adress)
    mail.devilvery(customer, adress)
    in_memory_messaging = InMemoryMessaging()
    file_messaging = FileMessaging("messsages.txt")
    in_memory_messaging.send_message("Julia", "Oi, tudo bem?")
    in_memory_messaging.send_message("Julia", "Como foi o seu dia?")
    in_memory_messaging.send_message("Julia", "Desejo um bom final de semana!")

    file_messaging.send_message("Paulo", "Como tá?")

    file_messaging.send_message("Paulo", "Muito obrigado!")

    file_messaging.send_message("Paulo", "Tenha um ótimo dia!")

    print(in_memory_messaging.receive_message())

    print(in_memory_messaging.receive_message())

    print(in_memory_messaging.receive_message())

    print(file_messaging.receive_message())

    print(file_messaging.receive_message())

    print(file_messaging.receive_message())


if __name__ == "__main__":
    main()
