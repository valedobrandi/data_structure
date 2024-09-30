# from typing import Union


# class Blender:
#     AVAILABLE_COLORS = {"VERMELHO", "ROSA", "PRETO", "BRANCO"}

#     # Getter

#     @property
#     def color(self) -> str:

#         return self.__color.upper()

#     @color.setter  # Repare que é @color.setter, e não @property.setter
#     def color(self, new_color: str) -> None:

#         if new_color.upper() not in self.AVAILABLE_COLORS:

#             raise ValueError(f"A cor '{new_color}' não está disponível")

#         self.__color = new_color

#     def __init__(
#         self,
#         color: str,
#         power: int,
#         voltage: int,
#         price: Union[float, int],
#     ) -> None:
#         # Observe que usamos o setter para já validarmos o primeiro valor
#         self.set_color(color)

#         # Demais variáveis omitidas para este exemplo


# blender = Blender("Azul", 110, 127, 200)

# print(f"A cor atual é {blender.__color}")
# AttributeError: 'Blender' object has no attribute '__color'

# print(f"A cor atual é {blender.get_color()}")
# # A cor atual é AZUL
# blender.set_color("Preto")
# print(f"Após pintarmos, a nova cor é {blender.get_color()}")
# # Após pintarmos, a nova cor é PRETO
# blender.get_color()


class MonthlyExpense:
    def __init__(self, internet, grocery, power, water, rent) -> None:
        self.internet = internet,
        self.grocery = grocery,
        self._power = power,
        self._water = water,
        self.__rent = rent

    @property
    def rent(self):
        return self.__rent

    @rent.setter
    def rent(self, state: bool):
        self.__rent = state
        
    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, state: bool):
        self._power = state


expense = MonthlyExpense(rent=True, internet=True, grocery="Extra", power=False, water=2)
print(expense.rent)
expense.rent = False
print(expense.rent)
print(expense.power)
expense.power = True
print(expense.power)
