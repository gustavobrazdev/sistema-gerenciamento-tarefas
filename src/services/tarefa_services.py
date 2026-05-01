from models.tarefa import Tarefa

from validators.tarefa_validator import (
    validar_titulo,
    validar_descricao,
    validar_prioridade,
    validar_status,
    validar_prazo
)

from database.tarefa_repository import (
    salvar_tarefa,
    listar_tarefas,
    excluir_tarefa
)


def cadastrar_tarefa(titulo, descricao, prioridade, status, prazo, id_usuario):
    titulo_validado = validar_titulo(titulo)
    descricao_validada = validar_descricao(descricao)
    prioridade_validada = validar_prioridade(prioridade)
    status_validado = validar_status(status)
    prazo_validado = validar_prazo(prazo)

    if titulo_validado is None:
        return "Título inválido."

    if descricao_validada is None:
        return "Descrição inválida."

    if prioridade_validada is None:
        return "Prioridade inválida."

    if status_validado is None:
        return "Status inválido."

    if prazo and prazo_validado is None:
        return "Prazo inválido."

    tarefa = Tarefa(
        titulo_validado,
        descricao_validada,
        prioridade_validada,
        status_validado,
        prazo_validado,
        id_usuario
    )

    salvar_tarefa(tarefa)

    return "Tarefa cadastrada com sucesso!"


def buscar_tarefas_usuario(id_usuario):
    return listar_tarefas(id_usuario)


def remover_tarefa(id_tarefa, id_usuario):
    excluir_tarefa(id_tarefa, id_usuario)
    return "Tarefa excluída com sucesso!"