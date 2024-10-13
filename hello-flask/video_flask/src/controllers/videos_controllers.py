from flask import Blueprint, request, render_template
from models.video import VideoModel


videos_controller = Blueprint("/videos", __name__)


def _get_all_videos():
    videos = VideoModel.find()
    return [details.to_dict() for details in videos]


def _get_by_title(titulo):
    videos = VideoModel._buscar_filmes_por_titulo(titulo)
    print(videos)
    return [video.to_dict() for video in videos]


@videos_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        videos = _get_by_title(titulo)
    else:
        videos = _get_all_videos()
    return render_template("index.html", videos=videos)
