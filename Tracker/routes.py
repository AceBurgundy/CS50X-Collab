
import os
import secrets
from PIL import Image
from flask import flash, redirect, render_template, request, jsonify, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker import app
from Tracker import db
from Tracker.models import User, Project, Conversations, Ticket
from flask_login import login_user, current_user, login_required, logout_user
from Tracker.helpers import apology
from Tracker.forms import profileForm, newProject, newTicket, changePassword

invalid = ["where","select","update","delete",".schema","from","drop","query"]

#!@$%^&*""_+}{":?></*+[;'./,]-/]

#Show all projects
@app.route("/")
@login_required
def index():
    """Show all user projects"""
    
    if request.method == "GET":
        form = profileForm()
        image_file = url_for('static', filename='profile_pictures/' + current_user.profile_picture)

        form.username.data = current_user.username
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.skills.data = current_user.skills
        form.address.data = current_user.address
        form.banner.data = current_user.banner
        form.country.data = current_user.country
        form.phone.data = current_user.phone 
         
    return render_template("index.html", form=form, image_file=image_file) #, projects=projects)

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

        try:           
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
            return apology("Login Unsucessful. Something was wrong on logging in user. line 71")

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

def save_picture(form_picture):
    random_value = secrets.token_hex(8)
    # fileName = "_"
    _, fileExtension = os.path.splitext(form_picture.filename)
    profilePictureFileName = random_value + fileExtension
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', profilePictureFileName)

    outputSize = (125,125)
    
    i = Image.open(form_picture)
    i.thumbnail(outputSize)
    i.save(picture_path)
        
    return profilePictureFileName

@app.route("/profile", methods=["POST"])
@login_required
def profile():
        
        form = profileForm()
        if request.method == "POST":
            
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
                
            db.session.commit()
            flash('account has been updated')
                
        return redirect('/')

# #Add project

@app.route("/add-project", methods=["GET", "POST"])
@login_required
def increase():

    form = newProject()
    if request.method == "POST":

        if form.validate_on_submit():
            
            title = request.form.get("title")
            description = request.form.get("content")
            deadline = request.form.get("deadline")
            
        
            project = Project(title = title, content = description, deadline = deadline)
            
            db.session.commit()


        return render_template("/")

# #Delete project

# @app.route("/delete-project", methods=["GET", "POST"])
# @login_required
# def increase():

#     if request.method == "POST":

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

 
