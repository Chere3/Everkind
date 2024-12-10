from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, EmailField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class LoginForm(FlaskForm):
    username = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=35), Email()]
    )
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    repeat_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    terms = BooleanField(
        "I agree to the Terms and Conditions", validators=[DataRequired()]
    )
    submit = SubmitField("Register")
