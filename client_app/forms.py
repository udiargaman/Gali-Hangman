from flask_wtf import FlaskForm
from wtforms import validators, StringField, TextAreaField, SelectField, FileField
from flask_wtf.file import FileAllowed
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    user_id = StringField("", validators=[
            validators.InputRequired(),
            validators.Length(min=4, max=20)
        ])
