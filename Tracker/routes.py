
from flask import flash, redirect, render_template, request
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker import app
from Tracker import db
from Tracker.models import User, Project
from flask_login import login_user, current_user, login_required, logout_user
from Tracker.helpers import apology

invalid = ["where","select","update","delete",".schema","from","drop"]

#!@$%^&*""_+}{":?></*+[;'./,]-/]

#Show all projects
@app.route("/")
@login_required
def index():
    """Show all user projects"""

    # projects = User.querry.all()

    return render_template("index.html") #, projects=projects)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    logout_user()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #ensure that there is no user that is currently logged in
        if current_user.is_authenticated:
            return redirect('/')

        emailInput = request.form.get("email")
        passwordInput = request.form.get("password")

        # Ensure that the user placed their email
        if not emailInput:
            return apology("missing email")

        # Ensure email has no invalid inputs
        if emailInput.lower() in invalid:
            return apology("email was not accepted")

        # Ensure input is indeed an emailInput
        if "@" not in emailInput and ".com" not in emailInput:
            return apology("Not an email")

        # Ensure passwordInput was submitted
        if not passwordInput:
            return apology("you must provide a password")

        # Ensure passwordInput has no invalid inputs
        if passwordInput.lower() in invalid:
            return apology("password was not accepted")

        try:
            user = User.query.filter_by(email=emailInput).first()
            
            if user and check_password_hash(user.password, passwordInput):
                login_user(user) #, remember=form.remember.data)
                next_page = request.args.get('next')
            # Redirect user to home page
            return redirect('/') if next_page else redirect("/")
        except:
            return apology("Login Unsucessful. Something was wrong on loging in user. line 71")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")


@app.route("/logout")
def logout():
    """Log user out"""

    logout_user()
    return render_template('users.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    logout_user()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #Check if there is a user currently logged in
        if current_user.is_authenticated:
            #if true, redirect them back to the homepage
            return redirect('/')

        usernameInput = request.form.get("username")
        emailInput = request.form.get("email")
        passwordInput = request.form.get("password")

        #ensure that the user placed their username
        if not usernameInput:
            return apology("missing username")

        # Ensure username has no invalid inputs
        if usernameInput.lower() in invalid:
            return apology("username was not accepted")

        #querries the database for similar usernames
        #returns a value if found else none
        has_similar_username = User.query.filter_by(username=usernameInput).first()
        
        if has_similar_username:
            return apology("Username is already taken")

        # Ensure email was submitted
        if not emailInput:
            return apology("must provide an email")

        # Ensure input is indeed an email
        if "@" not in emailInput and ".com" not in emailInput:
            return apology("Not an email")

        #querries the database for similar email
        #returns a value if found else none
        has_similar_email = User.query.filter_by(email=emailInput).first()
        
        if has_similar_email:
            return apology("You can only use the same email once")

        # Ensure password was submitted
        if not passwordInput:
            return apology("must provide password")

        # Ensure password has no invalid inputs
        if passwordInput.lower() in invalid:
            return apology("password was not accepted")

        encrypted_password = generate_password_hash(passwordInput)

        # Add new user to the database
        try:
            user = User(username=usernameInput, email=emailInput, password=encrypted_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Succesfully created account') #,success')
            return redirect("/")
            # Redirect user to home page
        except:
            return apology("Something went wrong when trying to push to the database")

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

 