import json
import random
from pymongo import mongoClient
from datime import datime, timedelta

#conexao local padrão
cliente = MongoClient

#conexao banco
db = cliente.dbsenai

#colecao post
conexao = db.posts

#definindo as postagens
postagens =["Produto bom", "Produto Ruim! ", "Ótima Qualidade!!", "Qualidade inferior da nacional"]

nome = input("Digite seu nome: \n")
postagens = random.choice(postagens)
data = input("Digite Data: \n")

#Incluindo umdocumento
conexao.insert_one({"nome": nome, "postagem": postagem, "data": data})

#imprimindo todos os documentos na colecao
for doc in conexao.find():
    print(doc)
cliente.close()