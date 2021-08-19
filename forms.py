from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
	username = StringField('Nombre de usuario',
						validators=[DataRequired(), Length(min=4, max=15)], render_kw={'autofocus': True})
	password = PasswordField('Contraseña', 
						validators=[DataRequired()])
	remember = BooleanField('Recordarme')
	submit = SubmitField('Iniciar Sesión')


class RegistrationForm(LoginForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	confirm_password = PasswordField('Confirmar Contraseña', 
						validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Registrarse')