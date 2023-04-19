import psycopg2

# Definir a string de conexão com o banco de dados
conn = psycopg2.connect(
    host="localhost",
    database="Empresa",
    user="postgres",
    password="bispo"
)

# Criar um cursor para executar as consultas SQL
cur = conn.cursor()

# Executar uma consulta SQL
cur.execute("SELECT * FROM funcionarios")

# Ler as linhas retornadas pela consulta SQL
rows = cur.fetchall()

# Exibir as linhas lidas
for row in rows:
    print(row)


cur = conn.cursor()
cur.execute("SELECT * FROM funcionarios")
rows = cur.fetchall()
# Fechar o cursor e a conexão com o banco de dados
cur.close()
conn.close()
