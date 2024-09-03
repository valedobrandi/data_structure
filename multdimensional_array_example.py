from array_example import ListArray


class Matrix(ListArray):

    def get(self, row, column):
        return self.data[row][column]

    def set(self, row, column, value):
        # if line dont exist create a new one
        try:
            self.data[row].insert(column, value)
        except IndexError:
            self.data.insert(row, [value])

    def remove(self, row, column):
        return self.data[row].pop(column)


print("----- Arrays multidimensionais")

array = Matrix()

array.set(0, 0, "Marcos")
array.set(0, 1, 6)
array.set(0, 2, 9)
print(array)

array.set(1, 0, "Patrícia")
array.set(1, 1, 9)
array.set(1, 2, 6)
print(array)

array.remove(0, 2)
print(array)
