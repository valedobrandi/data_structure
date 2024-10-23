from bson.errors import InvalidId
from flask import Blueprint, render_template, redirect, url_for, request
from models.projectModel import ProjectModel
from models.querys import _project_id, _task_id
from views.form.register_task import RegisterTask

project_controller = Blueprint("project", __name__)


def _get_project_or_task(id):
    project = ProjectModel.find(id)
    return [task.to_dict() for task in project]


@project_controller.route("/")
@project_controller.route("/projects")
def home():
    projects = ProjectModel.separate_projects()
    return render_template("home.html", projects=projects)


@project_controller.route("/projects/<id>")
def project(id):
    project = _get_project_or_task(_project_id(id))
    if not project:
        return render_template("404.html"), 404
    return render_template("project.html", project=project)


@project_controller.route("/task/<id>")
def task(id):
    try:
        task = _get_project_or_task(_task_id(id))

        if not task:
            return render_template("404.html"), 404
        return render_template("task.html", task=task[0])

    except InvalidId:
        return render_template("404.html"), 404


@project_controller.route("/task/<id_project>/form", methods=["GET", "POST"])
def register_task(id_project):
    get_project = _get_project_or_task(_project_id(id_project))
    project_title = get_project[0]["name"]
    id = get_project[0]["id_project"]

    if not project:
        return render_template("404.html"), 404

    form = RegisterTask()

    if request.method == "POST":
        new_project = ProjectModel(
            {
                "idProject": id,
                "name": project_title,
                "task": form.task.data,
                "status": form.status.data,
                "completionPercentage": form.completionPercentage.data,
                "descriptionTask": form.descriptionTask.data,
                "deadline": form.deadline.data,
                "responsible": form.responsible.data,
            }
        )
        if form.validate_on_submit():
            new_project.save()

            return redirect(f"http://172.21.0.3:8000/projects/{id_project}")

    return render_template("taskForm.html", form=form, name=project_title, id=id)
