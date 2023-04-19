import psycopg2

# Parâmetros de conexão com o banco de dados
db_name = "Empresa"
db_user = "postgres"
db_password = "bispo"
db_host = "localhost"
db_port = "5432"

# Estabelecer conexão com o banco de dados
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Consultar todos os funcionários
cur = conn.cursor()
cur.execute("SELECT * FROM funcionarios")
funcionarios = cur.fetchall()
cur.close()

# Exibir os funcionários
for funcionario in funcionarios:
    print(funcionario)
