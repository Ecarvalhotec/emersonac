import json

# Função para carregar os dados do arquivo JSON
def carregar_dados():
    with open('funcionarios_departamentos.json') as arquivo:
        dados = json.load(arquivo)
        return dados

# Função para listar todos os funcionários
def listar_funcionarios():
    dados = carregar_dados()
    for funcionario in dados['funcionarios']:
        print(funcionario['nome'])

# Função para exibir informações de um funcionário específico
def exibir_informacoes_funcionario(id_funcionario):
    dados = carregar_dados()
    for funcionario in dados['funcionarios']:
        if funcionario['id'] == id_funcionario:
            print('Nome:', funcionario['nome'])
            print('Idade:', funcionario['idade'])
            print('Cargo:', funcionario['cargo'])

# Função para listar os funcionários de um departamento específico
def listar_funcionarios_departamento(nome_departamento):
    dados = carregar_dados()
    for departamento in dados['departamentos']:
        if departamento['nome'] == nome_departamento:
            print('Funcionários do departamento de', nome_departamento, ':')
            for id_funcionario in departamento['funcionarios']:
                exibir_informacoes_funcionario(id_funcionario)
                print('---')

# Listar todos os funcionários
print('Lista de funcionários:')
listar_funcionarios()
print('')

# Listar todos os departamentos
print('Lista de departamentos:')
for departamento in carregar_dados()['departamentos']:
    print(departamento['nome'])
print('')

# Exibir informações de um funcionário específico
print('Informações do funcionário com ID 1:')
exibir_informacoes_funcionario(1)
print('')

# Listar os funcionários de um departamento específico
print('Funcionários do departamento de Desenvolvimento:')
listar_funcionarios_departamento('Desenvolvimento')
