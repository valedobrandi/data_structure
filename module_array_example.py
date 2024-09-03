import sys
from array import array

myarray = array("I")

myarray.insert(0, 5)
myarray.insert(1, 3)
myarray.insert(2, 5)

print(myarray)

myarray.insert(1, 4)

print(myarray)

myarray.pop(0)

print(myarray)

elements = list(range(100))

print(sys.getsizeof(elements))
newarray = array("I", elements)
print(sys.getsizeof(newarray))
print(newarray)
