import sys


class ListArray:
    def __init__(self):
        self.data = []

    # subscribe python methods
    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    # return element at index position
    def get(self, index):
        return self.data[index]

    # insert element at index position
    def set(self, index, value):
        self.data.insert(index, value)

    def remove(self, index):
        return self.data.pop(index)

    def update(self, index, value):
        self.data[index] = value
        return self.data[index]


array = ListArray()

array.set(0, "Felipe")
array.set(1, "Ana")
array.set(2, "Shirley")
array.set(3, "Miguel")
print("-----")
array.remove(0)
array.update(2, "Update")
print(array.get(0))
print(array.get(2))
print("-----")

index = 0

while index < len(array):
    print("Index:", index, ", Name:", array.get(index))
    index += 1

array_memoty_size = sys.getsizeof(array.data)
print(array_memoty_size)

array.set(4, "Alberto")
array.set(5, "Marta")
array.set(6, "Túlio")
array.set(7, "Michelle")

array_memoty_size = sys.getsizeof(array.data)
print(array_memoty_size)
