menor= 0
for i in range(5):
   numero = int(input("Digite um número: "))
   if menor == 0:
    menor = numero
   elif numero <= menor:
    menor = numero
    print("o numero inserido menor foi:",menor) 
    
   
