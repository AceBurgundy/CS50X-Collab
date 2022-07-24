from flask import Blueprint

from flask import flash, redirect, render_template, request, url_for
from Tracker import db
from werkzeug.security import check_password_hash, generate_password_hash
from Tracker.helpers import apology
from flask_login import current_user, login_required
from Tracker.helpers import save_picture
from Tracker.profile.forms import (profileForm, ChangePassword)

profile = Blueprint('profile', __name__, template_folder='templates/profile', static_folder='static/profile')
        
@profile.route("/profile", methods=["POST","GET"])
@login_required
def _profile():
        
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
                flash('Successfully updated profile')    
                db.session.commit()
                return redirect(url_for('profile._profile'))
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
                
            return render_template("profile.html", form=form, image_file=image_file, passForm=passForm)

@profile.route("/change-password", methods=["POST"])
@login_required
def changePassword():
    form = ChangePassword()
    
    if form.validate_on_submit():
        if check_password_hash(current_user.password, form.password.data):
            current_user.password = generate_password_hash(form.newPassword.data)
            db.session.commit()            
            
            return redirect(url_for('index._index'))
        else:
            return apology("passwords does not match")
    else:
        return render_template("profile.html", form.form_errors)


 
