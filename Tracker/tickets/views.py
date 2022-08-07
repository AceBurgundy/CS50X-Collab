from flask import render_template, request, url_for, flash, redirect, Blueprint
from Tracker.models import Ticket, Project
from Tracker import db, database
from Tracker.tickets.forms import TicketForm
from sqlalchemy import insert, update, delete
from flask_login import login_required, current_user

tickets = Blueprint('tickets', __name__, template_folder='templates/tickets', static_folder='static/tickets')

#Show tickets

@tickets.route("/show-tickets/<int:current_project_id>")
@login_required
def show_tickets(current_project_id):

    image_file = url_for('static', filename='profile_pictures/' + current_user.profile_picture)
    
    if request.method == "GET":
        tickets = database.execute("SELECT * FROM Ticket WHERE project_id = ?", current_project_id)
        # tickets = Ticket.query.filter_by(project_id=current_project_id)  
        return render_template("tickets.html", image_file=image_file, project_id=current_project_id, tickets=tickets, pageTitle="TICKETS")

@tickets.route("/add-ticket/<int:current_project_id>", methods=["POST","GET"])
@login_required
def add_ticket(current_project_id):

    modal_title = "CREATE NEW TICKET"
    form = TicketForm()
    if request.method == "POST":

        ticket_status = request.form.get('ticket-status')
        print(ticket_status)
        if form.validate_on_submit():
            
            try:
                db.session.add(Ticket(
                    name = form.name.data,
                    content = form.description.data, 
                    deadline = form.deadline.data,
                    status = ticket_status,
                    assigned_user = 'author',
                    created_by=current_user.username,
                    priority = form.priority.data,
                    project_id=current_project_id))

                db.session.commit()
                flash('Ticket added')
                return redirect(url_for('tickets.show_tickets', current_project_id=current_project_id))
            except:
                form.form_errors.append('Failed to add ticket')
                return render_template('ticket-modal.html', ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form, error=form.errors)
        else:
            return render_template('ticket-modal.html', ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form, error=form.form_errors)
    else:
        
        ticket_status = request.form.get('ticket-status')
        print(request.form.get('ticket-status'))

        return render_template('ticket-modal.html', ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form)
    
@tickets.route("/update-ticket/<int:current_ticket_id>", methods=["POST","GET"])
@login_required
def update_ticket(current_ticket_id):
    """ Update ticket """

    modal_title = "UPDATE THIS TICKET"
    form = TicketForm()
    if request.method == "POST":
        if form.validate_on_submit():
            
            try:
                db.session.execute(
                    update(Ticket).
                    where(Ticket.id == current_ticket_id).
                    values(title = form.title.data, 
                           description = form.description.data, 
                           deadline = form.deadline.data))
                
                db.session.commit()
                flash('Ticket updated')
                current_project_id = Project.query.filter_by(Project.tickets == current_ticket_id)
                return redirect(url_for('tickets.show_tickets', current_project_id=current_project_id))
            except:
                form.form_errors.append('Ticket update failed')
                return render_template('ticket-modal.html', modal_title=modal_title, form=form, error=form.errors)
        else:
            return render_template('ticket-modal.html', modal_title=modal_title, form=form, error=form.errors)
    else:
        ticket = Ticket.query.filter_by(id=current_ticket_id).first()
        form.name.data = ticket.name 
        form.description.data = ticket.content
        form.deadline.data = ticket.deadline
        status = ticket.status
        form.priority.data = ticket.priority

        return render_template('ticket-modal.html', status=status, current_ticket_id=current_ticket_id, modal_title=modal_title, form=form)

# Delete ticket

@tickets.route("/delete/<int:current_ticket_id>", methods=["POST"])
@login_required
def delete_ticket(current_ticket_id):
    """ Delete ticket """

    if request.method == "POST":
        try:      
            ticket = (delete(Ticket).where(Ticket.id == current_ticket_id))
            db.session.execute(ticket)
            db.session.commit()
            flash('Ticket deleted')
            current_project_id = Project.query.filter_by(Project.tickets == current_ticket_id)
            return redirect(url_for('tickets.show_tickets', current_project_id=current_project_id))
        except:
            flash('Ticket not found')
            current_project_id = Project.query.filter_by(Project.tickets == current_ticket_id)
            return redirect(url_for('tickets.show_tickets', current_project_id=current_project_id))