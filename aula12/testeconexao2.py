import pymysql

# Configurações do banco
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'etecSQL',
    'port': 33061
}

def obter_dados_usuario():
    """Obtém dados do aluno via input do usuário"""
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    idade = int(input("Idade: "))  # Converte para inteiro
    sexo = input("Sexo (M/F/Outro): ").strip().capitalize()
    return nome, sobrenome, idade, sexo

def inserir_aluno(nome, sobrenome, idade, sexo):
    """Insere um novo aluno no banco de dados"""
    try:
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            sql = """
            INSERT INTO aluno (nome, sobrenome, idade, sexo)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (nome, sobrenome, idade, sexo))
            conexao.commit()
            print(f"\n Aluno {nome} inserido com ID: {cursor.lastrowid}")
            return cursor.lastrowid  # Retorna o ID gerado
    except ValueError:
        print("Erro: Idade deve ser um número inteiro!")
    except Exception as e:
        print(f"Erro ao inserir: {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()

def listar_alunos():
    """Lista todos os alunos cadastrados"""
    try:
        conexao = pymysql.connect(**config)
        with conexao.cursor() as cursor:
            cursor.execute("SELECT id, nome, sobrenome, idade, sexo FROM aluno")
            alunos = cursor.fetchall()
            
            if not alunos:
                print("\nNenhum aluno cadastrado.")
                return
                
            print("\n Lista de Alunos:")
            print("-" * 60)
            print(f"{'ID':<5}{'Nome':<20}{'Sobrenome':<20}{'Idade':<10}{'Sexo':<10}")
            print("-" * 60)
            
            for aluno in alunos:
                print(f"{aluno[0]:<5}{aluno[1]:<20}{aluno[2]:<20}{aluno[3]:<10}{aluno[4]:<10}")
    except Exception as e:
        print(f"Erro ao listar: {e}")
    finally:
        if 'conexao' in locals():
            conexao.close()

def menu_principal():
    """Exibe o menu interativo"""
    while True:
        print("\n" + "="*50)
        print(" MENU PRINCIPAL ".center(50, '='))
        print("="*50)
        print("1. Cadastrar novo aluno")
        print("2. Listar todos os alunos")
        print("3. Sair")
        
        opcao = input("\nEscolha uma opção (1-3): ")
        
        if opcao == '1':
            try:
                dados = obter_dados_usuario()
                inserir_aluno(*dados)
            except ValueError:
                print("Erro: Idade deve ser um número válido!")
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Execução do programa
if __name__ == "__main__":
    menu_principal()