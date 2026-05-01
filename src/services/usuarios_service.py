from models.usuarios import Usuario
from validators.usuario_validator import validar_nome, validar_email, criptografar_senha, verificar_senha
from database.usuario_repository import (
    salvar_usuario,
    buscar_usuario_email,
    buscar_usuario_id,
    atualizar_dados_usuario,
    atualizar_senha_usuario,
)


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
        return "Email inválido.", None

    usuario = buscar_usuario_email(email_validado)

    if usuario is None:
        return "Usuário não encontrado.", None

    senha_correta = verificar_senha(senha, usuario["hash_senha_usuario"])

    if senha_correta:
        return "Login realizado com sucesso!", usuario
    else:
        return "Senha incorreta.", None


def buscar_perfil(id_usuario):
    return buscar_usuario_id(id_usuario)


def atualizar_perfil(id_usuario, nome, email):
    nome_validado = validar_nome(nome)
    email_validado = validar_email(email)

    if nome_validado is None:
        return "Nome inválido.", None

    if email_validado is None:
        return "Email inválido.", None

    usuario_existente = buscar_usuario_email(email_validado)
    if usuario_existente and usuario_existente["id_usuario"] != id_usuario:
        return "Este e-mail já está em uso por outra conta.", None

    atualizar_dados_usuario(id_usuario, nome_validado, email_validado)

    return "Dados atualizados com sucesso!", {"nome": nome_validado, "email": email_validado}


def alterar_senha(id_usuario, senha_atual, senha_nova):
    usuario = buscar_usuario_id(id_usuario)

    if usuario is None:
        return "Usuário não encontrado."

    if not verificar_senha(senha_atual, usuario["hash_senha_usuario"]):
        return "Senha atual incorreta."

    senha_hash = criptografar_senha(senha_nova)

    if senha_hash is None:
        return "A nova senha não atende aos requisitos."

    atualizar_senha_usuario(id_usuario, senha_hash)

    return "Senha alterada com sucesso!"