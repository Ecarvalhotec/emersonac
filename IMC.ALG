algoritmo "IMC"
// Disciplina   : [Linguagem e Lógica de Programação] 
// Professor   : Antonio Carlos Nicolodi 
var
    altura, peso, imc: real
inicio
    leia(altura)
    leia(peso)
    imc <- peso / (altura * altura)
    escreva("Seu IMC é: ", imc)
    se imc < 16 entao
        escreva("Magreza grave")
    senao
        se imc < 17 entao
            escreva("Magreza moderada")
        senao
            se imc < 18.5 entao
                escreva("Magreza leve")
            senao
                se imc < 25 entao
                    escreva("Saudável")
                senao
                    se imc < 30 entao
                        escreva("Sobrepeso")
                    senao
                        se imc < 35 entao
                            escreva("Obesidade Grau I")
                        senao
                            se imc < 40 entao
                                escreva("Obesidade Grau II (severa)")
                            senao
                                escreva("Obesidade Grau III (mórbida)")
                            fimse
                        fimse
                    fimse
                fimse
            fimse
        fimse
    fimse
fimalgoritmo