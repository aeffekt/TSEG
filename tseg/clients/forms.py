from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ClientForm(FlaskForm):
	client_name = StringField('Nombre', validators=[DataRequired()], render_kw={'autofocus': True})
	business_name = StringField('Razón social')
	contact = StringField('Contacto', validators=[DataRequired()])
	submit = SubmitField('Agregar')