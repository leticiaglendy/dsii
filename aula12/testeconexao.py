import pymysql

# Configurações do banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'etecSQL',
    'port': 3306
}

# Função para inserir dados
def inserir_aluno(nome, sobrenome, idade, sexo):
    try:
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            sql = """
            INSERT INTO aluno (nome, sobrenome, idade, sexo)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, sobrenome, idade, sexo))
            conexao.commit()
            print(f"Aluno {nome} inserido com sucesso! ID: {cursor.lastrowid}")
    except Exception as e:
        print(f"Erro ao inserir: {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()

# Função para listar alunos
def listar_alunos():
    try:
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            cursor.execute("SELECT * FROM aluno")
            alunos = cursor.fetchall()
            
            print("\nLista de Alunos:")
            print("-" * 40)
            print(f"{'ID':<5}{'Nome':<20}{'Sobrenome':<20}{'Idade':<10}{'Sexo':<10}")
            print("-" * 40)
            
            for aluno in alunos:
                print(f"{aluno[0]:<5}{aluno[1]:<20}{aluno[2]:<20}{aluno[3]:<10}{aluno[4]:<10}")
                
    except Exception as e:
        print(f"Erro ao listar: {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()

# Exemplo de uso
if __name__ == "__main__":
    # Inserindo dados
    inserir_aluno("Maria", "Silva", 20, "Feminino")
    inserir_aluno("Carlos", "Oliveira", 22, "Masculino")
    
    # Listando todos
    listar_alunos()