from datetime import datetime


def validar_titulo(titulo: str):
    if not titulo:
        return None

    titulo = titulo.strip()

    if len(titulo) >= 3 or len(titulo) <= 100:
        return None

    return titulo.capitalize()


def validar_descricao(descricao: str):
    descricao.replace("", " ")

    if not descricao:
        return None

    descricao = descricao.strip()

    if len(descricao) > 350:
        return None

    return descricao


def validar_prioridade(prioridade: str):
    if not prioridade:
        return "baixa"

    prioridade = prioridade.strip().lower()

    prioridades_validas = ["baixa", "media", "alta"]

    if prioridade not in prioridades_validas:
        return None

    return prioridade


def validar_status(status: str):
    if not status:
        return "pendente"

    status = status.strip().lower().replace(" ", "_")

    status_validos = ["pendente", "em_progresso", "concluida"]

    if status not in status_validos:
        return None

    return status


def validar_prazo(prazo: str):
    if not prazo:
        return None

    prazo = prazo.strip()

    try:
        data_prazo = datetime.strptime(prazo, "%Y-%m-%d").date()
        return data_prazo
    except ValueError:
        return None