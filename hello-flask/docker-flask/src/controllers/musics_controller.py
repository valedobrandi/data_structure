from flask import Blueprint, request, jsonify
from models.music_model import MusicModel
from enum import Enum

musics_controller = Blueprint("musics", __name__)


class Http_map(Enum):
    SUCCESSFULL = 200
    CREATED = 201


def _get_all_musics():
    musics = MusicModel.find()

    return [music.stringfy() for music in musics]


@musics_controller.route("/", methods=["GET"])
def music_index():
    music_list = _get_all_musics()
    return jsonify(music_list), Http_map.SUCCESSFULL.value


@musics_controller.route("/", methods=["POST"])
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()

    return jsonify(new_music.stringfy()), 201
