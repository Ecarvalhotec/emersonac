import json

class Funcionario:
    def __init__(self, id, nome, salario, id_departamento):
        self.id = id
        self.nome = nome
        self.salario = salario
        self.id_departamento = id_departamento

class Departamento:
    def __init__(self, id, nome, localizacao):
        self.id = id
        self.nome = nome
        self.localizacao = localizacao

# criando objetos de departamento
dep1 = Departamento(1, "Vendas", "São Paulo")
dep2 = Departamento(2, "Marketing", "Rio de Janeiro")

# criando objetos de funcionário
func1 = Funcionario(1, "João Silva", 3000, 1)
func2 = Funcionario(2, "Maria Souza", 4000, 1)
func3 = Funcionario(3, "Pedro Santos", 5000, 1)
func4 = Funcionario(4, "Julia Ferreira", 3500, 2)
func5 = Funcionario(5, "Fernando Oliveira", 4500, 2)
func6 = Funcionario(6, "Ana Paula Costa", 5500, 2)
func7 = Funcionario(7, "Lucas Mendes", 6000, 2)
func8 = Funcionario(8, "Carla Santos", 4000, 1)
func9 = Funcionario(9, "Márcio Souza", 4500, 1)
func10 = Funcionario(10, "Patrícia Lima", 5000, 2)

# criando lista de objetos
funcionarios = [func1, func2, func3, func4, func5, func6, func7, func8, func9, func10]
departamentos = [dep1, dep2]

# criando dicionário para o arquivo JSON
dados = {
    "funcionarios": [vars(f) for f in funcionarios],
    "departamentos": [vars(d) for d in departamentos]
}

# salvando os dados em um arquivo JSON
with open("dados.json", "w") as arquivo_json:
    json.dump(dados, arquivo_json)

def listar_departamentos():
    for departamento in dados['departamentos']:
        print(departamento['nome'])

def exibir_informacoes_funcionario(id_funcionario):
    for funcionario in dados['funcionarios']:
        if funcionario['id'] == id_funcionario:
            print(f"Nome: {funcionario['nome']}")
            print(f"Idade: {funcionario['idade']}")
            print(f"Cargo: {funcionario['cargo']}")
