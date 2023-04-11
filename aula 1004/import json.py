import json

with open ('dados.json') as file:
    data = json.load(file)

funcionarios = data['funcionarios']
print (funcionarios)
for funcionario in funcionarios:
    print(f"ID: {funcionario['id']}")
    print(f"Nome: {funcionario['nome']}")
    print(f"CPF: {funcionario['salario']}")
    print(f"ID do departamento: {funcionario['id_departamento']}")
