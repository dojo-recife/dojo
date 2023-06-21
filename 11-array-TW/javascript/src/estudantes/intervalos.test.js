const intervalos = require('./intervalos')

describe('Testes para arrays', () => {
    it('Deve retornar "Dados invalidos" caso algum item do array nao seja do tipo number', () => {
        const entrada = [1, 2, 3, 'a', 5]
        expect(intervalos.calcula(entrada)).toEqual("Dados invalidos")

    })

    it('Verificar se o array eh vazio', () => {
        const entrada = []
        expect(intervalos.calcula(entrada)).toEqual("Array Vazio")

    })

    it('Verificar tipo de entrada',() => {
        const entrada = "entrada"
        expect(intervalos.calcula(entrada)).toEqual("Nao e um array")
    })

    it('Se numero for igual',() => {
        const entrada = [1,1]
        expect(intervalos.calcula(entrada)).toEqual("O numero e igual")
    })










    // it('Deve retornar o intervalo um array com 1 e 3', () => {
    //     const entrada = [1, 2, 3]
    //     expect(intervalos.calcula(entrada).toEqual("[1, 3]"))
    // }) // it('Deve retornar o intervalo um array com 1 e 3', () => {
    //     const entrada = [1, 2, 3]
    //     expect(intervalos.calcula(entrada).toEqual("[1, 3]"))
    // })
})
    
