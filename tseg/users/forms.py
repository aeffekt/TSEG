from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from tseg.models import User


class LoginForm(FlaskForm):
	username = StringField('Nombre de usuario',
						validators=[DataRequired(), Length(min=2, max=30)], render_kw={'autofocus': True})
	password = PasswordField('Contraseña', 
						validators=[DataRequired(), Length(min=4, max=12)])
	remember = BooleanField('Recordarme')
	submit = SubmitField('Iniciar Sesión')

class RegistrationForm(LoginForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	confirm_password = PasswordField('Confirmar Contraseña', 
						validators=[DataRequired(), EqualTo('password'), Length(min=4, max=12)])
	submit = SubmitField('Registrarse')

	# custom validators = validator_{field_name}
	def validate_username(self, username):
		name_already_exist = User.query.filter_by(username=username.data).first()
		if name_already_exist:
			raise ValidationError('Ese nombre ya está en uso. Por favor, elija uno diferente')

	def validate_email(self, email):
		mail_already_exist = User.query.filter_by(email=email.data).first()
		if mail_already_exist:
			raise ValidationError('Ese Email ya está en uso. Por favor, elija uno diferente')

class UpdateAccountForm(FlaskForm):
	username = StringField('Nombre de usuario',
						validators=[DataRequired(), Length(min=2, max=30)], render_kw={'autofocus': True})
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	picture = FileField('Imagen de usuario', validators=[FileAllowed(['jpg', 'png', 'bmp', 'gif'])])
	submit = SubmitField('Actualizar')

	# custom validators = validator_{field_name}
	def validate_username(self, username):
		if username.data != current_user.username:
			name_already_exist = User.query.filter_by(username=username.data).first()
			if name_already_exist:
				raise ValidationError('Ese nombre ya está en uso. Por favor, elija uno diferente')

	def validate_email(self, email):
		if email.data != current_user.email:
			mail_already_exist = User.query.filter_by(email=email.data).first()
			if mail_already_exist:
				raise ValidationError('Ese Email ya está en uso. Por favor, elija uno diferente')


class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Resetear contraseña.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Ese email no se encuentra en nuestros registros. Debe crear una cuenta primero.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Aplicar nueva contraseña.')