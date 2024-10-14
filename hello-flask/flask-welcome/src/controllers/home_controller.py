from flask import Blueprint, render_template, jsonify, redirect, url_for
from models.book import Book
from models.book_model import BooksModel
from views.templates.form.edit import Edit

home_controller = Blueprint("home_controller", __name__)


@home_controller.route("/", methods=["GET"])
def index():
    book_list = BooksModel.find()
    library = [book.to_dict() for book in book_list]
    message = "Bernardo"
    return render_template("index.html", message=message, library=library)


@home_controller.route("/save", methods=["POST"])
def save():
    book = Book({"title": "Superman", "author": "Alfred", "year": "2025"})
    BooksModel.save(book.get_book())
    return jsonify({"message": "book saved!"}), 200


@home_controller.route("/edit/<book_id>", methods=["GET", "POST"])
def edit(book_id: str):
    get_book = BooksModel.find_one({"id": int(book_id)})
    book = get_book.to_dict()
    edit_form = Edit()
    # Pre-fill the form with the book data
    if edit_form.validate_on_submit():
        title = edit_form.title.data
        author = edit_form.author.data
        year = edit_form.year.data
        title = title if title else book["title"]
        author = author if author else book["author"]
        year = year if year else book["year"]
        BooksModel.edit(
            {"id": book["id"], "title": title, "author": author, "year": year}
        )
        return redirect(url_for("home_controller.index"))
    return render_template("edit.html", book=book, form=edit_form)


@home_controller.route("/find", methods=["GET"])
def find():
    find_book = BooksModel.find()
    return jsonify([book.to_dict() for book in find_book]), 200


@home_controller.route("/delete/<book_id>", methods=["GET", "DELETE"])
def delete(book_id):
    BooksModel.delete({"id": int(book_id)})
    return index(), 200
