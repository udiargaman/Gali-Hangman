from flask_wtf import FlaskForm
from wtforms import validators, StringField, SelectField
from flask_wtf.file import FileAllowed
from wtforms.fields.html5 import EmailField


class GameForm(FlaskForm):
    selection = StringField("", validators=[
            validators.InputRequired(),
            validators.Length(min=4, max=20)
        ])
