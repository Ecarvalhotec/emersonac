import json

# Definindo as entidades que precisam ser modeladas e seus atributos
class Funcionario:
    def __init__(self, id, nome, salario, departamento_id):
        self.id = id
        self.nome = nome
        self.salario = salario
        self.departamento_id = departamento_id

class Departamento:
    def __init__(self, id, nome, localizacao):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao

# Criando um diagrama de relacionamento para representar os relacionamentos entre as entidades
# O relacionamento é um para muitos: um departamento pode ter vários funcionários, mas cada funcionário só pode estar em um departamento.

# Criando as classes em Python correspondentes às entidades e seus atributos
# As classes devem ter os mesmos atributos definidos no diagrama de relacionamento.
class Funcionario:
    def __init__(self, id, nome, salario, departamento_id):
        self.id = id
        self.nome = nome
        self.salario = salario
        self.departamento_id = departamento_id

class Departamento:
    def __init__(self, id, nome, localizacao):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao

# Criando uma lista de objetos das classes criadas com dados fictícios
# Esses objetos serão usados para criar o arquivo JSON
funcionarios = [
    Funcionario(1, "Ana", 2500, 1),
    Funcionario(2, "Bruno", 3500, 1),
    Funcionario(3, "Carlos", 4500, 2),
    Funcionario(4, "Denise", 5500, 2),
    Funcionario(5, "Eduardo", 6500, 2)
]

departamentos = [
    Departamento(1, "Vendas", "São Paulo"),
    Departamento(2, "Marketing", "Rio de Janeiro")
]

# Criando um dicionário contendo a lista de objetos e seus atributos
dados = {
    "funcionarios": [vars(funcionario) for funcionario in funcionarios],
    "departamentos": [vars(departamento) for departamento in departamentos]
}

# Salvando o dicionário em um arquivo JSON
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json)
