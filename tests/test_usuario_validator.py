from validators.usuario_validator import validar_nome, validar_email, validar_senha, criptografar_senha


def test_validar_nome_valido():
    assert validar_nome("gustavo") == "Gustavo"


def test_validar_nome_remove_espacos():
    assert validar_nome("  gustavo  ") == "Gustavo"


def test_validar_nome_invalido():
    assert validar_nome("gui") is None


def test_validar_email_valido():
    assert validar_email("teste@email.com") == "teste@email.com"


def test_validar_email_deixa_minusculo():
    assert validar_email("TESTE@EMAIL.COM") == "teste@email.com"


def test_validar_email_invalido():
    assert validar_email("emailerrado") is None


def test_validar_senha_valida():
    assert validar_senha("Senha@123") == "Senha@123"


def test_validar_senha_sem_maiuscula():
    assert validar_senha("senha@123") is None


def test_validar_senha_sem_numero():
    assert validar_senha("Senha@abc") is None


def test_validar_senha_sem_caractere_especial():
    assert validar_senha("Senha123") is None


def test_criptografar_senha_valida():
    senhaHash = criptografar_senha("Senha@123")

    assert senhaHash is not None
    assert senhaHash.startswith("$2b$") or senhaHash.startswith("$2a$")
    assert senhaHash != "Senha@123"