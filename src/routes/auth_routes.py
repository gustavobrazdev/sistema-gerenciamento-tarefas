from services.usuarios_service import cadastrar_usuario, logar_usuario
from flask import Blueprint, render_template, request, redirect, url_for

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        resultado = cadastrar_usuario(nome, email, senha)
        return resultado

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        resultado = logar_usuario(email, senha)

        if resultado == "Login realizado com sucesso!":
            return redirect(url_for("tarefa.tarefas"))

        return resultado

    return render_template("login.html")
    