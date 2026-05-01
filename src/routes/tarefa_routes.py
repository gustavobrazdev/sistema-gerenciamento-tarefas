from flask import Blueprint, render_template, request, redirect, url_for

from services.tarefa_services import (
    cadastrar_tarefa,
    buscar_tarefas_usuario,
    remover_tarefa,
    buscar_tarefa_edicao,
    editar_tarefa
)


tarefa_bp = Blueprint("tarefa", __name__)


@tarefa_bp.route("/tarefas", methods=["GET", "POST"])
def tarefas():
    id_usuario = 1

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        prioridade = request.form["prioridade"]
        status = request.form["status"]
        prazo = request.form["prazo"]

        cadastrar_tarefa(
            titulo,
            descricao,
            prioridade,
            status,
            prazo,
            id_usuario
        )

        return redirect(url_for("tarefa.tarefas"))

    tarefas_usuario = buscar_tarefas_usuario(id_usuario)

    return render_template(
        "tarefas.html",
        tarefas=tarefas_usuario,
        tarefa_edicao=None
    )


@tarefa_bp.route("/tarefas/editar/<int:id_tarefa>", methods=["GET", "POST"])
def editar(id_tarefa):
    id_usuario = 1

    tarefa = buscar_tarefa_edicao(id_tarefa, id_usuario)

    if tarefa is None:
        return "Tarefa não encontrada."

    if request.method == "POST":
        titulo = request.form["titulo"]
        descricao = request.form["descricao"]
        prioridade = request.form["prioridade"]
        status = request.form["status"]
        prazo = request.form["prazo"]

        editar_tarefa(
            id_tarefa,
            titulo,
            descricao,
            prioridade,
            status,
            prazo,
            id_usuario
        )

        return redirect(url_for("tarefa.tarefas"))

    tarefas_usuario = buscar_tarefas_usuario(id_usuario)

    return render_template(
        "tarefas.html",
        tarefas=tarefas_usuario,
        tarefa_edicao=tarefa
    )


@tarefa_bp.route("/tarefas/excluir/<int:id_tarefa>")
def excluir(id_tarefa):
    id_usuario = 1

    remover_tarefa(id_tarefa, id_usuario)

    return redirect(url_for("tarefa.tarefas"))