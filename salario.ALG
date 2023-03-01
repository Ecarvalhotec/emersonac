Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
//  
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Seção de Declarações das variáveis 
   salario, prestacao :real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 
  escreval("digite seu salario")
   leia(salario)
   escreval("digite a parcela")
   leia(prestacao)
   se(prestacao > (salario*0.2)) entao
   escreval("emprestimo negado.", )
   senao
   escreval("emprestimo concedido.")
   fimse
Fimalgoritmo