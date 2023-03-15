// Palavras Primas https://dojopuzzles.com/problems/palavras-primas/
// Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 2, 3, 5, 101, 367 e 523.
//
// Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.
//
// Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.



module.exports = {
    verificaPalavraPrima: palavra => verificaPalavraPrima(palavra)
}

const letras = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
const primos = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]


function verifica_primo(numero){
    let restos = 0
    for(let index=1; index <= numero; index++){
        if (numero%index == 0){
            restos++
        }

    }
    console.log(restos)
    return restos<=2
}
function verificaPalavraPrima(palavra){
    let sum = 0;
    for (let letra of  palavra) {
        let indice = letras.indexOf(letra);
        sum += indice;
    }

     console.log(palavra)
     console.log(sum)


    return verifica_primo(sum);



 }

