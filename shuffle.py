# Exemplo 1:
cartas = [2, 6, 4, 5]
# cartas por parte = 2

resultado = [2, 4, 6, 5]

# Exemplo 2:
cartas = [1, 4, 4, 7, 6, 6]
# cartas por parte = 3

resultado = [1, 7, 4, 6, 4, 6]


def shuffle(array):
    half_length = len(array) // 2
    first_half = array[:half_length]
    second_half = array[half_length:]
    shuflled = []
    for _ in array:
        if len(first_half) > 0:
            shuflled.append(first_half[-1])
            first_half.pop(-1)
        if len(second_half) > 0:
            shuflled.append(second_half[-1])
            second_half.pop(-1)
    return shuflled


print(shuffle([1, 2, 3, 4, 5, 6]))