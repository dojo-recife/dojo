const lerPalavra = require('./index')
describe('Testes para alunos', () => {
    it('Deve retornar true para a', () => {
        expect(lerPalavra.verificaPalavraPrima("a"))
            .toEqual(true)
    })

    it('Deve retornar false para d', () => {
        expect(lerPalavra.verificaPalavraPrima("d"))
            .toEqual(false)
    })

    it('Deve retornar  para A', () => {
        expect(lerPalavra.verificaPalavraPrima("A"))
            .toEqual(false)
    })

    it('Deve retornar  para oi', () => {
        expect(lerPalavra.verificaPalavraPrima("oi"))
            .toEqual(false)
    })

    it('Deve retornar  para da', () => {
        expect(lerPalavra.verificaPalavraPrima("da"))
            .toEqual(true)
    })

    it('Deve retornar  para Ana', () => {
        expect(lerPalavra.verificaPalavraPrima("Ana"))
            .toEqual(false)
    })

    it('Deve retornar  para MUljdo', () => {
        expect(lerPalavra.verificaPalavraPrima("MUljdo"))
            .toEqual(true)
    })

it('Deve retornar  para zzzzzzzzz', () => {
        expect(lerPalavra.verificaPalavraPrima("zzzzzzzzz"))
            .toEqual(false)
    })






})