Algoritmo "prova"
var
saque: inteiro
inicio
escreva ("Entre com o valor do saque: ")
leia (saque)
escreval ("Número de cédulas de R$ 100: ",saque\100)
saque <- saque - saque\100*100
escreval ("Número de cédulas de R$ 50: ",saque\50)
saque <- saque%50
escreval ("Número de cédulas de R$ 20: ",saque\20)
saque <- saque%20
escreval ("Número de cédulas de R$ 10: ",saque\10)
saque <- saque%10
escreval ("Número de cédulas de R$ 5: ",saque\5)
saque <- saque%5
escreval ("Número de cédulas de R$ 2: ",saque\2)
saque <- saque%2
escreval ("Número de cédulas de R$ 1: ",saque)
fimalgoritmo