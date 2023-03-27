class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def informacoes (self):
        print(f'{self.marca} - {self.modelo} - {self.ano}')
    
    def aceleracao(self, velocidade):
        print (f'o carro {self.modelo}, acelerou {velocidade} Km/h')

carro1 = Carro("Fiat TORO", "FIAT", "2017")



carro1.informacoes()
carro1.aceleracao(80)


        

