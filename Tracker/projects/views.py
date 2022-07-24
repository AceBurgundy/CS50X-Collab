from flask import Blueprint

from Tracker import db
from Tracker.models import Project
from flask import redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash
from flask_login import current_user, login_required
from Tracker.projects.forms import newProject

projects = Blueprint('projects', __name__, template_folder='templates/projects', static_folder='static/projects')

@projects.route("/add-project", methods=["POST","GET"])
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
            return redirect(url_for('index._index'))
        else:
            return render_template('new_project.html', form=form, error=form.errors)
    else:
        return render_template('new_project.html', form=form)

# Delete project

@projects.route("/delete-project", methods=["POST"])
@login_required
def deleteProject():
        
    if request.method == "POST":
        project_key = request.form['key']
        
        project = Project.query.filter_by(key=project_key).first()

        if project:
            db.session.delete(project)
        return redirect(url_for('index._index'))