from flask import Blueprint, render_template, request
from services.usuarios_service import cadastrar_usuario

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