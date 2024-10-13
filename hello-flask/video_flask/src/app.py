from os import environ
from flask import Flask
from waitress import serve
from controllers.videos_controllers import videos_controller

app = Flask(__name__)
app.register_blueprint(videos_controller, url_prefix="/")


def start_server(host: str = "0.0.0.0", port: int = 8100):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
