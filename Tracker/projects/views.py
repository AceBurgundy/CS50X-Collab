from Tracker import db
from Tracker.models import Project, User
from flask import redirect, render_template, jsonify, request, url_for, flash, Blueprint
from flask_login import current_user, login_required
from Tracker.projects.forms import ProjectForm
from sqlalchemy import update, select

projects = Blueprint('projects', __name__, template_folder='templates/projects', static_folder='static/projects')

@projects.route("/add-project", methods=["POST","GET"])
@login_required
def add_project():

    modal_title = "CREATE NEW PROJECT"
    form = ProjectForm()
    users = db.session.scalars(select(User)).all()
    if request.method == "POST":
        if form.validate_on_submit():

            try:
                db.session.add(Project(
                    title = form.title.data, 
                    description = form.description.data, 
                    deadline = form.deadline.data, 
                    author=current_user))
            
                db.session.commit()
                
                flash('Project added')
                return redirect(url_for('index._index'))
            except:
                flash('Failed to add project')
                return redirect(url_for('index._index'))
        else:
            return render_template('project-modal.html', users=users, modal_title=modal_title, form=form, error=form.errors)
    else:
        return render_template('project-modal.html', users=users, modal_title=modal_title, form=form)
    
@projects.route("/update-project/<int:current_project_id>", methods=["POST","GET"])
@login_required
def update_project(current_project_id):
    """ Update project """

    modal_title = "UPDATE THIS PROJECT"
    form = ProjectForm()
    project = Project.query.filter_by(id=current_project_id)
    users = db.session.scalars(select(User)).all()
    # unfixed
    if request.method == "POST":
        if form.validate_on_submit():
            try:
                db.session.execute(update(Project).where(Project.id==current_project_id).values(
                    title=form.title.data,
                    description=form.description.data,
                    deadline=form.deadline.data,
                    user_id=current_user.id))
                db.session.commit()
                
                if form.collaborate.data is not None:
                    for user in form.collaborate.data:
                        if user not in project.collaborators:
                            user.collaborated_projects.append(current_project_id)
                    print(project.collaborators)
                    db.session.commit()
                flash('Project updated')
                return redirect(url_for('index._index'))
            except:
                form.form_errors.append('Failed to update project ')
                return render_template('project-modal.html', project_collaborators=project.collaborators, users=users, project_id=current_project_id, modal_title=modal_title, form=form, error=form.errors)
        else:
            return render_template('project-modal.html', project_collaborators=project.collaborators, users=users, project_id=current_project_id, modal_title=modal_title, form=form, error=form.errors)
    else:
        project = Project.query.filter_by(id=current_project_id).first() 
        form.title.data = project.title 
        form.description.data = project.description
        form.deadline.data = project.deadline
        return render_template('project-modal.html', project_collaborators=project.collaborators, users=users, project_id=current_project_id, modal_title=modal_title, form=form)

@projects.route("/remove-collaborator", methods=["POST"])
@login_required
def remove_user():

    if request.method == "POST":
        
        project = Project.query.filter_by(id=request.args.get("current_project_id", type=int))

        user = User.query.filter_by(id=request.args.get("user_id", type=int))

        project.collaborators.remove(user)
        
    return jsonify(f'result=`{user.username}` removed', 200)

@projects.route("/leave_project", methods=["POST"])
@login_required
def leave_project():

    if request.method == "POST":
        
        project = Project.query.filter_by(id=request.args.get("current_project_id", type=int))

        user = User.query.filter_by(id=request.args.get("user_id", type=int))

        project.collaborators.remove(user)
        
    return jsonify(f'result=`{user.username}` had left the project', 200)

# Bookmark/Unbookmark a project

@projects.route("/bookmark/<int:current_project_id>", methods=["POST"])
@login_required
def bookmark_project(current_project_id):
    """ Bookmark project """

    if request.method == "POST":
        project_state = db.session.get(Project, current_project_id)
        print(project_state.bookmark_state)
        try:
            if project_state.bookmark_state == False:
                db.session.execute(update(Project).where(Project.id==current_project_id).values(bookmark_state=True))
                db.session.commit()
                flash('Project bookmarked')
                return redirect(url_for('index._index'))
                
            if project_state.bookmark_state == True:
                db.session.execute(update(Project).where(Project.id==current_project_id).values(bookmark_state=False))
                db.session.commit()
                flash('Project bookmark removed')
                return redirect(url_for('index._index'))
        except:
            flash('Project bookmark failed')
        return redirect(url_for('index._index'))

# Delete project

@projects.route("/delete/<int:current_project_id>", methods=["POST"])
@login_required
def delete_project(current_project_id):
    """ Delete project """

    if request.method == "POST":
        try:      
            db.session.delete(Project.query.get(current_project_id))
            db.session.commit()
            flash('Project deleted')
            return redirect(url_for('index._index'))
        except:
            flash('Project not found')
            return redirect(url_for('index._index'))