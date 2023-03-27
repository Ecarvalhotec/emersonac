class pokemon:
    def __init__(self, especie, tipo, hp, movimento):
        self.especie = especie
        self.tipo = tipo
        self.hp = hp
        self.movimento = movimento
    def fazerBarulho(self):
        print(f"{self.especie} fez um barulhinho")

class PokemonFogo(pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)

class PokemonAgua(pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)
        
class PokemonGrama(pokemon):
    def __init__(self, especie, tipo, hp, movimento):
        super().__init__(especie, tipo, hp, movimento)