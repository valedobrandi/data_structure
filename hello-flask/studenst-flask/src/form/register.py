from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class Register(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired(), length(5, 20)])
    registration = StringField("Registration Code")
    submit = SubmitField("submit")
