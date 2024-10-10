from flask import Blueprint, jsonify, render_template, redirect, url_for
from models.student_model import StudentModel
from form.register import Register
from form.edit import Edit

students_controller = Blueprint("students", __name__)


@students_controller.route("/", methods=["GET"])
def student_index():
    student_db = StudentModel
    list = student_db.find()
    return render_template(
        "students.html", 
        app_name="Student List",
        students_list=list
        )


@students_controller.route("/register", methods=["GET", "POST"])
def student_register():
    form = Register()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        register = form.registration.data
        message = "SUCCESSFULL"
        student = StudentModel({"name": name, "registration": register})
        student.save()
    if message == "SUCCESSFULL":
        return redirect(url_for("students.student_index"))
    return render_template("register.html", form=form, message=message)


@students_controller.route("/edit/<student_id>", methods=["GET", "POST"])
def student_edit(student_id: str):
    student = StudentModel
    get_student = student.find_one(student_id)
    form = Edit()

    message = ""
    id = get_student["_id"]
    name = get_student["name"]

    if form.validate_on_submit():
        name = form.name.data
        update_name = StudentModel({"name": name})
        update_name.update(id)
        message = "SUCCESSFULL"

    if message == "SUCCESSFULL":
        return redirect(url_for("students.student_index"))

    return render_template("edit_student.html", form=form, name=name)


@students_controller.route("/delete/<student_id>", methods=["GET", "DELETE"])
def student_delete(student_id: str):
    message = ""
    student = StudentModel(student_id)
    student.delete()
    new_list = student.find()
    message = "SUCCESSFULL"
    if message == "SUCCESSFULL":
        return redirect(url_for("students.student_index"))
    return render_template(
        "students.html", app_name="Student List", students_list=new_list
    )
