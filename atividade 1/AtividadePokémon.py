

class Pokémon:
    def __init__(self, nome, tipo, level):
        self.nome = nome
        self.tipo = tipo
        self.level = level
        self.temporada = 1

pokemon1 = Pokémon("Pikachu", "Eletrico,", 20)
pokemon2 = Pokémon("Charmander", "Fogo", 25)
pokemon3 = Pokémon("Bulbasaur", "Planta", 20)

print(pokemon1.level)
print(pokemon2.nome)
print(pokemon1.nome)