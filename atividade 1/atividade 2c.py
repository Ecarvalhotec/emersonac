#Escreva um programa que leia uma lista de números inteiros e imprima a média
#desses números
num_alunos = 4
nomes = []
notas = []
media = 0
for i in range(num_alunos):
    nomes.append(input('Informe o nome do aluno: '))
    notas.append(float(input('Informe a nota de ' + nomes[i] + ': ')))

media = media / num_alunos
print('A media da turma eh ', media)
for i in range(num_alunos):
    if notas[i] > media:
        print('Parabens', nomes[i])
