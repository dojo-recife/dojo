algarismos = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
}
romanos = {
   value: key for key,value in algarismos.items()
}


def numeros_arabicos_romanos(numero):
    
    
    if numero in algarismos:
        return algarismos[numero] 
    
    contador = ""
    for chave in reversed(algarismos.keys()):
        if chave < numero and numero:
            divisao = int((numero / chave))
            resto = numero % chave
            contador += divisao * algarismos[chave]
            numero = resto
    return contador

def numeros_romanos_arabicos(romano):
    #return romanos[number]
    
    soma= 0

    for item in romano:
        valor = romanos[item]
        soma += valor 
        
    return soma 
        
        
        

