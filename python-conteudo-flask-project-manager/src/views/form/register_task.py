from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired


class RegisterTask(FlaskForm):
    task = StringField("task", validators=[DataRequired()])
    status = SelectField(
        "Status",
        choices=[("To Do", "To Do"), ("In Progress", "In Progress"), ("Done", "Done")],
        validators=[DataRequired()],
    )
    completionPercentage = StringField(
        "completionPercentage", validators=[DataRequired()]
    )
    descriptionTask = StringField("descriptionTask", validators=[DataRequired()])
    deadline = StringField("Deadline", validators=[DataRequired()])
    responsible = StringField("responsible", validators=[DataRequired()])
    submit = SubmitField("submit")
