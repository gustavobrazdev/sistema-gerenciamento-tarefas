from database.conexao import conexao_banco_dados


def salvar_usuario(usuario):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        INSERT INTO usuarios (nome_usuario, email_usuario, hash_senha_usuario)
        VALUES (%s, %s, %s)
    """

    valores = (
        usuario.nome,
        usuario.email,
        usuario.senha_hash
    )

    cursor.execute(sql, valores)
    conexao.commit()

    cursor.close()
    conexao.close()

def buscar_usuario_email(email):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT * FROM usuarios
        WHERE email_usuario = %s
    """

    cursor.execute(sql, (email,))
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario