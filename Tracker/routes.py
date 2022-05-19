
from flask import flash, redirect, render_template #, request, session
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker import app
# from Tracker import db
# from Tracker.models import User, Project

from Tracker import helpers 

invalid = ["where","select","update","delete",".schema","from","drop"]

#!@$%^&*""_+}{":?></*+[;'./,]-/]

#Show all projects

@app.route("/")
# @login_required
def index():
    """Show all user projects"""

    # user_id = session["user_id"]

    projects = db.execute("SELECT * FROM projects WHERE id = ?", user.id)

    return render_template("index.html", projects=projects)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    # session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
      
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username")

        if username in invalid:
            return apology("username was not accepted")

        # Ensure password was submitted
        if not password:
            return apology("must provide password")

        if password in invalid:
            return apology("must provide password")


        # Query database for username
        current_user = db.execute("SELECT * FROM User WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(current_user) != 1:
            return apology("invalid username and/or password")

        if not check_password_hash(current_user[0]["hash"], password):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        # session["user_id"] = current_user[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    # session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    # session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not username:
            return apology("missing username")

        if username in invalid:
            return apology("username was not accepted")

        # Ensure email was submitted
        if not email:
            return apology("must provide an email")

        if "@" not in email and ".com" not in email:
            return apology("wrong email")

        # Ensure password was submitted
        if not password:
            return apology("must provide password")

        if password in invalid:
            return apology("must provide password")

        encrypted_password = generate_password_hash(password)

        # Query database for username
        try:
            db.execute("INSERT INTO User (username, email, password) VALUES(?,?,?)", username, email, encrypted_password)
            return redirect("/")
            # Redirect user to/ home page
        except:
            return apology("Something is wrong with the registration")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")

# #Add project

# @app.route("/add-project", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

#         user_id = session["user_id"]

#         try:
#             pendingVal = int(request.form.get("add"))
#         except:
#             return apology("Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return apology("value must between 0 and 10000")
#         db.execute("UPDATE users SET cash = ? WHERE id = ?", pendingVal, user_id)
#         return render_template("/")

# #Delete project

# @app.route("/delete-project", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

#         user_id = session["user_id"]

#         try:
#             pendingVal = int(request.form.get("add"))
#         except:
#             return apology("Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return apology("value must between 0 and 10000")
#         db.execute("UPDATE users SET cash = ? WHERE id = ?", pendingVal, user_id)
#         return render_template("/")

# #Add ticket

# @app.route("/add-ticket", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

#         user_id = session["user_id"]

#         try:
#             pendingVal = int(request.form.get("add"))
#         except:
#             return apology("Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return apology("value must between 0 and 10000")
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
#             return apology("Please place a value")

#         if pendingVal <= 0 or pendingVal > 10000:
#             return apology("value must between 0 and 10000")
#         db.execute("UPDATE users SET cash = ? WHERE id = ?", pendingVal, user_id)
#         return render_template("/")

 