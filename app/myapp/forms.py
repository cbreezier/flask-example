from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email

class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
    username = TextField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])