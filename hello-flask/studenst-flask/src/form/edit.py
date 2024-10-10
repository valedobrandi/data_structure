from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, length


class Edit(FlaskForm):
    name = StringField("Edit Name", validators=[DataRequired(), length(5, 20)])
    submit = SubmitField("submit")