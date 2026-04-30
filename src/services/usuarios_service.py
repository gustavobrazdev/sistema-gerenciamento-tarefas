from models.usuarios import Usuario
from validators.usuario_validator import validar_nome, validar_email, criptografar_senha, verificar_senha
from database.usuario_repository import salvar_usuario, buscar_usuario_email


def cadastrar_usuario(nome, email, senha):
    nome_validado = validar_nome(nome)
    email_validado = validar_email(email)
    senha_hash = criptografar_senha(senha)

    if nome_validado is None:
        return "Nome inválido."

    if email_validado is None:
        return "Email inválido."

    if senha_hash is None:
        return "Senha inválida."

    usuario = Usuario(nome_validado, email_validado, senha_hash)

    salvar_usuario(usuario)

    return "Usuário cadastrado com sucesso!"

def logar_usuario(email, senha):
    email_validado = validar_email(email)

    if email_validado is None:
        return "Email inválido."

    usuario = buscar_usuario_email(email_validado)

    if usuario is None:
        return "Usuário não encontrado."

    senha_correta = verificar_senha(senha, usuario["hash_senha_usuario"])

    if senha_correta:
        return "Login realizado com sucesso!"
    else:
        return "Senha incorreta."