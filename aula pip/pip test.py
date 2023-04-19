import psycopg2
try:

    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="escola2",
        user="postgres",
        password="bispo",
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cursos")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    conn.close()
except(Exception, psycopg2.Error) as error:
    print("Erro ao conectar ao PostgreSQL", error)
