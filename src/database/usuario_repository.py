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
        SELECT id_usuarios AS id_usuario,
               nome_usuario,
               email_usuario,
               hash_senha_usuario
        FROM usuarios
        WHERE email_usuario = %s
    """

    cursor.execute(sql, (email,))
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario


def buscar_usuario_id(id_usuario):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor(dictionary=True)

    sql = """
        SELECT id_usuarios AS id_usuario,
               nome_usuario,
               email_usuario,
               hash_senha_usuario
        FROM usuarios
        WHERE id_usuarios = %s
    """

    cursor.execute(sql, (id_usuario,))
    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    return usuario


def atualizar_dados_usuario(id_usuario, nome, email):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        UPDATE usuarios
        SET nome_usuario = %s, email_usuario = %s
        WHERE id_usuarios = %s
    """

    cursor.execute(sql, (nome, email, id_usuario))
    conexao.commit()

    cursor.close()
    conexao.close()


def atualizar_senha_usuario(id_usuario, senha_hash):
    conexao = conexao_banco_dados()
    cursor = conexao.cursor()

    sql = """
        UPDATE usuarios
        SET hash_senha_usuario = %s
        WHERE id_usuarios = %s
    """

    cursor.execute(sql, (senha_hash, id_usuario))
    conexao.commit()

    cursor.close()
    conexao.close()