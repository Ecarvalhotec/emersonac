# Deve conter as seguintes entidades Funcionários e Departamentos
# Requisitos:
# - Ver lista de funcionários
# - Ver lista de departamentos
# - Ver informações de funcionários específico(Deve conter o Departamento de que faz parte)
# - Ver lista de funcionários de um departamento específico
# - Opcional: Funcionário gerente e autenticação antes de usar o sistema
# - Inserção de Funcionários e Departamentos
# - Atualização de informações de Funcionários e Departamentos
# - Remoção de Funcionários e Departamentos

# Entidade Funcionário:

# Id_Func: integer AUTO GENERATED (PK)
# Nome_Func: char(255) NOT NULL
# Salário_Func: float(2) NOT NULL default 0.00
# Cargo_Func: char(255) NOT NULL default Autônomo
# Id_Departamento: integer (FK)

# Entidade Departamento:

# Id_Departamento: integer AUTO GENERATED (PK)
# Nome_Departamento: char(255)
# #Id_Gerente: integer (FK) (OPCIONAL)

import psycopg2


# #Funções com código de criação das tabelas - Deve ser rodado apenas 1 vez
# def criarTabelaFuncionario():
#     sql = '''
#     CREATE TABLE "Funcionário"(
#     "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     "Nome" varchar(255) NOT NULL,
#     "Salário" money NOT NULL default 0,
#     "Cargo" varchar(255) NOT NULL default 'Autônomo',
#     "Id_Dept" int NOT NULL default 1
#     )
#     '''
#     return sql

# def criarTabelaDepartamento():

#     sql = '''
#     CREATE TABLE "Departamentos"(
#     "Id" int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#     "Nome" varchar(255) NOT NULL
#     -- "Id_Gerente" int NOT NULL default 1
#     )
#     '''
#     return sql

# try:
#     conn = psycopg2.connect(dbname="XYZ Soluções", host="localhost",port="5432",user="postgres", password="postgres")

#     cursor = conn.cursor()

#     cursor.execute(criarTabelaFuncionario())
#     conn.commit()

#     cursor.execute(criarTabelaDepartamento())
#     conn.commit()

#     print("Tabelas criadas.")


# # Código para verificar tabelas que existem no seu DB
# #     cursor.execute('''
# #     SELECT table_name
# #   FROM information_schema.tables
# #  WHERE table_schema='public'
# #    AND table_type='BASE TABLE';
# #     ''')

# #     print(cursor.fetchall())

#     cursor.close()

#     conn.close()

# except(Exception, psycopg2.Error) as error:
#     print("Ocorreu um erro ao tentar a conexão:", error)

def verFuncionarios():

    cursor.execute('''
                SELECT * FROM "Funcionário"
                ORDER BY "Id" ASC
                ''')

    listaFuncionarios = cursor.fetchall()
    print("ID - Nome")
    for funcionario in listaFuncionarios:
        print(f"{funcionario[0]} - {funcionario[1]}")


def verDepartamentos():

    cursor.execute('''
                SELECT * FROM "Departamentos"
                ORDER BY "Id" ASC
                ''')

    listaDepartamentos = cursor.fetchall()
    print("ID - Nome")
    for departamento in listaDepartamentos:
        print(f"{departamento[0]} - {departamento[1]}")

def inserirFuncionario():
    print("Você está cadastrando um funcionário.")

    novoFuncionarioNome = input("Digite o nome do novo funcionário: ")
    novoFuncionarioSalario = input("Digite o salário do novo funcionário: ")
    novoFuncionarioCargo = input("Digite o cargo do novo funcionário: ")
    novoFuncionarioIdDepartamento = input("Digite o departamento do novo funcionário: ")

    cursor.execute(f'''
    INSERT INTO "Funcionário"
    Values(default, '{novoFuncionarioNome}', '{novoFuncionarioSalario}', '{novoFuncionarioCargo}', '{novoFuncionarioIdDepartamento}')
    
    ''')

    conn.commit()

    print("Funcionário Inserido!")

def inserirDepartamento():
    print("Você está cadastrando um departamento.")

    novoDepartamentoNome = input("Digite o nome do novo departamento: ")


    cursor.execute(f'''
    INSERT INTO "Departamentos"
    Values(default, '{novoDepartamentoNome}')
    
    ''')

    conn.commit()

    print("Departamento Inserido!")


try:
    conn = psycopg2.connect(dbname="Empresa", host="localhost",
                            port="5432", user="postgres", password="bispo")

    cursor = conn.cursor()

except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro", error)


while True:
    try:

        print('''
        Bem vindo ao Gerenciamento Empresa

        Escolha uma opção do menu:

        1 - Ver Funcionários
        2 - Ver Departamentos
        3 - Inserir Funcionário
        4 - Inserir Departamento
        0 - Sair
        
        
        ''')

        op = input("Digite a opção escolhida:")

        match op:
            case "1":
                verFuncionarios()

            case "2":
                verDepartamentos()

            case "3":
                inserirFuncionario()

            case "4":
                inserirDepartamento()

            case "0":
                print("Saindo do programa...")
                cursor.close()
                conn.close()
                break
            case _:
                print("Opção inválida. Digite novamente!")

        input("Tecle enter para continuar.")

    except (Exception, psycopg2.Error) as error:

        print("Ocorreu um erro", error)