from flask import Blueprint

from Tracker import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user
from Tracker.models import User
from Tracker.user.forms import RegisterForm, LoginForm

user = Blueprint('user', __name__, template_folder='templates/user', static_folder='static/user')

@user.route("/login", methods=["GET", "POST"])
def login():
    """Logs user in"""

    logout_user()

    form = LoginForm()
    
    if request.method == "POST":

        if current_user.is_authenticated:
            return redirect(url_for('index._index'))

        email_input = form.login_email.data
        password_input = form.login_password.data

        user = User.query.filter_by(email=email_input).first()

        try:           
            if user and check_password_hash(user.password, password_input):
                login_user(user) #, remember=form.remember.data)
                next_page = request.args.get('next')
            return redirect(url_for('index._index')) if next_page else redirect(url_for('index._index'))
        except:
            form.form_errors.append("Login Unsuccesful")
            return render_template("login.html", form=form, errors=form.form_errors)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", form=form)


@user.route("/logout")
def logout():
    """Log user out"""

    logout_user()
    return redirect(url_for('user.login'))


@user.route("/register", methods=["GET", "POST"])
def register():
    """Register User in""" 
    
    form = RegisterForm()
    
    if request.method == "POST":

        if current_user.is_authenticated:
            return redirect(url_for('index._index'))

        if form.validate_on_submit():
            username_input = form.register_username.data
            email_input = form.register_email.data
            password_input = form.register_password.data

            encryptedPassword = generate_password_hash(password_input)

            try:
                user = User(username=username_input, email=email_input, password=encryptedPassword)
                
                db.session.add(user)
                db.session.commit()
                flash(f"Successfully created account.")
                return render_template("login.html")
            except:
                form.form_errors.append("Login Unsucessful. Something was wrong on logging in user")
                return render_template("register.html", form=form, errors=form.form_errors)
    else:
        return render_template("register.html", form=form)

