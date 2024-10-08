from flask import Flask, jsonify

app = Flask(__name__)  # instância


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/api")
def api_hello_world():
    return jsonify({"messsage": "Hello World!"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
