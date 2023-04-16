import mysql.connector
from mysql.connector import errorcode

# Configuração do banco de dados
config = {
  'user': 'root',
  'password': '',
  'host': 'localhost',
  'database': 'newsletter',
  'raise_on_warnings': True
}

# Obter os dados do usuário
nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")

try:
    # Conectar ao banco de dados
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Inserir os dados na tabela de usuários
    add_usuario = ("INSERT INTO usuarios (nome, email) VALUES (%s, %s)")
    data_usuario = (nome, email)
    cursor.execute(add_usuario, data_usuario)
    conn.commit()

    # Fechar a conexão
    cursor.close()
    conn.close()

    # Exibir uma mensagem de sucesso
    print("Cadastro realizado com sucesso!")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Erro: nome de usuário ou senha incorretos.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Erro: banco de dados não existe.")
    else:
        print("Erro: " + str(err))
