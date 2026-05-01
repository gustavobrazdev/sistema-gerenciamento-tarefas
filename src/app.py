from flask import Flask, redirect, url_for

from routes.auth_routes import auth_bp
from routes.tarefa_routes import tarefa_bp

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(tarefa_bp)


@app.route("/")
def home():
    return redirect(url_for("auth.login"))


if __name__ == "__main__":
    app.run(debug=True)