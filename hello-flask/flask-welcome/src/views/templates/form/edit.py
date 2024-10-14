from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class Edit(FlaskForm):
    title = StringField("Edit Title")
    author = StringField("Edit author")
    year = StringField("Edit year")
    submit = SubmitField("submit")
