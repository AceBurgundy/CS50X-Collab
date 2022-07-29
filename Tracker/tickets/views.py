from flask import Blueprint
from flask import render_template, request, url_for
from Tracker.models import Ticket
from flask_login import login_required
tickets = Blueprint('tickets', __name__, template_folder='templates/tickets', static_folder='static/tickets')


#Add ticket

@tickets.route("/show-tickets/<int:current_project_id>")
@login_required
def show_tickets(current_project_id):

    if request.method == "GET":
        tickets = Ticket.query.filter_by(project_id=current_project_id)  
        return render_template("tickets.html", tickets=tickets, pageTitle="Tickets")

# @app.route("/add-ticket", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

#         user_id = session["user_id"]

#         try:
#             pendingVal = int(request.form.get("add"))
#         except:
#             return Apology(message="Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return Apology(message="value must between 0 and 10000")
#         db.execute("UPDATE users SET cash = ? WHERE id = ?", pendingVal, user_id)
#         return render_template("/")

# #Delete ticket

# @app.route("/delete-ticket", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

#         user_id = session["user_id"]

#         try:
#             pendingVal = int(request.form.get("add"))
#         except:
#             return Apology(message="Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return Apology(message="value must between 0 and 10000")
#         db.execute("UPDATE users SET cash = ? WHERE id = ?", pendingVal, user_id)
#         return render_template("/")