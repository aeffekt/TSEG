from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

''' usar servidor debug (no requiere reiniciar al actualizar)
CMD: DIR/set FLASK_DEBUG=1
CMD: flask run
Browser: "localhost:5000" '''
app = Flask(__name__)

# seguridad Flask (ver readme.txt)
app.config['SECRET_KEY'] = 'bdded09a501a95d36034cf9a37905451'

posts = [
	{	'author': 'alguien1',
		'title': 'Blog post 1',
		'content': 'first post',
		'date_posted': 'Dec 2021'},
	{	'author': 'alguien2',
		'title': 'Blog post 2',
		'content': 'Second post',
		'date_posted': 'Nov 2021'}]

@app.route("/")
@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		# bootstrap message
		flash(f'Inicio de sesión correcto: {form.username.data}', 'Bienvenido')
		return redirect(url_for("blog"))
	return render_template('login.html', title='login', form=form)	

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		# bootstrap message
		flash(f'Cuenta creada: {form.username.data}', 'Con éxito')
		return redirect(url_for("blog"))
	return render_template('register.html', title='Register', form=form)	

@app.route("/blog")
def blog():
	return render_template('blog.html', posts=posts, title='BLOG')


if __name__ == "__main__":
	app.run(debug=True)