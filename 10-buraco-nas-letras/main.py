def conta_buraco(frase:str):
    contador_buracos = 0
    letras_com_1_buraco = "ADOPQRabdegopq"
    for letra in frase:
        if letra in letras_com_1_buraco:
            contador_buracos += 1
        elif letra == "B":
            contador_buracos += 2
      
    return contador_buracos    
