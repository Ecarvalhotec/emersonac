algoritmo "teste_glicose"
// Autor: Hélio Andrade da Silva Júnior
var
   nivel_acucar : real
inicio
   escreva("Digite seu nível de açúcar: ")
   leia(nivel_acucar)
   
   limpatela
   se (nivel_acucar < 70) entao
      escreval("Hipoglicemia! Procure um médico urgente!")
   senao
      se (nivel_acucar <= 110) entao
         escreval("Parabéns! Nível normal!")
      senao
         escreval("Hiperglicemia! Você vai morrer!")
      fimse
   fimse
fimalgoritmo