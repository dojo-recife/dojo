module.exports = {
    soma: notas => somaLocal(notas)
}

function somaLocal(notas){
    if(Math.min(...notas)){
        var resultado = notas.reduce((acc,nota) => {
             acc += nota
             return acc
         },0)
         return notas.length > 5 ? resultado *2 : resultado
     }

     return 0
 }

