import sys
import os
sys.path.append(os.path.abspath("/home/bernardoalbuquerque/Documentos/DEV"))
from linkedlist.node import LinkedList



# export PYTHONPATH=/home/bernardoalbuquerque/Documentos/DEV


class Queue(LinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, value):
        return self.insert_first(value)

    def dequeue(self):
        return self.remove_last()

    def peek(self):
        index = self.get_length()
        return self.get_element_at(index)

    def is_empty(self):
        return super().is_empty()


class Stack(LinkedList):
    def __init__(self):
        super().__init__()
        self._overflow = 99

    def push(self, value):
        if self.get_length() == self._overflow:
            raise OverflowError("Não é possível adicionar outro item à pilha")
        return self.insert_last(value)

    def pop(self):
        return self.remove_last()

    def peek(self):
        index = self.get_length() - 1
        returned_value = self.get_element_at(index)
        return returned_value

    def min_value(self):
        index = self.get_length() - 1
        min_value = self.pop().value
        for _ in range(index):
            cur = self.pop().value
            if cur < min_value:
                min_value = cur
        print(min_value)
        return min_value

    def limit_stack(self, value):
        self._overflow = value

    def is_empty(self):
        return super().is_empty()
