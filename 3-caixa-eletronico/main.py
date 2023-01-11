def retorna_saque(dinheiros):
    notas = [100, 50, 20, 10]
    saque = []
    for nota in notas:
        if dinheiros % nota == 0:
            qnt_notas = dinheiros // nota
            saque.extend([nota] * qnt_notas)
            dinheiros -= nota * qnt_notas
        elif nota <= dinheiros:
            saque.append(nota)
            dinheiros -= nota

    return saque