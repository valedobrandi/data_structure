from flask import Flask
from flask_bootstrap import Bootstrap5
from waitress import serve
from os import environ
from flask_wtf import CSRFProtect
import secrets
from controllers.home_controller import home_controller

app = Flask(__name__)
bootstrap = Bootstrap5
secret = secrets.token_urlsafe(16)
app.secret_key = secret
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

app.register_blueprint(home_controller, url_prefix="/")
app.template_folder = "views/templates"


def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
