from flask import render_template, request, Blueprint, flash, redirect, url_for
from flask_login import current_user, login_required
from tseg.models import Equipment
from tseg.equipments.forms import EquipmentForm
from tseg import db


equipments = Blueprint('equipments', __name__)


@equipments.route("/all_equipments")
def all_equipments(client_id=None):
	page = request.args.get('page', 1, type=int) # num pagina de mensajes
	all_equips = Equipment.query.order_by(Equipment.date_created.desc()).paginate(page=page, per_page=5)
	return render_template('all_equipments.html', 
							all_equipments=all_equips, 
							title='Equipos')


@equipments.route("/equipment/<int:equipment_id>")
def equipment(equipment_id):
	equipment = Equipment.query.get_or_404(equipment_id)
	return render_template("equipment.html", title=equipment.title,
											equipment=equipment,
											legend="Ver Equipo")

@equipments.route("/add_equipment/<string:client_name>", methods=['GET','POST'] )
@login_required
def add_equipment(client_name):
	form = EquipmentForm()
	if form.validate_on_submit():
		equipment = Equipment(title=form.title.data, 
							content=form.content.data, 
							author_eq=current_user, 
							client_name=form.owner.data)
		db.session.add(equipment)
		db.session.commit()
		flash('Equipo agregado!', 'success')
		return redirect(url_for('equipments.all_equipments'))
	elif request.method == 'GET':
			form.owner.data = client_name
	return render_template('create_equipment.html', title='Agregar equipo', 
												form=form,
												legend="Agregar equipo")


@equipments.route("/equipment/<int:equipment_id>/update", methods=['GET', 'POST'])
@login_required
def update_equipment(equipment_id):
	equipment = Equipment.query.get_or_404(equipment_id)
	form = EquipmentForm()
	if form.validate_on_submit():
		equipment.title = form.title.data
		equipment.content = form.content.data
		equipment.client_id = form.owner.data
		db.session.commit()
		flash("El equipmente ha sido editado con éxito", 'success')
		return redirect(url_for('equipments.equipment', equipment_id=equipment.id))
	elif request.method == 'GET':
		form.title.data = equipment.title
		form.content.data = equipment.content
		form.owner.data = equipment.owner
	return render_template('create_equipment.html',title='Editar equipo', 
												form=form,
												legend="Editar equipo")

@equipments.route("/equipment/<int:equipment_id>/delete", methods=['POST'])
@login_required
def delete_equipment(equipment_id):
	equipment = Equipment.query.get_or_404(equipment_id)
	db.session.delete(equipment)
	db.session.commit()
	flash("El equipo ha sido eliminado!", 'success')
	return redirect(url_for('equipments.all_equipments'))
