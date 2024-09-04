# Exemplo 1:
produtos = [1, 3, 1, 1, 2, 3]
resultado = 4
# Os índices (0, 2), (0, 3), (1, 5), (2, 3) formam combinações.

# Exemplo 2:
produtos = [1, 1, 2, 3]
resultado = 1
# Os índices (0, 1) formam a única combinação.


def arrange_producy(array):
    arrange = set()
    for index_a, n in enumerate(array):
        for index, _ in enumerate(array):
            if n == array[index]:
                if index_a < index:
                    arrange.add((index_a, index))

    print(len(sorted(arrange)))


arrange_producy([1, 3, 1, 1, 2, 3])
arrange_producy([1, 1, 2, 3])