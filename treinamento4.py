# Calculadora básica que calcula a média final do aluno.

nmateria = input('Digite o nome da disciplina: ')
nprofessor = input('Digite o nome do professor: ')
ndoaluno = input('Digite o nome do aluno: ')
nmatricula = int(input('Digite o número da matricula do aluno: '))
nparticipacao = int(input('Digite a nota de participação do aluno: '))
ntrabalho = int(input('Digite a nota de trabalho do aluno: '))
ncomportamento = int(input('Digite a nota de comportamento do aluno: '))
nprova = int(input('Digite a nota da prova do aluno: '))

soma = nparticipacao+ntrabalho+ncomportamento+nprova
divisao = soma/4

print('A média final do aluno é: ', divisao)
