import re
import string
import bcrypt

def validar_nome(nome:str):
    nome = nome.strip()
    tamanhoMinimo = 4
    tamanhoMaximo = 100
    
    
    if len(nome) >= tamanhoMinimo and len(nome) <= tamanhoMaximo:
        return nome.title()
    else:
        print(f"Nome inválido! O nome deve conter entre {tamanhoMinimo} e {tamanhoMaximo} caracteres.")
        return None
    
def validar_email(email:str):
    email = email.strip()
    padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(padrao, email):
        return email
    else:
        print("Email inválido!")
        return None

def validar_senha(senha:str):
    umaLetraMaiuscula = any(c.isupper() for c in senha)
    umNumero = any(c.isdigit() for c in senha)
    umCaracterEspecial = any(c in string.punctuation for c in senha)
    tamanhoMinimo = 8
    tamanhoMaximo = 300

    if umaLetraMaiuscula and umNumero and umCaracterEspecial and len(senha) >= tamanhoMinimo and len(senha) <= tamanhoMaximo:
        return senha
    else:
        print("Senha inválida! A senha deve conter pelo menos uma letra maiúscula, um número, um caractere especial e ter no mínimo 8 caracteres.")
        return None
    
def criptografar_senha(senha:str):
    senhaValidada = validar_senha(senha)

    if senhaValidada is None:
        return None
    
    senha_bytes = senha.encode('utf-8')
    senha_hash = bcrypt.hashpw(senha_bytes, bcrypt.gensalt())
    return senha_hash.decode('utf-8')