from flask import Blueprint, request, render_template
from models.message_model import MessageModel
from models.joke_model import JokeModel
from datetime import datetime
import random

chat_controller = Blueprint("chat_controler", __name__)


def _prepare_answer(name, menssage_content):
    if not menssage_content:
        return _answer_first(name)
    if "1" in menssage_content:
        return _answer_joke()
    return _answer_default()


@chat_controller.route("/", methods=["GET", "POST"])
def continue_chat():

    username = request.form.get("username") or "Visitante"
    message_content = request.form.get("message-content")

    _save_message(message_content, _from=username, to="Trybot")

    answer = _prepare_answer(username, message_content)

    _save_message(answer, _from="Trybot", to=username)
    session_messages = _get_message(username)
    print("session_messages", session_messages)
    return render_template(
        "chat.html", username=username, session_messages=session_messages
    )


def _answer_default():
    return random.choice(
        [
            "Interessante, me conte mais sobre isso.",
            "Compreendo como você se sente.",
            "Isso é algo com o qual muitas pessoas lidam.",
            "Como você está lidando com isso?",
            "Eu estou aqui para você, se precisar conversar.",
        ]
    )


def _get_message(name):
    messagens = MessageModel.find({"$or": [{"to": name}, {"from": name}]})
    print("messagens", messagens)
    return [message.to_dict() for message in messagens]


def _save_message(message_content, _from, to):
    if not message_content:
        return

    chat_message = MessageModel(
        {
            "content": message_content,
            "from": _from,
            "to": to,
            "time": datetime.now().strftime("%H:%H"),
        }
    )
    chat_message.save()


def _answer_first(name):
    return (
        f"Olá {name}, bem vindo a central de ajuda! Por hora posso "
        "te ajudar em algumas coisas 😄<br>1 - Contar uma piada"
    )


def _answer_joke():
    return (
        "Nok Nok"
        "Who is it?"
        "Mario"
        "Witch Mario?"
        "Aquele que te comeu atrás do armário"
    )
