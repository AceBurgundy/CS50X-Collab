
import os
import secrets
from PIL import Image
from flask import flash, redirect, render_template, request, jsonify, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker import app
from Tracker import db
from Tracker.models import User, Project, Conversations, Ticket, TicketComment
from flask_login import login_user, current_user, login_required, logout_user
from Tracker.helpers import apology, save_picture
from Tracker.forms import profileForm, newProject, newTicket, changePassword

invalid = ["where","select","update","delete",".schema","from","drop","query"]

#!@$%^&*""_+}{":?></*+[;'./,]-/]

#Show all projects
@app.route("/")
@login_required
def index():
    """Show all user projects"""
    pageTitle = "DASHBOARD"
    if request.method == "GET":
        form = profileForm()
    image_file = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

    if request.method == "GET":
        projects = Project.query.filter_by(user_id = current_user.id)  
        return render_template("index.html", projects=projects, image_file=image_file, pageTitle=pageTitle) #, projects=projects)

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

        # Ensure input is indeed an email
        if "@" not in emailInput and ".com" not in emailInput:
            return apology("Not an email")

        # Ensure password was submitted
        if not passwordInput:
            return apology("you must provide a password")

        # Ensure password has no invalid inputs
        if passwordInput.lower() in invalid:
            return apology("password was not accepted")

        user = User.query.filter_by(email=emailInput).first()

        if check_password_hash(user.password, passwordInput) == False:
            return apology("wrong password")
        
        try:           
            
            if user and check_password_hash(user.password, passwordInput):
                login_user(user) #, remember=form.remember.data)
                next_page = request.args.get('next')
            # Redirect user to home page
            return redirect('/') if next_page else redirect("/")
        except:
            return apology("Login Unsucessful. User have yet to register")

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
     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #ensure that there is no user that is currently logged in
        if current_user.is_authenticated:
            return redirect('/')

        emailInput = request.form.get("email")
        passwordInput = request.form.get("password")
        usernameInput = request.form.get("username")
         # Ensure that the user placed their email
        if not emailInput:
            return apology("missing email")

        # Ensure email has no invalid inputs
        if emailInput.lower() in invalid:
            return apology("email was not accepted")

        # Ensure input is indeed an email
        if "@" not in emailInput and ".com" not in emailInput:
            return apology("Not an email")

        # Ensure email has been already used 
        has_similar_email = User.query.filter_by(email=emailInput).first()

        if has_similar_email: 
            return apology("You have already used this email. Try another one")


        # Ensure password was submitted
        if not passwordInput:
            return apology("you must provide a password")

        # Ensure password has no invalid inputs
        if passwordInput.lower() in invalid:
            return apology("password was not accepted")

        # Ensure user inputs username
        if not usernameInput: 
            return apology("Please provide a username")
        
        # Ensure username has no invalid inputs
        if usernameInput.lower() in invalid:
            return apology("Invalid username, please try again")

        encryptedPassword = generate_password_hash(passwordInput)

        try:
            user = User(username = usernameInput, email = emailInput, password = encryptedPassword)
            
            db.session.add(user)
            db.session.commit()
            flash(f"Successfully created account.") #, success 

            # Redirect user to home page
            return redirect('/')
        except:
            return apology("Login Unsucessful. Something was wrong on logging in user. line 71")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")

@app.route("/change-password", methods=["POST"])
@login_required
def changePassword():
    form = ChangePassword()
    
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.password.data):
            current_user.password = generate_password_hash(form.newPassword.data)
            db.session.commit()            
            
            return redirect(url_for('index'))
        else:
            return apology("error in checking user.forms and form.data")
    else:
        return apology(form.form_errors)
        
        
        
@app.route("/profile", methods=["POST","GET"])
@login_required
def profile():
        
        form = profileForm()
        passForm = ChangePassword()
        image_file = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

        if request.method == "POST":
            if form.validate_on_submit():
                if form.profilePicture.data:  
                    current_user.profile_picture = save_picture(form.profilePicture.data)    
            
                current_user.username = form.username.data
                current_user.first_name = form.first_name.data
                current_user.last_name = form.last_name.data
                current_user.skills = form.skills.data
                current_user.address = form.address.data            
                current_user.banner = form.banner.data
                current_user.country = form.country.data
                current_user.phone = form.phone.data
                flash('Profile ave')    
                db.session.commit()
                return redirect(url_for('profile'))
            else:
                return render_template('profile.html', form=form, image_file=image_file, passForm=passForm, error=form.errors)
        else:      
            image_file = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

            form.username.data = current_user.username
            form.first_name.data = current_user.first_name
            form.last_name.data = current_user.last_name
            form.skills.data = current_user.skills
            form.address.data = current_user.address
            form.banner.data = current_user.banner
            form.country.data = current_user.country
            form.phone.data = current_user.phone
                
        return redirect('/')

# #Add project

@app.route("/add-project", methods=["POST","GET"])
@login_required
def addProject():

    form = newProject()
    if request.method == "POST":

        if form.validate_on_submit():
            input_title = form.title.data
            input_description = form.description.data
            input_deadline = form.deadline.data            
            
            project = Project(title = input_title, key=generate_password_hash(input_title), description = input_description, deadline = input_deadline, author=current_user)
            db.session.add(project)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return render_template('new_project.html', form=form, error=form.errors)
    else:
        return render_template('new_project.html', form=form)

# Delete project

@app.route("/delete-project", methods=["POST"])
@login_required
def deleteProject():
        
    if request.method == "POST":
        project_key = request.form['key']
        
        project = Project.query.filter_by(key=project_key).first()

        if project:
            db.session.delete(project)
        return redirect(url_for('index'))

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

 
