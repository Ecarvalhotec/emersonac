Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
//  
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 06/02/2023
Var
// Se��o de Declara��es das vari�veis 
   salario, prestacao :real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 
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