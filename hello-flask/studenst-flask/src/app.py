from flask import Flask
from os import environ
from waitress import serve
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
import secrets
from controllers.students_controller import students_controller


app = Flask(__name__)
secret = secrets.token_urlsafe(16)
app.secret_key = secret
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)


app.register_blueprint(students_controller, url_prefix="/students")


@app.route("/")
def hello_world():
    return "Hello World!"


def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
