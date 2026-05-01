from flask import Flask, render_template

from routes.auth_routes import auth_bp
from routes.tarefa_routes import tarefa_bp

app = Flask(__name__)
app.secret_key = "checklist-chave-secreta-dev"

app.register_blueprint(auth_bp)
app.register_blueprint(tarefa_bp)


@app.route("/")
def home():
    return render_template("landing.html")


if __name__ == "__main__":
    app.run(debug=True)