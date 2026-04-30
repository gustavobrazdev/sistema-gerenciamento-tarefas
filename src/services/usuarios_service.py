from models.usuarios import Usuario
from validators.usuario_validator import validar_nome, validar_email, criptografar_senha
from database.usuario_repository import salvar_usuario


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