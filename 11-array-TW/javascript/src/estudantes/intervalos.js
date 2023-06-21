module.exports = {
    calcula: listaArray => calculaIntervalos(listaArray) 
}

function calculaIntervalos(arr){
    
    if (typeof(arr) != "Array"){return "Nao e um array"} 
    
    if (arr.length === 0) {
        return "Array Vazio"
    }
    
    for (let i = 0; i < arr.length; i++){
        if( typeof(arr[i]) !== "Number"){ 
            return "Dados invalidos"
        }

        let primeiroNumero = arr[0]
        if (arr[i + 1] == arr[i] + 1) {

        }
    }


}
