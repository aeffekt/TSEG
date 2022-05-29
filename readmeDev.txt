User	id PK
	username
	email
	image_file
	password
	posts
Post	id PK
	content
	date_posted
	parent_name
	parent_id
	user_id
Equipos	id PK
	title
	date_created
	last_modified
	content
	client_id
	user_id
Clientes	id PK
	client_name
	business_name
	contact
Equip_data
	id PK
	manual_path
	content
	last_date_mod
	user_id


TSEG seguimiento de equipos

Este archivo contiene información del programa para desarrolladores.

Programa desarrollado a partir de:
video tutorial, Python Flask Tutorial: Full-Featured Web App, por Corey Schafer

CMD:
pip install flask
pip install flask_wtf
pip install flask-sqlalchemy
pip install flask-bcrypt
pip install flask-login
pip install flask-mail

if email error:::
pip install email_validator



PYTHON:
import secrets:
secrets.token_hex(16): #16  bytes --> resultado se como codigo de seguridad

DATABASE:
CMD:
python
>>> from tseg import db
>>> db.create_all()
>>> User.query.all()
[]

SECURITY:
CMD:
python
>>> from flask_bcrypt import Bcrypt
>>> bcrypt = Bcrypt()
>>> hashed_pw = bcrypt.generate_password_hash('admin')
>>> bcrypt.check_password_hash(hashed_pw, 'password') = False
>>> bcrypt.check_password_hash(hashed_pw, 'admin') = True

SHELL_VARIABLES (RESTART O.S. AFTER EDIT):
SECRET_KEY
SQLALCHEMY_DATABASE_URI
EMAIL_USER
EMAIL_PASS


usar servidor debug (no requiere reiniciar al actualizar)
CMD: DIR/set FLASK_DEBUG=1
CMD: flask run
Browser: "localhost:5000"

Windows 7 SERVER INSTALL:
https://www.youtube.com/watch?v=dC84NQqjYEc


Versión: 0.0.1

29/09/21 (Token que expira en segundos)
>> python
>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>> s = Serializer('secret', 30) #time 30secs
>> token = s.dumps({'user_id': 1}.decode('utf-8'))
>> token