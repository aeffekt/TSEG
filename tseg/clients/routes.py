from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user, login_required
from tseg.models import Client, Equipment
from tseg.clients.forms import ClientForm
from tseg import db

clients = Blueprint('clients', __name__)

@clients.route("/all_clients")
def all_clients():
	page = request.args.get('page', 1, type=int) # num pagina de mensajes
	all_clients = Client.query.order_by(Client.client_name.desc()).paginate(page=page, per_page=5)
	return render_template('all_clients.html', 
							all_clients=all_clients, 
							title='Clientes')


# ruteo de variables "client_id"
@clients.route("/client/<int:client_id>")
def client(client_id):
	client = Client.query.get_or_404(client_id)
	return render_template("client.html", title=client.client_name,
											client=client)


@clients.route("/add_client", methods=['GET','POST'] )
@login_required
def add_client():
	form = ClientForm()
	if form.validate_on_submit():
		client = Client(client_name=form.client_name.data, 
						business_name=form.business_name.data, 
						contact=form.contact.data,
						author_cl=current_user)
		db.session.add(client)
		db.session.commit()
		flash('Cliente agregado!', 'success')
		return redirect(url_for('clients.client'))
	return render_template('create_client.html', title='Nuevo cliente', 
												form=form,
												legend="Agregar cliente")

@clients.route("/client/<int:client_id>/update", methods=['GET', 'POST'])
@login_required
def update_client(client_id):
	client = Client.query.get_or_404(client_id)
	form = ClientForm()
	if form.validate_on_submit():
		client.client_name = form.client_name.data
		client.business_name = form.business_name.data
		client.contact = form.contact.data
		db.session.commit()
		flash("El cliente ha sido editado con éxito", 'success')
		return redirect(url_for('clients.client', client_id=client.id))
	elif request.method == 'GET':
		form.client_name.data = client.client_name
		form.business_name.data = client.business_name
		form.contact.data = client.contact
	return render_template('create_client.html',title='Editar cliente', 
												form=form,
												legend="Editar cliente")

@clients.route("/client/<int:client_id>/delete", methods=['POST'])
@login_required
def delete_client(client_id):
	client = Client.query.get_or_404(client_id)
	db.session.delete(client)
	db.session.commit()
	flash("El cliente ha sido eliminado!", 'success')
	return redirect(url_for('clients.all_clients'))


@clients.route("/client/<string:client_name>")
def client_equipments(client_name):
	page = request.args.get('page', 1, type=int) #num pagina de mensajes
	client = Client.query.filter_by(client_name=client_name).first_or_404()
	equipments = Equipment.query.filter_by(owner=client)\
					.order_by(Equipment.last_modified.desc())\
					.paginate(page=page, per_page=5)
	return render_template('client_equipments.html', equipments=equipments, client=client)
