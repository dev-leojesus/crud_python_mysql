import mysql.connector

def conectando_db(host, user, password):
    conexao_db = mysql.connector.connect(
        host = host,
        user = user,
        password = password
    )
    return conexao_db



