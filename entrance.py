entradas = [1, 2, 3]
saidas = [3, 2, 7]
instante_buscado = 4
resultado: 1

# O estudante 1 entrou no instante 1 e saiu no 3, já o segundo entrou
# e saiu no 2 e o último foi único a estar presente no instante 4.


def entrance(entry, exit, instante):
    count = 0
    for index, n in enumerate(entry):
        if instante >= n and instante <= exit[index]:
            count += 1
    print(count)


entrance(entradas, saidas, instante_buscado)