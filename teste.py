# Importando o módulo de conexão do Python com o MySQL
import mysql.connector
# Importando a função de conexão ao DB do arquivo conectar_db.py
from conectar_db import conectando_db

relacao_dbs = []
count = 0

#print("\n Para acessar o banco de dados informe os dados abaixo \n")
#host = input("Informe o host do DB: ")
#user = input("Informe o nome de usuário do DB: ")
#password = input("Informe a senha de acesso ao DB: ")

# Chamando a função de conexão ao DB e armazenando o retorno na variável conexão
conexao = conectando_db("localhost", "root", "leogm2015")

# Criando o objeto cursor
db_cursor = conexao.cursor()

# Realizando consulta ao banco 
db_cursor.execute("SHOW DATABASES")

# Lendo a relação de DB e armazenando o retorno em uma lista
for db in db_cursor:
    relacao_dbs.append(db[0])

# Exibindo a relação de DBs
for db in relacao_dbs:
    print(db)