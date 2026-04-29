import mysql.connector


def conexao_banco_dados():
    
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user = "root",
            password = "Root@123",
            database = "sistema_gerenciamento_tarefas"
        )
        if conexao.is_connected():
            print("Conexão bem-sucedida ao banco de dados!")
            return conexao
        
    except mysql.connector.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None