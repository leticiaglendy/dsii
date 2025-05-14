import pymysql

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'etecSQL',
    'port': 3306
}

try:
    conexao = pymysql.connect(**config)
    print("Conexão bem-sucedida!")
    with conexao.cursor() as cursor:
        cursor.execute("SELECT * FROM aluno LIMIT 5")
        print("\nPrimeiras 5 linhas:")
        for linha in cursor.fetchall():
            print(linha)

except Exception as erro:
    print(f"Erro: {erro} ")

finally:
    if 'conexao' in locals():
        conexao.close()
        print("Conexão encerrada.")