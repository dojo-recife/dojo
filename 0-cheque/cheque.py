# coding: utf-8
from decimal import Decimal
from operator import mul

labels = {
    'zero': 0,
    'um': 1,
    'dois': 2,
    'três': 3,
    'quatro': 4,
    'cinco': 5,
    'seis': 6,
    'sete': 7,
    'oito': 8,
    'nove': 9,
    'dez': 10,
    'onze': 11,
    'doze': 12,
    'treze': 13,
    'quatorze': 14,
    'catorze': 14,
    'quinze': 15,
    'dezesseis': 16,
    'dezessete': 17,
    'dezoito': 18,
    'dezenove': 19,
    'vinte': 20,
    'trinta': 30,
    'quarenta': 40,
    'cinquenta': 50,
    'sessenta': 60,
    'setenta': 70,
    'oitenta': 80,
    'noventa': 90,
    'cem': 100,
    'cento': 100,
    'duzentos': 200,
    'trezentos': 300,
    'quatrocentos': 400,
    'quinhentos': 500,
    'seiscentos': 600,
    'setecentos': 700,
    'oitocentos': 800,
    'novecentos': 900,
    'mil': 1000,
    'milhão': 1000000,
    'bilhão': 1000000000,
    'milhões': 1000000,
    'bilhões': 1000000000,
    'e': '+',
}

stop_words = {
    
}

def cheque(valor):
    if 'real' in valor:
        return '1.00'
    valores = valor.split(' reais')[0].split(' de')[0].split(' e ')
    resultado = 0
    # cinquenta e tres
    # 50 + 3
    for valor in valores:
        numeros = valor.split()
        if len(numeros) == 2:
            resultado += mul(*(labels[n] for n in numeros))
        else:
            resultado += labels[valor]
    
    return '%.2f' % resultado