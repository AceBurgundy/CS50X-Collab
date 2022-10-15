from flask import jsonify, render_template, request, url_for, flash, redirect, Blueprint
from Tracker.models import TicketCommentLikes
from Tracker.models import Ticket, Project, TicketComment, TicketCommentReplies, User
from Tracker import db
from Tracker.tickets.forms import TicketForm
from Tracker.helpers import check_profanity
from sqlalchemy import insert, update, delete, select
from flask_login import login_required, current_user
from colorama import init

tickets = Blueprint('tickets', __name__,
                    template_folder='templates/tickets', static_folder='static/tickets')

# Show tickets


@tickets.get("/show-tickets/<int:current_project_id>")
@login_required
def show_tickets(current_project_id):

    image_file = url_for(
        'static', filename='profile_pictures/' + current_user.profile_picture)

    tickets = db.session.execute(select(Ticket).filter_by(
        project_id=current_project_id)).scalars().all()

    project_author = Project.query.get(current_project_id).author.username

    assigned_user = []

    for ticket in tickets:
        assigned_user.append({
            "ticket_id": ticket.id,
            "author_profile_picture": url_for(
                'static', filename='profile_pictures/' + User.query.get(ticket.assigned_user).profile_picture)
        })

    return render_template("tickets.html", assigned_user=assigned_user, project_author=project_author, image_file=image_file, project_id=current_project_id, tickets=tickets, pageTitle="TICKETS")


@ tickets.route("/add-ticket/<int:current_project_id>", methods=["POST", "GET"])
@ login_required
def add_ticket(current_project_id):

    modal_title = "CREATE NEW TICKET"
    form = TicketForm()
    project = db.session.get(Project, current_project_id)

    if request.method == "POST":

        if form.validate_on_submit():
            ticket_status = request.form.get('ticket-status')

            try:
                ticket = (
                    insert(Ticket).values(
                        name=form.name.data,
                        content=form.description.data,
                        deadline=form.deadline.data,
                        status=ticket_status,
                        assigned_user=form.assign.data,
                        created_by=current_user.username,
                        priority=form.priority.data,
                        project_id=current_project_id)
                )
                db.session.execute(ticket)
                db.session.commit()
                flash('Ticket added')
                return redirect(url_for('tickets.show_tickets', current_project_id=current_project_id))
            except:
                form.form_errors.append('Failed to add ticket')
                return render_template('ticket-modal.html', project=project, ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form, error=form.errors)
        else:
            return render_template('ticket-modal.html', ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form, error=form.form_errors)
    else:

        ticket_status = request.form.get('ticket-status')

        return render_template('ticket-modal.html', project=project, ticket_status=ticket_status, project_id=current_project_id, modal_title=modal_title, form=form)

# open ticket


@ tickets.route("/details/<int:current_ticket_id>", methods=["GET", "POST"])
@ login_required
def open_ticket(current_ticket_id):

    image_file = url_for(
        'static', filename='profile_pictures/' + current_user.profile_picture)

    ticket = db.session.get(Ticket, current_ticket_id)

    # used to query comments
    ticket_comments = TicketComment.query.filter_by(
        ticket_id=current_ticket_id)

    if request.method == "GET":
        return render_template('ticket-details.html', pageTitle="TICKET #", image_file=image_file, ticket=ticket, ticket_comments=ticket_comments)


# Delete ticket

@ tickets.post("/delete-ticket/<int:current_ticket_id>")
@ login_required
def delete_ticket(current_ticket_id):
    """ Delete ticket """

    if request.method == "POST":
        try:
            print("called")
            ticket = (delete(Ticket).where(Ticket.id == current_ticket_id))
            ticket_comments = (delete(TicketComment).where(
                TicketComment.ticket_id == current_ticket_id))
            db.session.execute(ticket)
            db.session.execute(ticket_comments)

            db.session.commit()
            flash('Ticket deleted')
            return redirect(url_for('tickets.show_tickets', current_project_id=request.form["project_id"]))
        except:
            flash('Ticket not found')
            return redirect(url_for('tickets.show_tickets', current_project_id=request.form["project_id"]))

# update ticket status


@ tickets.post('/status')
@ login_required
def update_status():
    """ Update ticket status """

    if request.method == "POST":
        try:
            new_status = request.form['new_status']
            ticket_id = request.form['ticket_id']

            if new_status is None:
                return jsonify(failed='Cannot find new ticket status')

            if ticket_id is None:
                return jsonify(failed='Cannot find ticket id')

            ticket = db.session.get(Ticket, ticket_id)
            ticket.status = new_status
            db.session.commit()
            return jsonify(success='Ticket status updated')
        except:
            return jsonify(failed='Failed to update ticket')


@ tickets.post("/add-comment")
def add_comment():

    message = request.form['comment']
    ticket_id = request.form['ticket_id']

    if check_profanity(message) == True:
        init(autoreset=True)
        print(f"Checking profanity for message", "\033[1;32mpassed")

    if not message:
        return jsonify(failed='Comment cannot be empty'), 200

    if not ticket_id:
        return jsonify(failed='Missing ticket number'), 200

    new_comment = TicketComment(
        sender=current_user,
        comment=message,
        ticket_id=ticket_id
    )
    db.session.add(new_comment)
    db.session.commit()
    db.session.flush()
    db.session.refresh(new_comment)
    return render_template('comment.html', comment=new_comment)


@ tickets.post('/udpate-comment')
@ login_required
def update_comment():
    """ Update ticket status """

    if request.method == "POST":
        try:
            new_comment = request.form['new_comment']
            comment_id = request.form['comment_id']

            if new_comment is None:
                return jsonify(failed='Cannot find new ticket status')

            if comment_id is None:
                return jsonify(failed='Cannot find ticket id')

            comment = db.session.get(TicketComment, comment_id)
            comment.comment = new_comment
            db.session.commit()
            return jsonify(success='Comment updated')
        except:
            return jsonify(failed='Failed to update comment')


@ tickets.post("/like-comment")
def like_comment():
    if request.method == 'POST':
        try:
            comment_id = request.form['comment_id']
            comment = TicketComment.query.filter_by(
                id=comment_id).first()
            if comment.liked_state == False:
                comment.liked_state = True
                new_like = TicketCommentLikes(
                    ticket_comment_id=comment_id
                )
                db.session.add(new_like)
                db.session.commit()
                db.session.flush()
                db.session.refresh(new_like)
            return jsonify(success=new_like.id)
        except:
            return jsonify(failed='Failed to like comment')


@ tickets.post("/unlike-comment")
def unlike_comment():
    comment_id = request.form['comment_id']
    comment_likes_id = request.form['comment_likes_id']
    comment = db.session.get(TicketComment, comment_id)
    try:
        if comment.liked_state == True:
            comment.liked_state = False
            like = db.session.get(
                TicketCommentLikes, comment_likes_id)
            db.session.delete(like)
            db.session.commit()
            return jsonify(success='Unliked')
    except:
        return jsonify(failed="Failed to unlike comment")
    # error found on comment_likes_id are sometimes null


@ tickets.post("/delete-comment")
def delete_comment():
    try:
        comment = db.session.get(TicketComment, request.form['comment_id'])
        db.session.delete(comment)
        db.session.commit()
        return jsonify(success='Deleted'), 200
    except:
        return jsonify(failed='Failed to delete comment'), 200
