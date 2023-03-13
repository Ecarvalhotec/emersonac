#Escreva um programa que solicite ao usuário a nota de um aluno em uma prova e
#imprima a mensagem "Aprovado" se a nota for maior ou igual a 7, "Reprovado" se a
#nota for menor que 5 e "Recuperação" se a nota estiver entre 5 e 7.
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2

print('Media: ',media)
    
if media<7.0:
        print('Reprovado')
elif media<10:
        print('Aprovado')
else:
        print('Aprovado com Distinção!')