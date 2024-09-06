import numpy as np

# int empty array

my_array = np.array([], dtype=int)

my_array = np.insert(my_array, 0, 5)
my_array = np.insert(my_array, 1, 3)
my_array = np.insert(my_array, 2, 5)


print(my_array)

my_array = np.insert(my_array, 1, 4)

print(my_array)

my_array = np.delete(my_array, 0)

print(my_array)