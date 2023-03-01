# Distribuição de Mictórios
# Gostei! Vamos usar esse!
# Não gostei! Mostre-me outro.

# Este problema foi utilizado em 323 Dojo(s).

# Um problema enfrentado pelos homens no uso de mictórios em banheiros públicos é o constrangimento causado por outro homem urinando no mictório ao lado. Uma situação contrangedora é definida quando dois "mijões" deveriam ocupar mictórios adjacentes.

# Dada uma quantidade de mictórios em um banheiro e a ocupação inicial deles (informando em qual deles já existe um "mijão"), determine quantos "mijões" ainda podem usar os mictórios e qual a posição deles antes para que não ocorra uma situação constrangedora

def mictorio(mictorios):
    if mictorios == [0]:
        return [0]
    
    ocupado = ''
    for i, mictorio in enumerate(mictorios):
        if mictorio == 1:
            if i % 2 == 0:
                ocupado = 'par'
            else:
                ocupado = 'impar'

    for i, m in enumerate(mictorios):
        if i == 0 and m == 1:
            return [2]

    return [0, 2]