from flask import Blueprint

from Tracker import db
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker.helpers import apology
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user
from Tracker.helpers import apology
from Tracker.models import User

invalid = ["where","select","update","delete",".schema","from","drop","query"]

user = Blueprint('user', __name__, template_folder='templates/user', static_folder='static/user')

@user.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    logout_user()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #ensure that there is no user that is currently logged in
        if current_user.is_authenticated:
            return redirect(url_for('index._index'))

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

        if not user:
            return apology("wrong email or user not registered")
        
        if check_password_hash(user.password, passwordInput) == False:
            return apology("wrong password or user not registered")

        try:           
            
            if user and check_password_hash(user.password, passwordInput):
                login_user(user) #, remember=form.remember.data)
                next_page = request.args.get('next')
            # Redirect user to home page
            return redirect(url_for('index._index')) if next_page else redirect(url_for('index._index'))
        except:
            return apology("Login Unsucessful. User have yet to register")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")


@user.route("/logout")
def logout():
    """Log user out"""

    logout_user()
    return render_template('users.html')


@user.route("/register", methods=["GET", "POST"])
def register():
     # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        #ensure that there is no user that is currently logged in
        if current_user.is_authenticated:
            return redirect(url_for('index._index'))

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
            return redirect(url_for('index._index'))
        except:
            return apology("Login Unsucessful. Something was wrong on logging in user. line 71")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("users.html")

