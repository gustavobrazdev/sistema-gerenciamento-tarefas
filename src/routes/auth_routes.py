from services.usuarios_service import (
    cadastrar_usuario,
    logar_usuario,
    buscar_perfil,
    atualizar_perfil,
    alterar_senha,
)
from flask import Blueprint, render_template, request, redirect, url_for, session

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]

        resultado = cadastrar_usuario(nome, email, senha)

        if resultado == "Usuário cadastrado com sucesso!":
            return redirect(url_for("auth.login", cadastro="ok"))

        return render_template(
            "cadastro.html",
            erro=resultado,
            nome=nome,
            email=email,
        )

    return render_template("cadastro.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]

        mensagem, usuario = logar_usuario(email, senha)

        if usuario is not None:
            session["id_usuario"] = usuario["id_usuario"]
            session["nome_usuario"] = usuario["nome_usuario"]
            session["email_usuario"] = usuario["email_usuario"]
            return redirect(url_for("tarefa.tarefas"))

        return render_template("login.html", erro=mensagem, email=email)

    cadastro_ok = request.args.get("cadastro") == "ok"
    return render_template("login.html", cadastro_ok=cadastro_ok)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))


@auth_bp.route("/perfil", methods=["GET", "POST"])
def perfil():
    id_usuario = session.get("id_usuario")
    if id_usuario is None:
        return redirect(url_for("auth.login"))

    sucesso = None
    erro = None

    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]

        mensagem, dados = atualizar_perfil(id_usuario, nome, email)

        if dados is not None:
            session["nome_usuario"] = dados["nome"]
            session["email_usuario"] = dados["email"]
            sucesso = mensagem
        else:
            erro = mensagem

    usuario = buscar_perfil(id_usuario)

    return render_template(
        "perfil.html",
        usuario=usuario,
        sucesso=sucesso,
        erro=erro,
    )


@auth_bp.route("/perfil/senha", methods=["POST"])
def alterar_senha_route():
    id_usuario = session.get("id_usuario")
    if id_usuario is None:
        return redirect(url_for("auth.login"))

    senha_atual = request.form["senha_atual"]
    senha_nova = request.form["senha_nova"]

    mensagem = alterar_senha(id_usuario, senha_atual, senha_nova)

    usuario = buscar_perfil(id_usuario)

    if mensagem == "Senha alterada com sucesso!":
        return render_template(
            "perfil.html",
            usuario=usuario,
            sucesso_senha=mensagem,
        )

    return render_template(
        "perfil.html",
        usuario=usuario,
        erro_senha=mensagem,
    )
