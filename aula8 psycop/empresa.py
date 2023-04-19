import psycopg2

# Define os parâmetros de conexão ao banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="Empresa",
    user="postgres",
    password="bispo"
)

# Cria um cursor para executar as operações no banco de dados
cur = conn.cursor()

# Cria a tabela de funcionários
cur.execute("""
    CREATE TABLE funcionarios (
        id_funcionario SERIAL PRIMARY KEY,
        nome VARCHAR(255) NOT NULL,
        idade INT,
        cargo VARCHAR(255)
    );
""")

# Cria a tabela de salários
cur.execute("""
    CREATE TABLE salarios (
        id_salario SERIAL PRIMARY KEY,
        id_funcionario INT NOT NULL,
        salario FLOAT,
        FOREIGN KEY (id_funcionario) REFERENCES funcionarios (id_funcionario)
    );
""")

# Insere alguns dados na tabela de funcionários
cur.execute("""
    INSERT INTO funcionarios (nome, idade, cargo)
    VALUES ('João Silva', 30, 'Gerente'),
           ('Maria Santos', 25, 'Analista de RH'),
           ('Pedro Alves', 40, 'Programador');
""")

# Insere alguns dados na tabela de salários
cur.execute("""
    INSERT INTO salarios (id_funcionario, salario)
    VALUES (1, 5000),
           (2, 3500),
           (3, 6000);
""")

# Confirma as alterações no banco de dados
conn.commit()

# Fecha o cursor e a conexão com o banco de dados
cur.close()
conn.close()
