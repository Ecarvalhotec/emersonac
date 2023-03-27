class Animal:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def emitirSom(self):
        print("Rosnar")

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print ("auau")

class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print ("miau")

class Pato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
    def emitirSom(self):
        print ("Quack, Quack")

objCachorro = Cachorro("Batata", "2 anos")
objCachorro.emitirSom()

objGato = Gato("Chidori", "5 anos")
objGato.emitirSom()

objPato = Pato("Patolinno", "3 anos")
objPato.emitirSom

objanimal = Animal("Samurai", "30")
objanimal.emitirSom()





