const estudante = require('./estudantes')
describe('Testes para alunos', () => {
    it('Deve retornar 10 quando as notas forem 5,3 e 2', () => {
        const notas = [3,5,2,2,5,1]
        expect(estudante.soma(notas)).toEqual(36)
    })

    it('Deve retornar zero quando uma das notas forem 0', () => {
        const notas = [3,5,2,0]
        expect(estudante.soma(notas)).toEqual(0)
    })

    it('Deve retornar X quando o aluno tiver mais de 5 notas', () => {
        const notas = [3,5,7,8]
        expect(estudante.soma(notas)).toEqual(23)
    })

})