import pymysql

try:
    conexao = pymysql.connect(
        host="localhost",
        database="etecBD",
        user="root",
        password="",
        port=3306
    )
    cursor = conexao.cursor()


    while True:
        nome = input("Digite o Nome: ")
        sobrenome = input("Digite o Sobrenome: ")
        idade = int(input("Digite a Idade: "))
        sexo = input("Digite o Sexo (Masculino/Feminino): ").upper()

        try:
            cursor.execute("INSERT INTO Cadastro (Nome, Sobrenome, Idade, Sexo) VALUES (%s, %s, %s, %s)", (nome, sobrenome, idade, sexo))
            conexao.commit()
            print("Dados inseridos com sucesso!")

        except pymysql.MySQLError as e:
            print(f"Erro ao inserir dados: {e}")
            conexao.rollback()

        continuar = input("Deseja continuar? (s/n) ")
        if continuar.lower() == "n":
            break


    cursor.execute("SELECT * FROM Cadastro")
    registros = cursor.fetchall()

    for row in registros:
        print("Nome = ", row[1])
        print("Sobrenome = ", row[2])
        print("Idade = ", row[3])
        print("Sexo  = ", row[4], "\n")

except pymysql.MySQLError as e:
    print(f"Erro de conexão/operação com o banco de dados: {e}")

finally:
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()