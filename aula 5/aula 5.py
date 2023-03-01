frase = input('Digite uma frase: ')
print(' Você digitou: {}'.format(frase))
invertida = ' '.join(palavra[::-1] for palavra in frase.split())
print('A frase que você digitou invertida fica: {}'.format(invertida))