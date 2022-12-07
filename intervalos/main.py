# Intervalos (https://dojopuzzles.com/problems/intervalos/)
#
# Este problema foi utilizado em 313 Dojo(s).
#
# Dado uma lista de números inteiros, agrupe a lista em um conjunto de intervalos
#
# Exemplo:
#
# Entrada: 100, 101, 102, 103, 104, 105, 110, 111, 113, 114, 115, 150
#
# Saída: [100-105], [110-111], [113-115], [150]



def intervals(numbers_list):
    #return [[numbers_list[0], numbers_list[-1]]]
    interval = []
    output = []
    secundary = []

    for position, i in enumerate(numbers_list):
        if position == 0 or position == 1:
            interval.append(i)
        elif i == interval[-1] + 1:
            interval[-1] = i
        elif i != interval[-1] + 1:
            secundary.append(i)

    if interval:
        output.append(interval)
    if secundary:
        output.append(secundary)

    return output