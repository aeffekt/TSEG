from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class EquipmentForm(FlaskForm):
	title = StringField('Nombre', validators=[DataRequired()])
	content = TextAreaField('Descripción')
	owner = StringField('Cliente', validators=[DataRequired()])
	submit = SubmitField('Agregar')