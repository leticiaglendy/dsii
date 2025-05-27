import json
import random
from pymongo import MongoClient
from datetime import datetime, timedelta

# Conexão local padrão
cliente = MongoClient('mongodb://localhost:27017/')

# Banco dbetec
db = cliente.dbetec

# Coleção posts
conexao = db.posts

# Loop de inserção (seu código original)
while True:
    acao = input("O que você deseja fazer? \n(i)nserir,\n(d)eletar,\n(l)istar,\n(s)air: ").lower()

    if acao == 'i':
        nome = input("Digite seu Nome: ")
        sbnome = input("Digite seu Sobrenome: ")
        idade = input("Digite sua Idade: ") # Lembre-se que idade está sendo salva como string
        sexo = input("Digite Sexo: ")
        
        # Incluindo um documento
        conexao.insert_one({"nome": nome, "sobrenome": sbnome, "idade": idade, "sexo": sexo})
        print("Registro inserido com sucesso!")

    elif acao == 'd':
        print("\n--- Deletar Registro ---")
        nome_del = input("Digite o Nome do registro a deletar: ")
        sbnome_del = input("Digite o Sobrenome do registro a deletar: ")
        idade_del = input("Digite a Idade do registro a deletar: ")
        sexo_del = input("Digite o Sexo do registro a deletar: ")

        # Critério para encontrar o documento a ser deletado
        filtro_delecao = {
            "nome": nome_del,
            "sobrenome": sbnome_del,
            "idade": idade_del,  # Importante: idade foi salva como string
            "sexo": sexo_del
        }

        # Tenta deletar um documento que corresponda ao filtro
        # Se você espera que possa haver múltiplos documentos idênticos e quer deletar todos,
        # use conexao.delete_many(filtro_delecao)
        resultado_delecao = conexao.delete_one(filtro_delecao)

        if resultado_delecao.deleted_count > 0:
            print(f"Registro com nome '{nome_del}' e sobrenome '{sbnome_del}' deletado com sucesso.")
        else:
            print(f"Nenhum registro encontrado com os critérios fornecidos para '{nome_del} {sbnome_del}'.")

    elif acao == 'l':
        print("\n--- Listando todos os documentos ---")
        documentos = list(conexao.find()) # Pega todos para verificar se há algo antes de iterar
        if not documentos:
            print("Nenhum documento na coleção.")
        else:
            for doc in documentos:
                print(doc)
        print("----------------------------------")
        
    elif acao == 's':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")

    continuar_geral = input("\nDeseja realizar outra operação? (s/n) ")
    if continuar_geral.lower() == "n":
        break

# Imprimindo todos os documentos na coleção uma última vez antes de sair (opcional)
print("\n--- Estado final da coleção ---")
for doc in conexao.find():
    print(doc)
print("-----------------------------")

cliente.close()
print("Conexão com o MongoDB fechada.")
